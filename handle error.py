#menghandle error menggunakan try dan except


try:
    angka = int(input("masukkan angka : "))
    print(angka)
except ValueError:
    print("your input a string, please input integer")