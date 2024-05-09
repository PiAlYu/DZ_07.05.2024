fin = open('24.txt')
a = fin.readline()
fin.close()
indx, indy, m = [-1, -1], [-1, -1], 0
for i in range(len(a)):
    if a[i] == 'X':
        indx[0], indx[1] = indx[1], i
    elif a[i] == 'Y':
        indy[0], indy[1] = indy[1], i
    m = max(m, i - max(indx[0], indy[0]))
print(m)