c = float(input("Masukkan nilai suhu :"))
konv = input ("Masukkan jenis konversi K/F/R atau k/f/r :")

if (konv == "K") or (konv == "k") :
    print (f"{c} °C dalan {konv} menjadi {c + 273:.2f} °K")

elif (konv == "F") or (konv == "f") :
    print (f"{c} °C dalam {konv} menjadi {9/5 * c + 32:.2f} °F")

elif (konv == "R") or (konv == "r") :
    print (f"{c} °C dalam {konv} menjadi {c * 4/5:.2f} °R")

else :
    print ("Jenis konversi tidak terdefinisi")