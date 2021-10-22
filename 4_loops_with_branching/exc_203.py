# 203

n = int(input("n: "))
c = []
t = []
s = 0
minI = 0
for i in range(n):
    t.append(float(input("t{}:".format(i + 1))))
    c.append(s)
    s += t[i]
    if t[i] < t[minI]:
        minI = i

print(c)
print(t[minI])
