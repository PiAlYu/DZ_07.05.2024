fin = open('17.txt')
a = fin.readlines()
fin.close()
a = [int(i) for i in a]
k, m = 0, 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 10 == 0:
            k += 1
            m = max(m, a[i] + a[j])
print(k, m)