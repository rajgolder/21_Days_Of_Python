#!/usr/bin/env python3
"""CommitCraft CLI — local git diff to conventional commit message."""

from __future__ import annotations

import argparse
import collections
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

KV_SECRET_RE = re.compile(
    r"(?i)\b(api[_-]?key|secret|token|password|passwd|pwd|client_secret|access_token|refresh_token|private_key)\b\s*[:=]\s*['\"]?[^'\"\s,;]+"
)
AUTH_HEADER_RE = re.compile(r"(?i)\bauthorization\b\s*[:=]\s*[^,\n]+")
BEARER_RE = re.compile(r"(?i)\bbearer\b\s+[A-Za-z0-9._~+/=-]+")
AWS_ACCESS_KEY_RE = re.compile(r"\bAKIA[0-9A-Z]{16}\b")
GITHUB_TOKEN_RE = re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{36,}\b")
JWT_RE = re.compile(r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b")
PRIVATE_KEY_RE = re.compile(
    r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |)?PRIVATE KEY-----.*?-----END (?:RSA |EC |OPENSSH |DSA |)?PRIVATE KEY-----",
    re.DOTALL,
)
LONG_TOKEN_RE = re.compile(r"[A-Za-z0-9_\-+/=\.]{24,}")

COMMIT_TYPES = [
    "feat",
    "fix",
    "docs",
    "style",
    "refactor",
    "test",
    "chore",
    "perf",
]


def git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        text=True,
        capture_output=True,
    )

    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or f"git {' '.join(args)} failed")

    return result.stdout


def get_diff(include_unstaged: bool = False) -> str:
    staged = git(["diff", "--no-ext-diff", "--staged"])

    if include_unstaged:
        unstaged = git(["diff", "--no-ext-diff"])
        return staged + "\n" + unstaged

    return staged


def redact_high_entropy(text: str) -> tuple[str, int]:
    redacted = text
    count = 0

    for token in set(LONG_TOKEN_RE.findall(text)):
        if len(token) >= 24 and len(set(token)) / len(token) > 0.45:
            redacted = redacted.replace(token, "REDACTED_SECRET")
            count += text.count(token)

    return redacted, count


def redact_credentials(text: str) -> tuple[str, int]:
    redacted, count = KV_SECRET_RE.subn(
        lambda match: f"{match.group(1)}=REDACTED_SECRET",
        text,
    )

    redacted, n = AUTH_HEADER_RE.subn("authorization: REDACTED_SECRET", redacted)
    count += n

    redacted, n = BEARER_RE.subn("Bearer REDACTED_SECRET", redacted)
    count += n

    for pattern in [
        AWS_ACCESS_KEY_RE,
        GITHUB_TOKEN_RE,
        JWT_RE,
        PRIVATE_KEY_RE,
    ]:
        redacted, n = pattern.subn("REDACTED_SECRET", redacted)
        count += n

    redacted, n = redact_high_entropy(redacted)
    count += n

    return redacted, count


def parse_diff(diff: str) -> dict[str, object]:
    paths: set[str] = set()
    added_lines = 0
    deleted_lines = 0
    added_files = 0
    deleted_files = 0
    current_path: str | None = None

    for line in diff.splitlines():
        if line.startswith("diff --git "):
            parts = line.split()
            current_path = None

            if len(parts) >= 4:
                raw = parts[-1]
                if raw.startswith("b/"):
                    current_path = raw[2:]
                elif raw != "/dev/null":
                    current_path = raw

            if current_path:
                paths.add(current_path)

            continue

        if line.startswith("+++ "):
            if line.startswith("+++ /dev/null"):
                deleted_files += 1
                current_path = None
                continue

            path = line[4:].strip()
            if path.startswith("b/"):
                path = path[2:]

            current_path = path
            paths.add(path)
            continue

        if line.startswith("--- "):
            if line.startswith("--- /dev/null"):
                added_files += 1
            continue

        if line.startswith("+") and not line.startswith("+++"):
            added_lines += 1
        elif line.startswith("-") and not line.startswith("---"):
            deleted_lines += 1

    return {
        "paths": paths,
        "added_lines": added_lines,
        "deleted_lines": deleted_lines,
        "added_files": added_files,
        "deleted_files": deleted_files,
        "modified_files": max(0, len(paths) - added_files - deleted_files),
    }


