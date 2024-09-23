def ekstrak_string(input_str):
    huruf = ""
    angka = ""
    simbol = ""
    
    for char in input_str:
        if char.isalpha():
            huruf += char
        elif char.isdigit():
            angka += char
        else:
            simbol += char

    angka = int(angka) if angka else 0

    return [huruf, angka, simbol]

def main():
    input_str = input("Masukkan string: ")
    hasil = ekstrak_string(input_str)
    print(hasil)

if __name__ == "__main__":
    main()
