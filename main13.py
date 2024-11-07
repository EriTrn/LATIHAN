# Membuat contoh penggunaan fungsi

# 1. Fungsi untuk menghitung luas dan keliling persegi
def hitung_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

sisi = 5
luas, keliling = hitung_persegi(sisi)
print("Luas persegi:", luas)
print("Keliling persegi:", keliling)

# 2. Fungsi untuk menghitung luas dan keliling lingkaran
def hitung_lingkaran(jari_jari):
    luas = 3.14 * jari_jari * jari_jari
    keliling = 2 * 3.14 * jari_jari
    return luas, keliling

jari_jari = 7
luas, keliling = hitung_lingkaran(jari_jari)
print("Luas lingkaran:", luas)
print("Keliling lingkaran:", keliling)

# 3. Fungsi untuk menghitung faktorial
def hitung_faktorial(n):
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i
    return faktorial

n = 5
faktorial = hitung_faktorial(n)
print("Faktorial dari", n, "adalah", faktorial)

# 4. Fungsi menghitung bilangan prima
def bilangan_prima(n):
    prima = True
    for i in range(2, n):
        if n % i == 0:
            prima = False
            break
    return prima


print("Apakah", n, "adalah bilangan prima?", bilangan_prima(3))

# 5. Fungsi untuk menemukan nilai maksimum dan minimum dalam list
def max_min(numbers):
    return max(numbers), min(numbers)

numbers = [1, 2, 3, 4, 5]
max_value, min_value = max_min(numbers)
print("Nilai maksimum:", max_value)
print("Nilai minimum:", min_value)

# 6. Fungsi untuk mengonversi suhu Celcius ke Fahrenheit
def celcius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f

c = 25
f = celcius_to_fahrenheit(c)
print("Suhu dalam Fahrenheit:", f)

# 7. Fungsi untuk mengonversi suhu Celsius ke Reamur
def celcius_to_reamur(c):
    r = c * 4 / 5
    return r

c = 25
r = celcius_to_reamur(c)
print("Suhu dalam Reamur:", r) 

# 8. Fungsi untuk mengonversi suhu Celsius ke Kelvin
def celcius_to_kelvin(c):
    k = c + 273.15
    return k    

c = 25
k = celcius_to_kelvin(c)
print("Suhu dalam Kelvin:", k)

# 9. Fungsi untuk mengonversi suhu Fahrenheit ke Kelvin
def fahrenheit_to_kelvin(f):
    k = (f + 459.67) * 5 / 9
    return k

f = 77
k = fahrenheit_to_kelvin(f)
print("Suhu dalam Kelvin:", k)

# 10. Fungsi untuk mengonversi suhu Reamur ke Kelvin
def reamur_to_kelvin(r):
    k = r * 5 / 4 + 273.15
    return k    

r = 25
k = reamur_to_kelvin(r)
print("Suhu dalam Kelvin:", k)     

# 11. Fungsi untuk mengonversi suhu Reamur ke Fahrenheit
def reamur_to_fahrenheit(r):
    f = r * 4 / 5 * 9 + 32
    return f

r = 25
f = reamur_to_fahrenheit(r)
print("Suhu dalam Fahrenheit:", f)