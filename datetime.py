"""
Tanggal Python, Tanggal di Python bukanlah tipe data sendiri, 
tetapi kita dapat mengimpor modul bernama datetime
untuk bekerja dengan tanggal sebagai objek tanggal.
"""
#Impor modul datetime dan tampilkan tanggal saat ini:
# import datetime
# x = datetime.datetime.now()
# print(x)

"""
Output Tanggal
Ketika kita mengeksekusi kode dari contoh di atas hasilnya adalah:
2022-03-03 14:25:44.465073

Tanggal tersebut berisi tahun, bulan, hari, jam, menit, detik, dan mikrodetik.
Modul datetime memiliki banyak metode untuk mengembalikan informasi tentang objek tanggal.
Berikut adalah beberapa contoh, Anda akan mempelajari lebih lanjut tentang mereka nanti di bab ini:
"""
#Contoh Kembalikan tahun dan nama hari kerja:
import datetime
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))