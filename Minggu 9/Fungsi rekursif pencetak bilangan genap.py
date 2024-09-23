def jumlah_genap(a, b):
    if a > b:
        return 0
    if a % 2 == 0:
        return a + jumlah_genap(a + 1, b)
    else:
        return jumlah_genap(a + 1, b)

def main():
    a = int(input("Masukkan nilai a: "))
    b = int(input("Masukkan nilai b: "))
    
    hasil = jumlah_genap(a, b)
    print(f"Jumlah bilangan genap dari {a} sampai {b} adalah {hasil}.")

if __name__ == "__main__":
    main()