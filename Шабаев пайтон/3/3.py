for i in range(1, 11):
    print(i)

for i in range(1, 6):
    print(i ** 2)

total = 0
for i in range(1, 101):
    total += i
print("Сумма:", total)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

for i in range(1, 11):
    print(f"3 * {i} = {3 * i}")

for i in range(10, 0, -1):
    print(i)

factorial = 1
for i in range(1, 6):
    factorial *= i
print("Факториал 5:", factorial)

for i in range(1, 31):
    if i % 3 == 0:
        print(i)

a, b = 0, 1
while a <= 100:
    print(a, end=" ")
    a, b = b, a + b