# 377. Дана действительная квадратная матрица порядка !2.
# Заменить нулями все ее элементы, расположенные на главной диагонали и выше нее.

n = 1

for i in range(3):
    n *= i + 1

A = []
for i in range(n):
    A.append([1] * n)

for i in range(len(A)):
    for j in range(i, len(A[i]), 1):
        A[i][j] = 0

for row in A:
    print(row)
