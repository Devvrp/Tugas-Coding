def cetak_ganjil(n):
    if n % 2 == 0:
        n -= 1
    
    for i in range(n, 0, -2):
        print(i, end=" ")

N = int(input("Masukkan bilangan bulat N: "))

cetak_ganjil(N)