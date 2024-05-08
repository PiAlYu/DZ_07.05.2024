fin = open('27-B.txt')
a = fin.readlines()
fin.close()
a = [int(i) for i in a]
n = a.pop(0)
s = 0
b = [[0 for i in range(9)] for j in range(9)]
for i in range(n):
    for j in range(9):
        ind = (i - a[i] - j) % 9
        s += b[j][ind]
    b[i % 9][a[i] % 9] += 1
print(s % 10 ** 6)