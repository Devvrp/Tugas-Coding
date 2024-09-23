def buat_matriks(baris, kolom):
    matriks = []
    for i in range(baris):
        baris_matriks = []
        for j in range(kolom):
            nilai = float(input(f"Masukkan nilai untuk matriks[{i}][{j}]: "))
            baris_matriks.append(nilai)
        matriks.append(baris_matriks)
    return matriks

def tampilkan_matriks(matriks):
    for baris in matriks:
        print(" | ".join(map(str, baris)))

def perkalian_matriks(matriks_a, matriks_b):
    baris_a = len(matriks_a)
    kolom_a = len(matriks_a[0])
    baris_b = len(matriks_b)
    kolom_b = len(matriks_b[0])
    
    if kolom_a != baris_b:
        print("Perkalian tidak dapat dilakukan. Kolom matriks A harus sama dengan baris matriks B.")
        return None

    hasil = [[0] * kolom_b for _ in range(baris_a)]

    for i in range(baris_a):
        for j in range(kolom_b):
            for k in range(kolom_a):
                hasil[i][j] += matriks_a[i][k] * matriks_b[k][j]
    
    return hasil

def main():
    print("Matriks A:")
    baris_a = int(input("Masukkan jumlah baris matriks A: "))
    kolom_a = int(input("Masukkan jumlah kolom matriks A: "))
    matriks_a = buat_matriks(baris_a, kolom_a)

    print("\nMatriks B:")
    baris_b = int(input("Masukkan jumlah baris matriks B: "))
    kolom_b = int(input("Masukkan jumlah kolom matriks B: "))
    matriks_b = buat_matriks(baris_b, kolom_b)

    hasil_perkalian = perkalian_matriks(matriks_a, matriks_b)

    if hasil_perkalian is not None:
        print("\nHasil Perkalian Matriks:")
        tampilkan_matriks(hasil_perkalian)

if __name__ == "__main__":
    main()
