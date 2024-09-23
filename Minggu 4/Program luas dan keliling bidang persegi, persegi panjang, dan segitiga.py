def luas_keliling_persegi(sisi):
    luas = sisi ** 2
    keliling = 4 * sisi
    return luas, keliling

def luas_keliling_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def luas_keliling_segitiga(alas, tinggi, sisi1, sisi2):
    luas = 0.5 * alas * tinggi
    keliling = alas + sisi1 + sisi2
    return luas, keliling

while True:
    print("\nMenu:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas, keliling = luas_keliling_persegi(sisi)
        print(f"Luas Persegi: {luas}")
        print(f"Keliling Persegi: {keliling}")

    elif pilihan == '2':
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas, keliling = luas_keliling_persegi_panjang(panjang, lebar)
        print(f"Luas Persegi Panjang: {luas}")
        print(f"Keliling Persegi Panjang: {keliling}")

    elif pilihan == '3':
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        sisi1 = float(input("Masukkan panjang sisi 1 segitiga: "))
        sisi2 = float(input("Masukkan panjang sisi 2 segitiga: "))
        luas, keliling = luas_keliling_segitiga(alas, tinggi, sisi1, sisi2)
        print(f"Luas Segitiga: {luas}")
        print(f"Keliling Segitiga: {keliling}")

    elif pilihan == '4':
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
