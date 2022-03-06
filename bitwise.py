#OPERASI BITWISE
a = 7
b = 8
print('nilai =',a,', binery',format(a,'08b'))
print('nilai =',b,', binery',format(b,'08b'))
print('---------OR----------')
#Bitwise OR (|)
#Menjumlahkan antara bilangan biner
c = b | a
print('nilai =',a,', binery',format(a,'08b'))
print('nilai =',b,', binery',format(b,'08b'))
print('nilai OR =',c,', binery',format(c,'08b'))
print('---------AND---------')

#bitwise AND (&) 
#Akan false jika salah satunya false
c = a & b
print('nilai =',a,', binery',format(a,'08b'))
print('nilai =',b,', binery',format(b,'08b'))
print('nilai AND =',c,', binery',format(c,'08b'))
print('---------XOR---------')
#bitwise XOR (^)
#Akan true jika salah satunya true
c = a ^ b
print('nilai =',a,', binery',format(a,'08b'))
print('nilai =',b,', binery',format(b,'08b'))
print('nilai XOR =',c,', binery',format(c,'08b'))
print('---------NOT---------')
#bitwise NOT (~)
#Operasi ini akan memiror data binary 
c = ~a
print('nilai =',a,', binery',format(a,'08b'))
print('nilai NOT =',c,', binery',format(c,'08b'))
print('---------------------')
#Solusi jika kita mau ngeflip kita hanya perlu menambahkan XOR
a = 0b0000000111 #Ini bernilai 7
b = 0b1111111111
print('nilai =',b,', binery',format(b,'08b'))
print('nilai NOT =',a ^ b,', binery',format(a ^ b,'08b'))
print('------shifting-------')

#Berikutnya operasi Shifting
#Operasi shifting berguna untuk memindahkan sebuah kode binar
#Ada dua macam jenis shifting sebagai berikut:
#Shifting right (>>)
#Shifting right berfungsi untuk memindahkan ke kanan
print('------Right-------')
a = 7
b = a >> 1
print('nilai =',a,', binery',format(a,'08b'))
print('nilai =',b,', binery',format(b,'08b'))
b = a >> 2
print('nilai =',b,', binery',format(b,'08b'))

#Shifting left (<<)
#Shifting left berfungsi untuk memindahkan ke kiri
print('------Left-------')
a = 7
b = a << 1
print('nilai =',a,', binery',format(a,'08b'))
print('nilai =',b,', binery',format(b,'08b'))
b = a << 2
print('nilai =',b,', binery',format(b,'08b'))
