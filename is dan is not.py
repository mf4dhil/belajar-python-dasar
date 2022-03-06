
y = 5
x = 5
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))
hasil = x is y
print("hasilnya =",hasil)

y = 5
x = 5
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))
hasil = x is not y
print("hasilnya =",hasil)

print("=================")
y = 3
x = 5
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))
hasil = x is y
print("hasilnya =",hasil)

y = 3
x = 5
print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))
hasil = x is not y
print("hasilnya =",hasil)