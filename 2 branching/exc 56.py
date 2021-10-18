# 56. Даны действительные положительные числа а, Ь, с, х, у. Выяснить, пройдет ли кирпич с ребрами а, Ь, с
# в прямоугольное отверстие со сторонами х и у. Просовывать кирпич в отверстие разрешается только так, чтобы
# каждое из его ребер было параллельно или перпендикулярно каждой из сторон отверстия.


a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
x = float(input("x:"))
y = float(input("y:"))

min1 = a
min2 = b
result = False

if (b < a) & (b < c):
    min1 = b
    if (a < c):
        min2 = a
    else:
        min2 = c
elif (c < a) & (c < b):
    min1 = c
    if (b < a):
        min2 = b
    else:
        min2 = a

if ((min1 <= x) & (min2 <= y)) & ((min2 <= x) & (min1 <= y)):
    result = True

print(result)
