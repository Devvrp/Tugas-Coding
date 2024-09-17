def hitung_cicilan_per_tahun(harga_rumah, harga_klien, tahun):
    # Menghitung jumlah pinjaman
    pinjaman = harga_klien - harga_rumah
    
    # Jika pinjaman kurang dari atau sama dengan 0
    if pinjaman <= 0:
        return 0

    # Cicilan per tahun tanpa bunga
    cicilan_per_tahun = pinjaman / tahun
    return cicilan_per_tahun

def main():
    try:
        # Mengambil input dari pengguna
        harga_rumah = float(input("Masukkan harga rumah asal (Rp.): "))
        harga_klien = float(input("Masukkan harga rumah yang dijual ke klien (Rp.): "))
        
        # Skema waktu cicilan
        skema_tahun = [20, 15, 10, 5]

        print("\nCicilan per tahun untuk setiap skema:")
        for tahun in skema_tahun:
            cicilan = hitung_cicilan_per_tahun(harga_rumah, harga_klien, tahun)
            print(f"{tahun} tahun: Rp. {cicilan:,.2f}")
    except ValueError:
        print("Masukkan nilai yang valid.")

if __name__ == "__main__":
    main()
