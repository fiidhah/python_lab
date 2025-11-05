import calendar

# Step 1: Get user input
year = int(input("Enter a year: "))

# Step 2: Check leap year
if calendar.isleap(year):
    print(year, "is a Leap Year.")
else:
    print(year, "is Not a Leap Year.")
