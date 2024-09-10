import math

def hitung_akar(a, b, c):
    D = b**2 - 4*a*c

    if D < 0:
        real_part = -b / (2*a)
        imag_part = math.sqrt(abs(D)) / (2*a)
        print(f"Akar-akar imajinernya adalah: {real_part} ± {imag_part}i")

    elif D == 0:
        x = -b / (2*a)
        print(f"Akar-akarnya sama dan bernilai: x1 = x2 = {x}")
    
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Akar-akarnya adalah: x1 = {x1}, x2 = {x2}")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

hitung_akar(a, b, c)
