def buat_matriks(baris, kolom):
    matriks = []
    for i in range(baris):
        baris_matriks = []
        for j in range(kolom):
            nilai = input(f"Masukkan nilai untuk matriks[{i}][{j}]: ")
            baris_matriks.append(nilai)
        matriks.append(baris_matriks)
    return matriks

def tampilkan_matriks(matriks):
    for baris in matriks:
        print(" | ".join(baris))

def ubah_nilai_matriks(matriks):
    baris = int(input("Masukkan indeks baris yang ingin diubah: "))
    kolom = int(input("Masukkan indeks kolom yang ingin diubah: "))
    if 0 <= baris < len(matriks) and 0 <= kolom < len(matriks[0]):
        nilai_baru = input("Masukkan nilai baru: ")
        matriks[baris][kolom] = nilai_baru
    else:
        print("Indeks di luar jangkauan matriks.")

def main():
    matriks = []
    while True:
        print("\nMenu:")
        print("1. Buat Matriks")
        print("2. Tampilkan Matriks")
        print("3. Ubah Nilai Matriks")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            baris = int(input("Masukkan jumlah baris: "))
            kolom = int(input("Masukkan jumlah kolom: "))
            matriks = buat_matriks(baris, kolom)

        elif pilihan == '2':
            if matriks:
                print("Matriks saat ini:")
                tampilkan_matriks(matriks)
            else:
                print("Matriks masih kosong.")

        elif pilihan == '3':
            if matriks:
                ubah_nilai_matriks(matriks)
            else:
                print("Matriks masih kosong.")

        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
