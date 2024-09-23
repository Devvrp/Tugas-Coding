def hitung_aritmatika(pertanyaan):
    pertanyaan = pertanyaan.lower().replace("berapa", "").strip()

    parts = pertanyaan.split()
    
    if len(parts) != 5:
        return "Pertanyaan tidak valid."

    angka1 = float(parts[0])
    operator = parts[1]
    angka2 = float(parts[3])

    if operator == "ditambah":
        return angka1 + angka2
    elif operator == "dikurangi":
        return angka1 - angka2
    elif operator == "dikali":
        return angka1 * angka2
    elif operator == "dibagi":
        if angka2 != 0:
            return angka1 / angka2
        else:
            return "Pembagian dengan nol tidak valid."
    else:
        return "Operator tidak dikenali."

def main():
    while True:
        pertanyaan = input("Masukkan pertanyaan aritmatika (atau 'selesai' untuk keluar): ")
        
        if pertanyaan.lower() == 'selesai':
            print("--program berhenti--")
            break
        
        hasil = hitung_aritmatika(pertanyaan)
        print(f"-> {hasil}")

if __name__ == "__main__":
    main()