def translasi_rna(rna):
    kodon_protein = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    polipeptida = []

    for i in range(0, len(rna), 3):
        kodon = rna[i:i+3]
        if kodon in kodon_protein:
            if kodon_protein[kodon] == "STOP":
                break
            polipeptida.append(kodon_protein[kodon])
        else:
            print(f"Kodon {kodon} tidak dikenal.")
    
    return polipeptida

def main():
    rna_input = input("Masukkan urutan RNA (contoh: AUGUUUUCU): ").strip()
    polipeptida = translasi_rna(rna_input)

    if polipeptida:
        print("Protein yang dihasilkan:", ", ".join(polipeptida))

if __name__ == "__main__":
    main()
