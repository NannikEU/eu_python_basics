# 42. Даны действительные числа х, y (х != у ). Меньшее из этих двух чисел заменить их полусуммой, а большее — их удвоенным произведением.

x = int(input("a: "))
y = int(input("b: "))

if x == y:
    return

min = (x + y) / 2
max = x * y

if x < y:
    x = min
    y = max
else:
    x = max
    y = min

print("x:", x)
print("y:", y)
