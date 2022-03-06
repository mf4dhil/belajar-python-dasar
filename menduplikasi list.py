##Teknik menduplikasi list
a = ["fadhil","riska","pudhwh"]
print(f"Data a = {a}")

b = a
print(f"Data b = {b}")

#kita coba rubah list b
b[2] = "ayam"
print(f"Data a = {a}")
print(f"Data b = {b}")

#kita urutkan list b
b.sort()
print(f"Data a = {a}")
print(f"Data b = {b}")

#kita lihat alamat adressnya
print(f"Alamat adress A = {hex(id(a))}")
print(f"Alamat adress b = {hex(id(a))}")

#maka untuk mengubah data pada list kita perlu menduplikatnya terlebih dahulu
#untuk menduplikat kita hanya perlu menggunakan copy
c = a.copy()
print(f"Alamat adress a = {hex(id(a))}")
print(f"Alamat adress b = {hex(id(b))}")
print(f"Alamat adress c = {hex(id(c))}")

#selanjutnya mari kita mencoba merubah data pada list c
print(f"Alamat adress a = {a}") 
print(f"Alamat adress b = {b}")
print(f"Alamat adress c = {c}")
c[0] = "gokil" 
#jadi dapat kita artikan misalkan jika adress pada variable listnya sama dan kita mengubah datanya
#maka data yang lain dengan adress yang sama akan ikut berubah
#maka kita perlu membuat variable baru dengan alamat adress yang berbeda 
#dengan cara menduplikat list tersebut dengan copy
#barulah datanya bisa beruba dengan tidak mempengaruhi data yang lain
