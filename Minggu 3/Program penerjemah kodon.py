protein_translation = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine',
    'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
    'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'UGU': 'Cysteine', 'UGC': 'Cysteine',
    'UGG': 'Tryptophan'
}

kodon = input("Masukkan kodon RNA: ").upper()

if kodon in protein_translation:
    protein = protein_translation[kodon]
    print(f"Kodon {kodon} menghasilkan protein: {protein}")
else:
    print(f"Kodon {kodon} tidak dikenali.")
