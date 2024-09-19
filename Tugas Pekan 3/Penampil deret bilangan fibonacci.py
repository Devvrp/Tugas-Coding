def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(b)
        a, b = b, a + b
    return sequence

def main():
    try:
        N = int(input("Masukkan nilai N: "))
        if N <= 0:
            print("N harus bilangan bulat positif.")
            return
        fib_sequence = fibonacci(N)
        print(", ".join(map(str, fib_sequence)))
    except ValueError:
        print("Masukkan nilai yang valid.")

if __name__ == "__main__":
    main()
