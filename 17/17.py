fin = open('17.txt')
a = fin.readlines()
fin.close()
a = [int(i) for i in a]
k, m = 0, 0
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) % 10 == 0:
        k += 1
        m = max(m, a[i] + a[i + 1])
print(k, m)