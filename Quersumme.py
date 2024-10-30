number = int(input("Zahl: "))
result = 0
while number > 0:
    result += number % 10
    number = number // 10
print(result)