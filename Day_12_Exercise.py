# Exercises: Level 1
# 1. Write a function which generates a six digit/character random_user_id.
import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ""
    for i in range(6):
        user_id = user_id + random.choice(characters)
    return user_id
print(random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_characters = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of IDs: "))
    characters = string.ascii_letters + string.digits

    for _ in range(num_ids):
        user_id = ""
        for _ in range(num_characters):
            user_id += random.choice(characters)
        print(user_id)
print(user_id_gen_by_user())

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return f"rgb({r}, {g}, {b})"
print(rgb_color_gen())

# Exercises: Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n):
    colors = []
    hex_digits = "0123456789abcdef"

    for l in range(n):
        color = "#"
        for a in range(6):
            color += random.choice(hex_digits)
        colors.append(color)
    return colors
print(list_of_hexa_colors(int(input("Enter number of hexadecimal: "))))

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        colors.append(f"rgb({r}, {g}, {b})")
    return colors

print(list_of_rgb_colors(int(input("Enter number of rgb: "))))

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, n):
    if color_type.lower() == "hexa":
        return list_of_hexa_colors(n)
    elif color_type.lower() == "rgb":
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type."

color_type = input("Enter color type (hexa or rgb): ")
n = int(input("Enter number of colors: "))
print(generate_colors(color_type, n))

# Exercises: Level 3
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
print("Shuffled list:", shuffle_list(numbers))

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    return random.sample(range(10), 7)
print(unique_random_numbers())
