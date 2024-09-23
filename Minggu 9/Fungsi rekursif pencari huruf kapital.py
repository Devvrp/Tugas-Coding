def kapital_pertama(s, i):
    if i >= len(s):
        return None

    if s[i].isupper():
        return s[i]

    return kapital_pertama(s, i + 1)

def main():
    s = input("Masukkan string: ")
    hasil = kapital_pertama(s, 0)
    
    if hasil:
        print(f"Huruf kapital pertama: {hasil}")
    else:
        print("Tidak ada huruf kapital dalam string.")

if __name__ == "__main__":
    main()