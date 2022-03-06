#Assigment adalah operasi yang dapat dilakukan dengan penyingkatan
from msilib.schema import Binary


a = 5
a *= 5
print(a)

bere = "count" #ini berfungsi untuk memeriksa apakah karakter didalam string huruf kecil atau tidak
apakah_lower = bere.islower() #Hasilnya bool
print(bere + " is lower = " + str(apakah_lower))

##format string --> format string menggunakan f didepannya
#String
blabla = "boleang"
format_string = f"Botak teleang adalah singkatan dari = {blabla}"
print(format_string)

#bolean
bolean = True
format_string = f"Bolean = {bolean}"
print(format_string)

#angka
blabla = 245.34
format_string = f"angka = {blabla}"
print(format_string)

#bilangan bulat
blabla = 20
format_string = f"Bulat = {blabla:b}" 
print(format_string)

#Dengan ordo jutaan
blabla = 2234304
format_string = f"Jutaan = {blabla:,}"# koma didalam kurung berfungsi untuk menambah koma pada angka
print(format_string)

#Desimal # menampilkan angka dibelakang koma
blabla = 245.34234
format_string = f"Desimal = {blabla:.3f}" # f pada kurung kurawal berarti float sedangkan titik adalah titik pada bilangan desimal
print(format_string)

#leading zero 
#berfungsi untuk menambahkan angka didepan
blabla = 245.34234
format_string = f"angka = {blabla:08.3f}"# 0 hanya akan muncul jika kita membuat banyak angka yg akan di tampilkan lebih banyak dari angka biasa
print(format_string)

#Menampilkan plus(+) dan minus(-)
blabla = -24
blibli = 23.342
format_strung = f"Minus = {blabla:+d}"
format_string = f"Plus = {blibli:+.2f}"# plus dengan desimal
print(format_strung)
print(format_string)

#Memformat persen
persetes = 0.600
format_string = f"Persen = {persetes:.0%}"#.0 berfungsi untuk menampilkan persen
print(format_string)

#melakukan operasi aritmatika didalam placeholder
harga = 23000
jumlah = 3
format_string = f"Aritmatika = {harga*jumlah:,}"
print(format_string)

#format angka lain (binary,octal,hexadecimal)
angka = 265
format_Binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hexadecimal = f"hexa = {hex(angka)}"

print(format_Binary)
print(format_octal)
print(format_hexadecimal)