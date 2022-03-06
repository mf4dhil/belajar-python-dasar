data_0 = [1,2]
data_1 =[3,4]

data_2d = [data_0,data_1,10] # yang bisa dikopi cman angka listnya cuman adressnya saja
data_2d_copy = data_2d.copy()

print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")
#mengambil data adri nested list
data = data_2d[1][1]
data1 = data_2d[0][1]
print(f"data = {data}")
print(f"data = {data1}")

#adress semuanya
print(f"adress asli = {hex(id(data_2d))}")
print(f"adress copy = {hex(id(data_2d_copy))}")

print("adress dari member ke-1")
print(f"adress asli = {hex(id(data_2d[0]))}")
print(f"adress copy = {hex(id(data_2d_copy[0]))}")

data_2d[2] = 9
data_2d[1][0] = 6

print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")

from copy import deepcopy

data_2d = [data_0, data_1,10]
data_2d_deepcopy = deepcopy(data_2d)

print(f"adress asli = {hex(id(data_2d))}")
print(f"adress copy = {hex(id(data_2d_deepcopy))}")

print("adress dari member ke-1")
print(f"adress asli = {hex(id(data_2d[0]))}")
print(f"adress copy = {hex(id(data_2d_copy[0]))}")

data_2d[1][0] = 100
print(f"data = {data_2d}")
print(f"data copy = {data_2d_copy}")
print(f"data deep = {data_2d_deepcopy}")


