import math

def hitung_akar(a, b, c):
    D = b**2 - 4*a*c
    print(f"Diskriminan (D) = {D}")
    
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Akar-akarnya adalah x1 = {x1:.2f} dan x2 = {x2:.2f}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Akar-akarnya sama, x1 = x2 = {x:.2f}")
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(abs(D)) / (2 * a)
        print(f"Akar-akarnya imajiner: x1 = {real_part:.2f} + {imag_part:.2f}i dan x2 = {real_part:.2f} - {imag_part:.2f}i")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

if a == 0:
    print("Nilai a tidak boleh 0, karena bukan persamaan kuadrat.")
else:
    hitung_akar(a, b, c)
