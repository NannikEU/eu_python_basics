#67.

n = int(input("n: "))

t = n

i = 0
sum = 0
first = 0

while t > 0:
    i += 1
    sum += t % 10

    if t < 10:
        first = t

    t = int(t / 10)


if n >= 10:
    print(i, sum, n % 10, first, int(n / 10) % 10)
else:
    print(i, sum, n % 10, first)
