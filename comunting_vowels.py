"""Write a program that counts the number of vowels in a sentence.

Task:
Ask the user to enter a sentence.
Count the vowels (a, e, i, o, u) in the sentence.
Print the number of vowels found."""

sentence = input("Enter the sentence to count vowels: ").strip().lower()

vowels = "aeiou"
vowels_count = 0

for j in sentence:
    if j in vowels:
        vowels_count += 1
        
print("Total vowels:", vowels_count)