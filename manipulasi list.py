##manipulasi list

#Operasi

#nomor urut list 0(-3)  1(-2)   2(-1)
data_list = ["fadhil","riska","nayya"]
ambil_data = data_list[0] #mengambil data
print(f"data yang di ambil adalah --> {ambil_data}")

ambil_data = data_list[-1]#mengambil data
print(f"data yang di ambil adalah --> {ambil_data}")

#mengambil info jumlah data dalam list

info_data = len(data_list) #mengambil info jumlah data
print(f"jumlah data --> {info_data}")

##Manipulasi

#menambahkan data kedalam list sesuai posisi

print(f"data sebelum ditambahkan --> {data_list}")

data_list.insert(1,"marin")#Menambahkan data kedalam list sesuai posisi yang diinginkan
print(f"data setelah ditambahkan --> {data_list}")

#Menambahkan data di akhir list

data_list.append("kuntul") #menambahkan data di akhir list
print(f"Data setelah ditambahkan --> {data_list}")

#menambahkan list dengan list

list2 = ["samyang","boleang", "gulugulu"]
data_list.extend(list2) #berfungsi untuk menggabungkan list atau menambahkan list dengan list

print(f"List setalh di gabung --> {data_list}")

#merubah data
data_list[5] = "gehol" #kida ubah data no 5 menjadi gehol
print(f"data yang di ubah --> {data_list}")

##Meremove data
#remove
data_list.remove("kuntul") #berfungsi untuk menghapus data
print(f" data setelah diremove --> {data_list}")

#meremove data paling belakang 
remove_akhir = data_list.pop() #berfungsi untuk menghapus data paling belajakang dan bisa ditampilkan kembali
print(f"Data setelah di remove dengan pop = \n {data_list}")
#menampilkan data yang diremove menggunakan pop
print(f"tampilkan data yang diremove menggunakan pop --> {remove_akhir}")