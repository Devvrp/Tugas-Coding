def verifikasi_isbn(isbn):

    isbn = isbn.replace("-", "").replace(" ", "")

    if len(isbn) != 10:
        return False
    
    total = 0
    
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (10 - i)

    if isbn[9] == 'X':
        total += 10
    elif isbn[9].isdigit():
        total += int(isbn[9]) * 1
    else:
        return False

    return total % 11 == 0

def main():
    isbn_input = input("Masukkan kode ISBN-10: ")
    
    if verifikasi_isbn(isbn_input):
        print("ISBN-10 valid.")
    else:
        print("ISBN-10 tidak valid.")

if __name__ == "__main__":
    main()