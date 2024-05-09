def f(l):
    k = 0
    for i in l:
        if l.count(i) >= 2:
            k += 1
    return k == 4

def f1(l):
    k = []
    for i in l:
        if l.count(i) >= 2:
            k.append(i)
    return sum(k) < ((sum(l) - sum(k)) / 3)

fin = open('09.csv')
a = fin.readlines()
fin.close()
a = [list(map(int, i.split(';'))) for i in a]
c = 0
for i in a:
    if f(i) and f1(i):
        c += 1
print(c)