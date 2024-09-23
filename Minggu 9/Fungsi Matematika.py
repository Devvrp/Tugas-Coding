def fungsi_matematika(x):
    return 6 * (x ** 2) + 3 * x + 2

def main():
    print("Nilai y untuk x dari -10 hingga 10:")
    for x in range(-10, 11):
        y = fungsi_matematika(x)
        print(f"x = {x}, y = {y}")

if __name__ == "__main__":
    main()