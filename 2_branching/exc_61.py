# 61. Дано действительное число х. Получить целую часть числа х; затем — число х, округленное до ближайшего целого; затем— число х без дробных цифр.

# Я специально не использовал встроенные арифметические методы
x = float(input("x: "))

xInt = x - (x % 1)

print(xInt)

remainder = x % 1 * 10
if (remainder >= 5):
    print(xInt + 1)
else:
    print(xInt)

print(int(xInt))
