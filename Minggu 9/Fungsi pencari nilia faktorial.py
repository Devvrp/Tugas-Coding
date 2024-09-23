def hitung_faktorial(n):
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif."
    elif n == 0:
        return "0! = 1"
    
    faktorial = 1
    penjabaran = []
    
    for i in range(n, 0, -1):
        faktorial *= i
        penjabaran.append(str(i))
    
    return f"{n}! = {' x '.join(penjabaran)} = {faktorial}"

def main():
    angka = int(input("Masukkan angka untuk menghitung faktorial: "))
    hasil = hitung_faktorial(angka)
    print(hasil)

if __name__ == "__main__":
    main()