def infer_type(diff: str, stats: dict[str, object]) -> str:
    paths = {str(path).lower() for path in stats["paths"]}
    lowered = diff.lower()

    if any(word in lowered for word in [" bug ", " fix ", "crash", "exception", " failed", " failure"]):
        return "fix"

    if any("test" in path for path in paths) or "test" in lowered:
        return "test"

    if "refactor" in lowered:
        return "refactor"

    if "perf" in lowered or "performance" in lowered:
        return "perf"

    if any(word in lowered for word in ["style", "format", "lint"]):
        return "style"

    if "doc" in lowered or any(path.endswith((".md", ".rst", ".txt")) for path in paths):
        return "docs"

    if stats["added_files"] and not stats["modified_files"] and not stats["deleted_files"]:
        return "feat"

    if any(path.startswith(("src/", "app/", "lib/", "packages/")) for path in paths):
        return "feat"

    return "chore"


def infer_scope(paths: Iterable[str]) -> str:
    scopes: list[str] = []

    for raw_path in paths:
        path = Path(str(raw_path))

        if path.name in {"/dev/null", "."}:
            continue

        if len(path.parts) > 1 and path.parts[0] not in {"test", "tests"}:
            scopes.append(path.parts[0])
        else:
            scopes.append(path.stem or path.name)

    if not scopes:
        return ""

    return collections.Counter(scopes).most_common(1)[0][0]


def trim(text: str, limit: int = 72) -> str:
    if len(text) <= limit:
        return text

    return text[: limit - 3].rstrip() + "..."


def build_subject(stats: dict[str, object], scope: str) -> str:
    scope = scope or "project"
    paths = {str(path).lower() for path in stats["paths"]}
    added_lines = int(stats["added_lines"])
    deleted_lines = int(stats["deleted_lines"])

    if int(stats["deleted_files"]) and not int(stats["added_files"]):
        return f"remove {scope}"

    if any("test" in path for path in paths) and added_lines:
        return f"add tests for {scope}"

    if int(stats["added_files"]) and not int(stats["modified_files"]) and not int(stats["deleted_files"]):
        return f"add {scope}"

    if deleted_lines and not added_lines:
        return f"remove {scope} logic"

    if added_lines >= deleted_lines:
        return f"update {scope} behavior"

    return f"clean up {scope}"


def build_body(stats: dict[str, object], redaction_count: int, include_body: bool) -> str:
    if not include_body:
        return ""

    paths = sorted(str(path) for path in stats["paths"])
    shown_paths = paths[:8]
    suffix = ""

    if len(paths) > len(shown_paths):
        suffix = f"\n- ...and {len(paths) - len(shown_paths)} more"

    lines = [
        f"Changed files: {', '.join(shown_paths)}{suffix}",
        f"Stats: +{stats['added_lines']}/-{stats['deleted_lines']}",
    ]

    if redaction_count:
        lines.append("Security: potential credentials were redacted before message generation.")

    return "\n".join(lines)


def generate_message(
    diff: str,
    scope_override: str | None = None,
    type_override: str | None = None,
    include_body: bool = True,
) -> str | None:
    clean_diff, redaction_count = redact_credentials(diff)
    stats = parse_diff(clean_diff)

    if not stats["paths"]:
        return None

    commit_type = type_override or infer_type(clean_diff, stats)
    scope = scope_override or infer_scope(stats["paths"])
    subject = trim(build_subject(stats, scope))
    body = build_body(stats, redaction_count, include_body)

    scope_part = f"({scope})" if scope else ""
    message = f"{commit_type}{scope_part}: {subject}"

    if body:
        message += f"\n\n{body}"

    return message


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate a conventional commit message from local git changes."
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Include unstaged changes in addition to staged changes.",
    )
    parser.add_argument(
        "--scope",
        help="Override the conventional commit scope.",
    )
    parser.add_argument(
        "--type",
        choices=COMMIT_TYPES,
        help="Override the conventional commit type.",
    )
    parser.add_argument(
        "--commit",
        action="store_true",
        help="Create the git commit using the generated message.",
    )
    parser.add_argument(
        "--no-body",
        action="store_true",
        help="Print only the subject line.",
    )

    args = parser.parse_args(argv)

    try:
        git(["rev-parse", "--is-inside-work-tree"])
    except SystemExit:
        print("CommitCraft must be run inside a git repository.", file=sys.stderr)
        return 1

    diff = get_diff(include_unstaged=args.all)

    if not diff.strip():
        target = "staged or unstaged" if args.all else "staged"
        print(f"No {target} changes found.", file=sys.stderr)
        return 1

    message = generate_message(
        diff,
        scope_override=args.scope,
        type_override=args.type,
        include_body=not args.no_body,
    )

    if message is None:
        print("Could not generate a commit message.", file=sys.stderr)
        return 1

    if args.commit:
        result = subprocess.run(
            ["git", "commit", "-m", message],
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            print(result.stderr or result.stdout, file=sys.stderr)
            return result.returncode

        print(result.stdout or "Commit created.")
        return 0

    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())