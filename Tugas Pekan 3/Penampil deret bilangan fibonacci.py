def fibonacci(n):
    # Menghasilkan deret Fibonacci hingga suku ke-n
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(b)
        a, b = b, a + b
    return sequence

def main():
    # Mengambil input dari pengguna
    try:
        N = int(input("Masukkan nilai N: "))
        if N <= 0:
            print("N harus bilangan bulat positif.")
            return
        
        # Menghitung deret Fibonacci
        fib_sequence = fibonacci(N)
        
        # Mencetak hasil dengan format yang diinginkan
        print(", ".join(map(str, fib_sequence)))
    except ValueError:
        print("Masukkan nilai yang valid.")

if __name__ == "__main__":
    main()
