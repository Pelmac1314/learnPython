"""Create a program that displays the multiplication table for a given number.

Task:
Ask the user for a number.
Print the multiplication table for that number from 1 to 10.
For example, if the user enters 3, the program should print:
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30"""

number = int(input("Please enter the number to multiply with: "))

for i in range(1,11):
    result = number * i
    print(i, "x", number, "=", result)