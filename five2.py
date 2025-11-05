import time
import datetime

# Step 1: Get current date and time
current_time = datetime.datetime.now()

# Step 2: Display details
print("Current Date and Time:", current_time)
print("Current Year:", current_time.year)
print("Month of the Year:", current_time.month)
print("Week Number of the Year:", current_time.strftime("%U"))
print("Weekday of the Week:", current_time.strftime("%A"))
print("Day of Year:", current_time.strftime("%j"))
print("Day of Month:", current_time.day)
print("Day of Week:", current_time.isoweekday())  # Monday=1 ... Sunday=7
