# 117. Дано натуральное число п. Вычислить произведение первых п сомножителей:

n = int(input("n: "))

r1 = 1
r2 = 1

# a)
top = 1
bottom = 2

for i in range(n):
    r1 *= top / bottom
    top += 2
    bottom += 2


# b
top = 1
bottom = 1

for i in range(n):
    r2 *= top / bottom
    top += 2
    bottom += 1

print("a:", r1)
print("b:", r2)