protein_translation = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan"
}

def translate_codon(codon):
    return protein_translation.get(codon, "Kodon tidak dikenal")

input_codon = input("Masukkan kodon (3 huruf, seperti 'AUG'): ").upper()

protein = translate_codon(input_codon)
print(f"Kodon {input_codon} menghasilkan protein: {protein}")
