#import mymodule #memanggil module
#nama module bisa diganti contohnya
#import mymodule as mx
#a = mx.person1["nama"]

# nama = mymodule.personal1["nama"]
# umur = mymodule.personal1["age"]
# print(nama)
# print(umur)

#import platform #module bawaan

# x = platform.system()
# print(x)
#x = dir(platform)
#print(x)

from mymodule import personal1
print(personal1["nama"])