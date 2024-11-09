# Contoh perulangan 'for'

# 1. Perulangan 'for' sederhana
for i in range(5):
    print(i)

# 2. Perulangan dengan Daftar (List)
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# 3. Perulangan dengan String
name = "Eri"
for char in name:
    print(char)

# 4. Perulangan dengan Fungsi range (Langkah Terbatas)
for i in range(1, 6, 2):
    print(i)

# 5. Perulangan untuk Mengakses Indeks dan Elemen dalam List dengan enumerate
fruits = ["apel", "pisang", "semangka"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 6. Perulangan dengan Menggunakan Fungsi zip (Multiple Lists)
names = ["Eri", "Dede", "Habib"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, "berumur", age, "tahun")

# 7. Perulangan dengan Operasi Matematis
numbers = [1, 2, 3, 4]
for num in numbers:
    square = num ** 2
    print(f'Kuadrat dari {num} adalah {square}')

# 8. Perulangan dengan Dictionary
person = {"name": "Eri", "age": 25, "city": "Bandung"}
for key, value in person.items():
    print(key, ":", value)

# 9. Perulangan untuk Membalik List
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)

# 10. Perulangan dengan List Comprehension
squares = [num ** 2 for num in range(1, 6)]
print(squares)