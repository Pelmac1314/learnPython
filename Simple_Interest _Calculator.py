"""Create a program to calculate simple interest.

Task:
Ask the user for the principal amount, rate of interest, and time (in years).
Calculate the simple interest using the formula:
Simple Interest= Principal x Rate x Time / 100
 
Print the calculated interest."""

principal_amount = float(input("Please enter the principal amount: "))
rate_of_interest = float(input("Please enter the rate of interest: "))
time = float(input("Please enter the time: "))

calculated_interest = principal_amount * rate_of_interest * time / 100

print("Simple Interest is: ", calculated_interest)