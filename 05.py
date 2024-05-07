for n in range(100, 1000):
    r = str(n)
    r = [int(r[0]) * int(r[1]), int(r[1]) * int(r[2])]
    r = str(min(r)) + str(max(r))
    if r == '621':
        print(n)
        break