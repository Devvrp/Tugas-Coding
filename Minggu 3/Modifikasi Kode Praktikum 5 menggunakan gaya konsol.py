import random, sys

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"

print(CYAN + ".:: Permainan Suit/Pingsut ::." + RESET)
print(GREEN + "1. Jempol (Gajah)")
print("2. Telunjuk (Manusia)")
print("3. Kelingking (Semut)" + RESET)

pil = int(input(YELLOW + "Pilihan anda ? " + RESET))
if(pil < 1 or pil > 3):
    sys.exit(RED + "Masukkan pilihan yang benar!! Pilihan antara 1 - 3." + RESET)

kom = random.randint(1, 3)

if kom == 1:
    if pil == 1:
        print(BLUE + "Sama-sama Gajah! sesama gajah saling membantu..." + RESET)
    elif pil == 2:
        print(RED + "Diinjek gajah.. kamu kalah!" + RESET)
    elif pil == 3:
        print(GREEN + "Kamu gigit gajah, kamu menang!" + RESET)
elif kom == 2: 
    if pil == 1:
        print(GREEN + "Kamu abis nginjek manusia, kamu menang!" + RESET)
    elif pil == 2:
        print(BLUE + "Sama-sama Manusia! Jangan berantem lah..." + RESET)
    elif pil == 3:
        print(RED + "Kamu dibunuh manusia, kamu kalah!" + RESET)
elif kom == 3:
    if pil == 1:
        print(RED + "Kamu abis dikerjain sama semut, kamu kalah!" + RESET)
    elif pil == 2:
        print(GREEN + "Kamu gak sengaja injek semut, kamu menang!" + RESET)
    elif pil == 3:
        print(BLUE + "Sesama semut saling membahu..!" + RESET)
