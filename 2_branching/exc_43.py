# 43. Даны три действительные числа. Возвести в квадрат те из них, значения которых неотрицательны.

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a >= 0:
    a *= a

if b >= 0:
    b *= b

if c >= 0:
    c *= c

print("a:", a)
print("b:", b)
print("c:", c)
