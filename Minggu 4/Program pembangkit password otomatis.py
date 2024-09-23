import random
import string

def generate_password(length):
    if length < 1:
        return "Panjang password harus lebih dari 0."

    karakter = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(karakter) for _ in range(length))
    
    return password

panjang = int(input("Masukkan panjang password yang diinginkan: "))
password = generate_password(panjang)

print(f"Password yang dihasilkan: {password}")