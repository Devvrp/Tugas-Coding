def hitung_deret_harmonik(N):
    # Menghitung deret harmonik dan menyimpan tiap bagian deret dalam list
    deret = [1 / i for i in range(1, N + 1)]
    # Menjumlahkan semua bagian deret untuk mendapatkan hasil akhir
    total = sum(deret)
    # Membuat string deret harmonik
    deret_str = " + ".join(f"(1/{i})" for i in range(1, N + 1))
    return deret_str, total

def main():
    # Mengambil input dari pengguna
    try:
        N = int(input("Masukkan nilai N: "))
        if N <= 0:
            print("N harus bilangan bulat positif.")
            return
        
        # Menghitung deret harmonik
        deret_str, total = hitung_deret_harmonik(N)
        
        # Mencetak hasil
        print(f"{deret_str} = {total:.9f}")
    except ValueError:
        print("Masukkan nilai yang valid.")

if __name__ == "__main__":
    main()
