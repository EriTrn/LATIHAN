import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Menghitung Luas Persegi Panjang
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2*(panjang + lebar)
    return luas, keliling

panjang = int(input("Masukan angka pertama disini: "))
lebar = int(input("Masukan angka kedua disini: "))

luas, keliling = hitung_persegi_panjang(panjang, lebar)

# Tampilan
fig, ax = plt.subplots()
persegi = patches.Rectangle((0, 0), panjang, lebar, linewidth=2, edgecolor='blue', facecolor='lightblue')
ax.add_patch(persegi)

ax.text(panjang / 2, lebar + 0.5, f'Panjang = {panjang}, Lebar = {lebar}', ha='center', fontsize=12)
ax.text(panjang / 2, -1, f'Luas = {luas}', ha='center', fontsize=12)
ax.text(panjang / 2, -2, f'Keliling = {keliling}', ha='center', fontsize=12)

plt.xlim(-2, panjang + 2)
plt.ylim(-3, lebar + 2)
ax.set_aspect('equal')
plt.gca().set_axis_off()
plt.title("Visualisasi Persegi panjang")
plt.show()
