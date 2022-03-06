# kalkulator sederhana 

from turtle import goto


angka_1 = float(input("Masukkan angka pertama : "))
ope = input("masukkan [+ , - , * , /]: ")
angka_2 = float(input("Masukkan angka kedua   : "))

if ope == "+" :
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah : {hasil}")
elif ope == "-" :
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah : {hasil}")
elif ope == "*" or ope == "x" :
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah : {hasil}")
elif ope == "/" or ope == ":" :
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah : {hasil}")
else:
    print("Yang batua masuak ann pakak!!!")

print("Akhir program")