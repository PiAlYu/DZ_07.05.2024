fin = open('26_59821.txt')
a = fin.readlines()
fin.close()
n = int(a.pop(0))
a = [list(map(int, i.split())) for i in a]
start, finish, k = [], [], 1
for i in a:
    if i[0] < i[1]:
        start.append([i[0], k])
    else:
        finish.append([i[1], k])
    k += 1
start.sort(); finish.sort()
if finish[-1][0] > start[-1][0]: last = finish[-1][1]
else: last = start[-1][1]
print(last, len([i[0] for i in start if i[0] < finish[-1][0]]))