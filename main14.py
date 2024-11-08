# Pola Bangun Datar

# 1. Persegi
size = 5
for i in range(size):
    print('* ' * size)

# 2. Persegi dengan garis tepi
size = 5
for i in range(size):
    if i == 0 or i == size - 1:
        print('* ' * size)
    else:
        print('* ' + '  ' * (size - 2) + '*')

# 3. Persegi Panjang
width = 7
height = 4
for i in range(height):
    print('* ' * width)

# 4. Segitiga sama kaki
size = 5
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * i)

# 5. Segitiga siku-siku
size = 5
for i in range(1, size + 1):
    print('* ' * i)

# 6. Segitiga siku-siku terbalik
size = 5
for i in range(size, 0, -1):
    print('* ' * i)

# 7. Segitiga sama kaki terbalik
size = 5
for i in range(size, 0, -1):
    print(' ' * (size - i) + '* ' * i)

# 8. Segitiga siku -siku berlubang
size = 5
for i in range(1, size + 1):
    if i == 1 or i == size:
        print('* ' * i)
    else:
        print('* ' + '  ' * (i - 2) + '*')

# 9. Segitiga siku -siku berlubang terbalik
size = 5
for i in range(size, 0, -1):
    if i == size or i == 1:
        print('* ' * i)
    else:
        print('* ' + '  ' * (i - 2) + '*')

# 10. Belah ketupat
size = 5
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * i)
for i in range(size - 1, 0, -1):
    print(' ' * (size - i) + '* ' * i)

# 11. Belah ketupat berlubang
size = 5
for i in range(1, size + 1):
    if i == 1:
        print(' ' * (size - i) + '*')
    else:
        print(' ' * (size - i) + '*' + ' ' * (2 * i - 3) + '*')
for i in range(size - 1, 0, -1):
    if i == 1:
        print(' ' * (size - i) + '*')
    else:
        print(' ' * (size - i) + '*' + ' ' * (2 * i - 3) + '*')

# 12. Panah(atas)
size = 5
for i in range(1, size + 1):
    print(' ' * (size - i) + '* ' * i)
for i in range(2, size + 1):
    print(' ' * (size - 1) + '*')

# 13. Panah(bawah)
size = 5
for i in range(size):
    print(' ' * (size - 1) + '*')
for i in range(size, 0, -1):
    print(' ' * (size - i) + '* ' * i)

# 14. X atau silang
size = 5
for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# 15. Huruf H
size = 5
for i in range(size):
    for j in range(size):
        if j == 0 or j == size - 1 or i == size // 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# 16. Plus(+)
size = 5
for i in range(size):
    for j in range(size):
        if i == size // 2 or j == size // 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# 17. X dalam kotak
size = 7
for i in range(size):
    for j in range(size):
        if i in {0, size - 1} or j in {0, size - 1} or i == j or i + j == size - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# 18. Kotak berpola
size = 7
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

# 19. Segitiga sama kaki dengan garis tepi
size = 5
for i in range(1, size + 1):
    if i == 1 or i == size:
        print(' ' * (size - i) + '* ' * i)
    else:
        print(' ' * (size - i) + '*' + ' ' * (2 * i - 3) + '*')

# 20. Garis diagonal(miring ke kiri)
size = 5
for i in range(size):
    for j in range(size):
        if i == j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
