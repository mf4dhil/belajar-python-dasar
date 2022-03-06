#Continue, Pass, Dan break

#Passs --> dia berfungsi sebagai dummy tidak akan di eksekusi

# angka = 0 #angka awal

# while angka <5:
#     angka += 1 #angka akan di tambah dengan satu
#     print(f"angkanya --> {angka}")
    
#     if angka == 3:
#         pass #tidak di eksekusi
#     print(angka)
    
#continue #akan membuat loop meloncat ke step selanjutnya

# angka = 0 # angka awal
# print(f"Angka sekarang --> {angka}")

# while angka <5:
#     angka += 1 # angka akan ditambah dengan satu
#     print(f"Angka sekarang --> {angka}") #aksi 1
    
#     if angka == 3:
#         print("wellk!!!")
#         continue #akan membuat loop meloncat ke step selanjutnya
    
#     print("whassup") #aksi 2
    
# print("finishim")

#Break --> akan berhenti jika mencapai angka yang ditentukan

# angka = 0 #--> adalah angka awal
# print(f"angka sekarang adalah --> {angka}")

# while angka <5:
#     angka +=1 #angka awal akan ditambah dengan 1 secara terus menerus
#     print((f"Angka sekarang --> {angka}"))
    
#     if angka == 3: #angka yang ditentukan
#         print("naice!!!")
#         break
    
#     print("wassupp!!")
    
# print("finishhh")


#contoh 2

data_int = int(input("menghitung sampai = ")) #masukkan angka yang ditentukan

angka = 0 #angka awal
print(f"angka sekarang adalah --> {angka}")

while True :
    angka +=1 #angka awal akan ditambah dengan 1 secara terus menerus
    print((f"Angka sekarang --> {angka}"))
    
    if angka == data_int:
        print("naice!!!")
        break
    
    print("wassupp!!")
    
print("finishhh")