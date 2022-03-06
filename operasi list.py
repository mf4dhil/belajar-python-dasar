#Operasi list

data = [1,2,3,1,2,5,6,4,5,5,2,9,0,8,6,7,5]
print(f"Data Biasa = {data}")

#mencari jumlah data yang ada pada list sperti angka 1 ada 4bh atau angka 2 ada 5bh
jumlah_data1 = data.count(1)
jumlah_data2 = data.count(2)
print(f"Jumlah angka 1 = {jumlah_data1}")
print(f"Jumlah angka 2 = {jumlah_data2}")

#mencari index atau posisi pada list
datas = ["fadhil", "riska", "nayya", "gulugulu"]

po_index_r = datas.index("riska")
po_index_g =datas.index("gulugulu")

print(f"index riska adalah = {po_index_r}")
print(f"index gulugulu adalah = {po_index_g}")

#mengurutkan data pada list
#data int
print(f"data sebelum di urut = \n{data}")
data.sort()
print(f"data setelah diurut = \n{data}")

#data string
print(f"datas sebelum di urut = \n{datas}")
datas.sort()
print(f"datas setelah disort = \n{datas}")

#mengurutkan data dari belakang
#data int
print(f"data yang diurutkan dari depan = \n{data}")
data.reverse()
print(f"data setelah di urut dari belakang = \n{data}")

#data string
print(f"datas yang diurut dari depan = \n {datas}")
datas.reverse()
print(f"datas setelah diurut dari belakang = {datas}")