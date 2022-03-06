#latihan 2
#1. ------0+++++++5---------8+++++++++11-------
InputAngka = float(input("Masukkan Angka Lebih Dari 0\nKurang Dari 5\nLebih Dari 8\nKurang dari 11 : "))

#-----0++++++
LeDa0 = InputAngka >= 0  
print("Hasil Lebih Dari  =",LeDa0)
#+++++5------
KuDa5 = InputAngka <= 5  
print("Hasil Kurang Dari =",KuDa5)
#-----8++++++
LeDa8 = InputAngka >= 8  
print("Hasil Lebih Dari  =",LeDa8)
#+++++11-----
KuDa11 = InputAngka <= 11  
print("Hasil Kurang Dari =",KuDa11)

#1. ------0+++++++5---------8+++++++++11-------
Correct = LeDa0 and KuDa5 or LeDa8 and KuDa11
print("Hasilnya : ", Correct)

print("\n",10*"=","\n")
#2. ++++++0-------5+++++++++8---------11+++++++
InputAngka = float(input("Masukkan Angka Kurang Dari 0\nLebih Dari 5\nKurang Dari 8\nLebih dari 11 : "))

#+++++++0-------
kuDa0 = InputAngka <= 0  
print("Hasil Lebih Dari  =", kuDa0)
#-------5+++++++
LeDa5 = InputAngka >= 5  
print("Hasil Kurang Dari =",LeDa5)
#+++++++8-------
KuDa8 = InputAngka <= 8  
print("Hasil Lebih Dari  =",KuDa8)
#------11+++++++
LeDa11 = InputAngka >= 11  
print("Hasil Kurang Dari =",LeDa11)

#2. ++++++0-------5+++++++++8---------11+++++++
Correct = kuDa0 or LeDa5 and KuDa8 or LeDa11
print("Hasilnya : ", Correct)
