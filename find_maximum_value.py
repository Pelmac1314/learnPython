"""Write a program that finds the largest number in a list.

Task:
Create a list of numbers.
Loop through the list to find the maximum value.
Print the maximum number."""

my_list = [1, 15, 123, 124234, 43, 12, 65]

max_list = 0

for i in my_list:
    if i > max_list:
        max_list = i
    
print(max_list)