# Weekly task 5
# Write a program that outputs whether or not today is a weekday
# You will need to search the web to find how you work out what day it is:
# Ref;
# https://www.w3schools.com/python/python_datetime.asp
# https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python#:~:text=date%20using%20datetime.-,datetime.,)%20to%206%20(Sunday).
# https://www.w3schools.com/python/python_conditions.asp

# An example of running this program on a Thursday is given below.
# $ python weekday.py
# Yes, unfortunately today is a weekday.

# An example of running it on a Saturday is as follows:
#$ python weekday.py
# It is the weekend, yay!

import datetime

today = datetime.datetime.today()

if today.weekday() == 4:
    print("Bravissimo! It's almost the weekend!")
elif today.weekday() == 5 or today.weekday() == 6:
    print("Yes! It's the weekend!")
else: 
    days_to_weekend = 4 - today.weekday()
    print(f"{days_to_weekend} days until the weekend.")

