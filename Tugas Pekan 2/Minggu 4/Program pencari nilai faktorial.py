def faktorial(n):
    hasil = 1
    penjabaran = f"{n}! = " 
    for i in range(n, 0, -1):
        hasil *= i
        penjabaran += f"{i} x " if i != 1 else f"{i} = "
    penjabaran += str(hasil)
    print(penjabaran)

N = int(input("Masukkan angka: "))
faktorial(N)