def cetak_bilangan_ganjil(n):
    print(f"Bilangan ganjil dari {n} sampai 1 adalah: ")
    for i in range(n, 0, -1):
        if i % 2 != 0:
            print(i, end=" ")

N = int(input("Masukkan bilangan bulat N: "))

if N > 0:
    cetak_bilangan_ganjil(N)
else:
    print("Masukkan bilangan bulat positif.")