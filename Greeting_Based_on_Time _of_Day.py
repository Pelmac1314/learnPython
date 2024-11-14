"""Write a program that greets the user based on the time of day.

Task:
Ask the user to enter the current hour (in 24-hour format).
If the hour is between 6 and 12, print "Good Morning!"
If the hour is between 12 and 18, print "Good Afternoon!"
If the hour is between 18 and 22, print "Good Evening!"
For any other time, print "Good Night!"
"""

user_input = int(input("Please enter the current hour (in 24-hour format): "))
if 6 < user_input < 12:
    print("Good Morning!")
elif 12 < user_input < 18:
    print("Good Afternoon!")
elif 18 < user_input < 22:
    print("Good Evening!")
else:
    print("Good Night!")