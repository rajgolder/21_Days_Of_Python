# Import the datetime module to access date and time classes and functions.
import datetime
# Display all available attributes and methods of the datetime module.
print(dir(datetime))

# Import the datetime class for working with current date and time.
from datetime import datetime
# Get the current date and time.
now = datetime.now()
print(now)
# Extract individual components from the current date-time.
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
# Get the current timestamp in seconds since the Unix epoch.
timestamp = now.timestamp
print(day, month, year, hour, minute)
print('timestamp', timestamp)
# Print the date in a readable day/month/year and hour:minute format.
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Import datetime class again for creating a custom date-time object.
from datetime import datetime
# Create a specific date-time object for New Year 2027.
new_year = datetime(2027, 1, 1)
print(new_year)
# Extract date and time parts from the custom date-time object.
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
# Format the custom date-time for display.
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Import datetime class for formatting date-time objects.
from datetime import datetime
# Get the current time and format it in different styles.
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
# Format date and time as day/month/year, hour:minute:second.
time_one = now.strftime("%d/%m/%Y, %H:%M:%S")
print('time one:', time_one)
# Format date and time again using the same pattern.
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two:", time_two)

# Import datetime class to parse a string into a date-time object.
from datetime import datetime
# Define a date string and convert it to a datetime object using the specified format.
date_string = "5 December, 2026"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# Import the date class for working with calendar dates only.
from datetime import date
# Create a specific date and print it.
d = date(2026, 1, 1)
print(d)
# Display today's date using the date class.
print("Current date:", d.today())
# Get today's date and print its separate year, month, and day components.
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# Import the time class for working with time-of-day values.
from datetime import time
# Create default time object with zeroed values.
a = time()
print('a =', a)
# Create a time object with specified hour, minute, and second.
b = time(10, 30, 50)
print('b =', b)
# Create a time object using named arguments for clarity.
c = time(hour=10, minute=30, second=50)
print("c =", c)
# Create a time object including microseconds.
d = time(10, 30, 50, 200435)
print("d =", d)

# Import date and datetime classes to calculate differences between dates.
from datetime import date, datetime
# Define today's date and the date for the next New Year.
today = date(year=2026, month=7, day=1)
new_year = date(year=2027, month=1, day=1)
# Calculate the number of days remaining until New Year.
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

# Create two datetime objects and find the difference between them.
t1 = datetime(year=2026, month=7, day=1, hour=0, minute=59, second=0)
t2 = datetime(year=2027, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print('Time left for new year:', diff)

# Import timedelta to work with durations of time.
from datetime import timedelta
# Create two time durations and subtract them to get the difference.
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
