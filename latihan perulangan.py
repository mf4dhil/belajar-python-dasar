#latihan loop

#Menggunakan for
from itertools import count


sisi = 5
tambah = 1
for i in range(sisi):
    print("*"*tambah)
    tambah += 1
    
    


#Menggunakan while
tambah = 1
while True:
    if (tambah%2):
        print("*"+tambah)
        tambah -= 1
        continue
    
    else:
        tambah += 1
        continue
    
    if tambah > sisi:
        tambah += 1
        break
    
for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()

    
    
        
    
    
    
    
    