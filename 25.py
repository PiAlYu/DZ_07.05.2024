from fnmatch import fnmatch

for i in range(123450706, 10 ** 9 + 1, 23):
    if fnmatch(str(i), '12345?7?8'):
        print(i, i // 23)