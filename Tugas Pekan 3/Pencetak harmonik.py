def hitung_deret_harmonik(N):
    deret = [1 / i for i in range(1, N + 1)]
    total = sum(deret)
    deret_str = " + ".join(f"(1/{i})" for i in range(1, N + 1))
    return deret_str, total

def main():
    try:
        N = int(input("Masukkan nilai N: "))
        if N <= 0:
            print("N harus bilangan bulat positif.")
            return
        deret_str, total = hitung_deret_harmonik(N)
        
        print(f"{deret_str} = {total:.9f}")
    except ValueError:
        print("Masukkan nilai yang valid.")

if __name__ == "__main__":
    main()
