

from operator import xor


b = True
c = not b
print("niali B = ",b)

print("-----NOT-----")
print("nilai C = ",c)

print("-----OR-----")
a = False 
b = False
c = a or b
print(a,"or",b,"=",c)
a = False 
b = True
c = a or b
print(a,"or",b," =",c)
a = True 
b = True
c = a or b
print(a," or",b," =",c)
a = True 
b = False
c = a or b
print(a," or",b,"=",c)

print("-----AND-----")
a = False 
b = False
c = a and b
print(a,"AND",b,"=",c)
a = False 
b = True
c = a and b
print(a,"AND",b," =",c)
a = True 
b = True
c = a and b
print(a," AND",b," =",c)
a = True 
b = False
c = a and b
print(a," AND",b,"=",c)

print("-----XOR-----")
a = False 
b = False
c = a ^ b
print(a,"XOR",b,"=",c)
a = False 
b = True
c = a ^ b
print(a,"XOR",b," =",c)
a = True 
b = True
c = a ^ b
print(a," XOR",b," =",c)
a = True 
b = False
c = a ^ b
print(a," XOR",b,"=",c)



