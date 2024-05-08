fin = open('24.txt')
a = fin.readline()
fin.close()
indx, indy, m = [0, 0], [0, 0], 0
for i in range(len(a)):
    if a[i] == 'X':
        m = max(m, i - max(indx[1], indy[0]))
        indx[0] = indx[1]
        indx[1] = i
    elif a[i] == 'Y':
        m = max(m, i - max(indx[0], indy[1]))
        indy[0] = indy[1]
        indy[1] = i
print(m)