def hitung_faktorial(n):
    faktorial = 1
    penjabaran = []
    
    for i in range(n, 0, -1):
        faktorial *= i
        penjabaran.append(str(i))
    
    return faktorial, " x ".join(penjabaran)

angka = int(input("Masukkan angka: "))
faktorial, penjabaran = hitung_faktorial(angka)

print(f"{angka}! = {penjabaran} = {faktorial}")