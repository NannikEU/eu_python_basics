# 45.

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = int(input("d:"))

if (a <= b) & (b <= c) & (c <= d):
    a = d
    b = d
    c = d
elif not ((a > b) & (b > c) & (c > d)):
    a *= a
    b *= b
    c *= c
    d *= d

print(a, b, c, d)
