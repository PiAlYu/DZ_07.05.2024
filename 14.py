def f(n):
    k = 0
    while n > 0:
        if n % 3 == 2:
            k += 1
        n = n // 3
    return k

print(f(9 ** 12 + 3 ** 8 - 3))