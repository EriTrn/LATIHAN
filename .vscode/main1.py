# LAtihan perulangan membuat segitiga

sisi = 5
# 1. Menggunakan For

# dummy variable
print("awal for")
count = 1 
for i in range(sisi*2):
    print("*"*(sisi*2))
    count += 1

print("akhir dari for")
# 2. Menggunakan while

print("awal while")    
count = 1
while count <= (sisi*2):
    print("*"*(sisi*2))
    count += 1

    if count > sisi*2:
        break

print("akhir dari While")

# 3. hanya ganjil saja

print("awal dari while")
count = 1
while True:
spasi = int(sisi2)
    if (count%2):
        # prin jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan print jika genap
    print("*"*count)
    count += 1

    #akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir dari while")
