# generate number fibonacci
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


print(fibonacci(20))

# menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
alas = 10
tinggi = 5
print(luas_segitiga(alas, tinggi))

# menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari
jari_jari = 7
print(luas_lingkaran(jari_jari))

# menghitung luas belah ketupat
def luas_belakang_ketupat(diagonal_1, diagonal_2):
    return 0.5 * diagonal_1 * diagonal_2
diagonal_1 = 10
diagonal_2 = 5  
print(luas_belakang_ketupat(diagonal_1, diagonal_2))

# menghitung luas persegi
def luas_persegi(sisi): 
    return sisi * sisi
sisi = 5            
print(luas_persegi(sisi))  

# menghitung luas jajar genjang
def luas_jajar_genjang(panjang, lebar):
    return panjang * lebar
panjang = 10
lebar = 5
print(luas_jajar_genjang(panjang, lebar))

# menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar
panjang = 10    
lebar = 5
print(luas_persegi_panjang(panjang, lebar))

# menghitung luas trapesium
def luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    return 0.5 * (sisi_atas + sisi_bawah) * tinggi
sisi_atas = 10
sisi_bawah = 5
tinggi = 5
print(luas_trapesium(sisi_atas, sisi_bawah, tinggi))