# 317

n = 10

sum = 0
for i in range(n):
    a = float(input("a{}:".format(i + 1)))
    for j in range(i):
        a *= a
    sum += a

print(sum)