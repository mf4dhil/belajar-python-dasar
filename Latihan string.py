#date and time

import datetime as dt

print("silahkan masukkan tanggal, bulan, dan tahun lahir anda")

tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,tanggal,bulan)
Tanggal_sekarang = dt.date.today()

print(f"Tanggal sekarang adalah = {Tanggal_sekarang}")
print(f"Hari ini adalah = hari {Tanggal_sekarang:%A}\n")

umur_hari = Tanggal_sekarang - tanggal_lahir
umur_bulan = umur_hari.days // 365

print(f"tanggal lahir anda adalah = {tanggal_lahir}")
print(f"Hari lahir anda adalah : hari {tanggal_lahir:%A}")
print(f"Umur anda adalah = {umur_bulan} Tahun")
