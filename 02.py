print('         x y z w f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (z == (not(x))) <= ((w <= (not(y))) and (y <= x))
                s = x + y + z + w
                if f == 1 and s == 3:
                    print('1 строка', x, y, z, w, f)
                if f == 0 and s <= 2:
                    print('2 строка', x, y, z, w, f)
                elif f == 0 and s <= 3:
                    print('3 строка', x, y, z, w, f)
