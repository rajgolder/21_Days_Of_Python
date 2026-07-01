# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
current = datetime.now()
print(current.day)
print(current.month)
print(current.year)
print(current.hour)
print(current.minute)
print(current.timestamp())


# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
from datetime import datetime
current = datetime.now()
formatted = current.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted)

# 3. Today is 5 December, 2019. Change this time string to time.
from datetime import datetime
date_string = "5 December 2026"
date_object = datetime.strptime(date_string, "%d %B %Y")
print(date_object)

# 4. Calculate the time difference between now and new year.
from datetime import datetime
now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)
difference = new_year - now
print(difference)

# 5. Calculate the time difference between 1 January 1970 and now
from datetime import datetime
old = datetime(1970, 1, 1)
now = datetime.now()
difference = now - old
print(difference)