import math

def luas_permukaan_tabung(jari_jari, tinggi):
    luas = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return luas

jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

luas = luas_permukaan_tabung(jari_jari, tinggi)

print(f"Luas permukaan tabung adalah: {luas:.2f}")
