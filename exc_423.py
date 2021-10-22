# 423
import math
import random


def a():
    result = 0

    for i in range(n):
        result += A[i][0]

    return result


def b():
    result = 0

    for i in range(n):
        result += A[i][i]

    for i in range(n):
        result += A[i][n - i - 1]

    if n % 2 == 1:
        result -= A[math.floor(n / 2)][math.floor(n / 2)]

    return result


def c():
    max = A[0][0]

    for j in range(2, n):
        if A[0][j] > max:
            max = A[0][j]

    for j in range(n):
        if A[n - 1][j] > max:
            max = A[n - 1][j]

    return max


def d():
    if n < 3:
        print("n must be > 3")
        return 0

    min = A[0][n - 1]

    for i in range(n - 2, -1, -1):
        if A[i][n - i - 1] < min:
            min = A[i][n - i - 1]

    for i in range(n - 1, -1, -1):
        if A[i][n - i - 2] < min:
            min = A[i][n - i - 2]

    for i in range(n - 2, -1, -1):
        if A[i - 1][n - i - 1] < min:
            min = A[i - 1][n - i - 1]

    return min


def e():
    result = 0

    m = int(input("print m: "))
    if m > 2 * n:
        print("m must be <= {}".format(2 * n))
        return 0

    i = m
    j = 0

    while i >= 0:
        if i < len(A):
            if j < len(A[i]):
                result += A[i][j]
        i -= 1
        j += 1

    return result


def f():
    min = A[0][n - 1]
    max = A[0][0]

    for i in range(1, n):
        if A[i][i] > max:
            max = A[i][i]

    for i in range(1, n):
        if A[i][n - i - 1] < min:
            min = A[i][n - i - 1]

    return max > min


n = int(input("n: "))
A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(0, 9))
    A.append(row)

print("")
for row in A:
    print(row)

print("\na:", a())
print("b:", b())
print("c:", c())
print("d:", d())
print("e:", e())
print("f:", f())
