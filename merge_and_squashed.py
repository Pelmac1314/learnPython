number = int(input())  
numbers = [input().strip() for _ in range(number)]  


merged = []
squashed = []


for i in range(number - 1):
    num1 = numbers[i]
    num2 = numbers[i + 1]
    
    merged.append(num1[1] + num2[0])
    
    a = num1[0]
    b = int(num1[1])
    c = int(num2[0])
    d = num2[1]
    middle = (b + c) % 10  
    squashed.append(a + str(middle) + d)


print(" ".join(merged))
print(" ".join(squashed))