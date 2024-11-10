# Perulangan While

# 1. Perulangan 'while' sederhana
i = 0
while i < 5:
    print(i)
    i += 1

# 2. Perulangan while dengan Kondisi Berdasarkan Input Pengguna
user_input = ""
while user_input.lower() != "stop":
    user_input = input("Ketik sesuatu (atau ketik 'stop' untuk berhenti): ")
    print(f'Anda mengetik: {user_input}')

# 3. Perulangan while dengan break
number = 0
while True:
    if number == 5:
        break
    print(number)
    number += 1

# 4. Perulangan while dengan continue
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)

# 5. Perulangan while untuk Menghitung Jumlah dari List
numbers = [10, 20, 30, 40]
index = 0
total = 0
while index < len(numbers):
    total += numbers[index]
    index += 1
print(f'Total: {total}')

#6. Perulangan while Menggunakan Kondisi Boolean
keep_running = True
counter = 0
while keep_running:
    print(f'Iterasi ke-{counter}')
    counter += 1
    if counter >= 3:
        keep_running = False

# 7. Perulangan while untuk Mencari Elemen dalam List
numbers = [1, 2, 3, 4, 5]
target = 4
index = 0
while index < len(numbers):
    if numbers[index] == target:
        print(f'Elemen {target} ditemukan di indeks {index}')
        break
    index += 1

# 8. Perulangan while dengan Pengurangan Nilai
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1

# 9. Perulangan while untuk Membalik List
numbers = [1, 2, 3, 4, 5]
reversed_numbers = []
index = len(numbers) - 1
while index >= 0:
    reversed_numbers.append(numbers[index])
    index -= 1
print(reversed_numbers)

# 10. Perulangan while untuk Menemukan Faktor dari Sebuah Angka
number = 12
factor = 1
factors = []
while factor <= number:
    if number % factor == 0:
        factors.append(factor)
    factor += 1
print(factors)