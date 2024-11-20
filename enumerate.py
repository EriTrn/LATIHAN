# 1. Menggunakan enumerate untuk mencetak indeks dan nilai dari sebuah daftar

fruits = ["apel", "pisang", "semangka"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 2. Mengatur awal indeks menggunakan parameter start
fruits = ["apel", "pisang", "semangka"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# 3. Menggunakan enumerate dengan tuple
points = [(1, 2), (3, 4), (5, 6)]
for index, point in enumerate(points):
    print(f"Index {index}: {point}")

# 4. Menggunakan enumerate untuk membuat daftar indeks
items = ["a", "b", "c"]
indices = [i for i, _ in enumerate(items)]
print(indices)

# 5. Mencetak daftar menggunakan indeks dan nilai
items = ["x", "y", "z"]
for index, item in enumerate(items):
    print(f"Item {index} adalah {item}")

# 6. Mengubah elemen daftar berdasarkan indeks
numbers = [10, 20, 30]
for index, num in enumerate(numbers):
    numbers[index] = num * 2
print(numbers)

# 7. Menggabungkan enumerate dengan kondisi
fruits = ["apel", "pisang", "semangka", "data"]
for index, word in enumerate(fruits):
    if len(word) > 5:
        print(f"Index {index}: {word}")

# 8. Menggunakan enumerate untuk menambah elemen ke dictionary
fruits = ["apel", "pisang", "semangka"]
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
print(fruit_dict)

# 9. Menggunakan enumerate dengan file input/output
with open("example.txt", "r") as file:
    for line_no, line in enumerate(file, start=1):
        print(f"Line {line_no}: {line.strip()}")

# 10. Menggunakan enumerate untuk melacak indeks elemen yang cocok
nums = [1, 3, 5, 7, 9]
for index, num in enumerate(nums):
    if num > 5:
        print(f"Number {num} found at index {index}")