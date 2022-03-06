#sistem operasi komparasi dan logika
#++++++++3----------10++++++++++
inputUser = float(input("Masukkan angka\nkurang dari 3\natau lebih dari 10 : "))

#++++++++3----------
KurangDari = (inputUser < 3)
print("Hasil kurang dari 3 =",KurangDari)

#--------10+++++++++
LebihDari = (inputUser > 10)
print("Hasil Lebih dari 10 =",LebihDari)

#++++++++3------------10+++++++++
KurangDariAtauLebihDari = KurangDari or LebihDari
print("kurang dari 3 atau lebih dari 10 = ",KurangDariAtauLebihDari)

#-------3++++++++++++10---------
inputUser1 = float(input("Masukkan Angka\nlebih dari 3\ndan\nkurang dari 10: "))

#-------3++++++++++++
LebihDari = inputUser1 > 3
print("Hasil lebih dari 3  =", LebihDari)
#+++++++10-----------
KurangDari = inputUser1 < 10
print("Hsil kurang dari 10 =", KurangDari)
#-------3++++++++++++10---------
lebihDariAtauKurangDari = LebihDari and KurangDari
print("kurang dari 3 atau lebih dari 10 = ",lebihDariAtauKurangDari)
