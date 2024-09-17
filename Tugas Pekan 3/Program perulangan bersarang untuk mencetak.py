def pola_a(n):
    print("Pola a:")
    for i in range(n, 0, -1):
        print('x' * i)

def pola_b(n):
    print("Pola b:")
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print('-' * i)
        else:
            print('x' * i)

def pola_c(n):
    print("Pola c:")
    # Mencetak pola naik
    for i in range(1, n + 1):
        print(''.join(str(j) for j in range(1, i + 1)))
    # Mencetak pola turun
    for i in range(n - 1, 0, -1):
        print(''.join(str(j) for j in range(1, i + 1)))

def pola_d(n):
    print("Pola d:")
    # Mencetak pola naik
    for i in range(1, n + 1):
        print('x' * i)
    # Mencetak pola turun
    for i in range(n - 1, 0, -1):
        print('x' * i)

def pola_e(n):
    print("Pola e:")
    for i in range(n, 0, -1):
        print('. ' * (n - i) + ' '.join(str(j) for j in range(1, i + 1)))

def main():
    try:
        n = int(input("Masukkan nilai N: "))
        if n <= 0:
            print("N harus bilangan bulat positif.")
            return
        
        pola_a(n)
        print()
        pola_b(n)
        print()
        pola_c(n)
        print()
        pola_d(n)
        print()
        pola_e(n)
    except ValueError:
        print("Masukkan nilai yang valid.")

if __name__ == "__main__":
    main()
