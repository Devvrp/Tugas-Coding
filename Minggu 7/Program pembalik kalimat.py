def hitung_vokal(kalimat):
    vokal = "aeiouAEIOU"
    jumlah_vokal = sum(1 for char in kalimat if char in vokal)
    return jumlah_vokal

def main():
    kalimat = input("Masukkan kalimat: ")

    kalimat_balik = kalimat[::-1]

    jumlah_vokal = hitung_vokal(kalimat)

    print(f"Kalimat setelah dibalik: {kalimat_balik}")
    print(f"Jumlah huruf vokal: {jumlah_vokal}")

if __name__ == "__main__":
    main()
