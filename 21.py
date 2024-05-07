def game(i, h):
    if i >= 39 and str(h) in '35':
        return 1
    if (i < 39 and h == 5) or (i >= 39 and str(h) in '24'):
        return 0
    if h % 2 == 0:
        return game(i + 1, h + 1) or game(i * 3, h + 1)
    return game(i + 1, h + 1) and game(i * 3, h + 1)

for i in range(1, 39):
    if game(i, 1):
        print(i)