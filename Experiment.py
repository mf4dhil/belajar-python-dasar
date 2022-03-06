import datetime as dt
# Experiment

costumer = input("Nama \t\t= ")
date     = dt.datetime.today()
print(f"Tanggal \t= {date}")
print("\n",30*"-","\n")

NamaBa = input("Nama Barang \t= ")
Harga  = int(input("Harga \t\t= "))
Jumlah = int(input("jumlah \t\t= "))
Nama_ba = input("Nama Barang 2 \t= ")
Harga2 = int(input("Harga 2 \t= "))
Jumlah2 = int(input("Jumlah 2 \t= "))

print("\n",30*"=","\n")

print(f"Nama Barang \t= {NamaBa}")
print(f"Harga \t\t= {Harga:,}")
print(f"Jumlah \t\t= {Jumlah}")
print(f"Nama Barang 2 \t= {Nama_ba}")
print(f"Harga 2\t\t= {Harga2:,}")
print(f"Jumlah 2\t= {Jumlah2}")
tothar1 = Harga * Jumlah
tothar2 = Harga2 * Jumlah2
tothar = tothar1 + tothar2
print("\n",30*"=","\n")
print(f"Total harga \t= {tothar:,}")
