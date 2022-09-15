n = int(input())
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

p = n
def negafibonacci(p):
    return (-1)**(p+1)*fibonacci(p)

a = []
for i in range(1, n+1):
    a.append(negafibonacci(i))
a = a[::-1]

b = []
for i in range(1, n+1):
    b.append(fibonacci(i))

c = a+b
print(c)