"""Write a program that checks if a number is even or odd.

Task:
Ask the user to enter a number.
Check if the number is even or odd.
Print "The number is even" if it is even, or "The number is odd" if it is odd."""

number = int(input("Enter the number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")