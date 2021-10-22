from random import choice

n = int(input("n: "))

A = []

for i in range(n):
    row = []
    for j in range(n):
        if j < i:
            row.append([None, None])
        elif i == j:
            row.append([False, False])
        else:
            row.append([choice([True, False]), choice([True, False])])

    A.append(row)

for i in range(len(A)):
    for j in range(i):
        A[i][j][0] = not A[j][i][0]
        A[i][j][1] = not A[j][i][1]

teamsWins = []
count = 0
topTeams = []
for i in range(len(A)):
    teamsWins.append(0)
    for game in A[i]:
        for score in game:
            if score:
                teamsWins[i] += 1
    if teamsWins[i] > n - 1:
        count += 1
    if teamsWins[i] == (n - 1) * 2:
        topTeams.append(i + 1)

for row in A:
    print(row)

print("a)", count)
print("b)", topTeams)
print("c)", count > 0)