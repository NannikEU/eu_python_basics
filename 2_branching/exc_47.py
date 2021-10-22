# 47.

x = float(input("x:"))
y = float(input("y:"))
z = float(input("z:"))

if (x <= 0) | (y <= 0) | (z <= 0):
    return

isTriangle = False
isSharp = False

if (x + y > z) && (y + z > x) && (z + x > y):
    isTriangle = True

    if (x >= y) & (x >= z):
        if x * x > y * y + z * z:
            isSharp = True
    elif (y >= z) & (y >= x):
        if y * y > x * x + z * z:
            isSharp = True
    elif (z >= x) & (z >= y):
        if z * z > y * y + x * x:
            isSharp = True

print("isTriangle: ", isTriangle)
if (isTriangle):
    print("isSharp: ", isSharp)
