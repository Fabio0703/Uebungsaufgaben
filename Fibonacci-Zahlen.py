n = int(input("Gib eine Zahl ein: "))
a,b=0,1

print("Fibonacci-Folge bis", n, ":")
while a <= n:
    print(a, end=' ')
    a, b = b, a + b