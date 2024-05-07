from itertools import product

k = 0
for i in product('ЖИРАФ', repeat=4):
    s = ''.join(i)
    if s.count('Р') == 1:
        k += 1
print(k)