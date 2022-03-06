data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print(f"{data_list_biasa}")

gabungan_data = [data_0,data_1]

print(f"{gabungan_data}")

gabungan_data1 = [data_0,data_1,data_list_biasa]

print(f"{gabungan_data1}") 


#contoh penggunaan

peserta0 = ["fadhil",20,"laki-laki"]
peserta1 = ["mikoto",20,"laki-laki"]
peserta2 = ["marin",19,"wanita"]

list_peserta = [peserta0,peserta1,peserta2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"peserta\t = {peserta[0]}")
    print(f"umur\t = {peserta[1]}")
    print(f"gender\t = {peserta[2]}\n")
    
    
#dengan reference
list_copy = list_peserta.copy();
print(f"peserta = {list_copy}")
print(15*"=")
peserta0[0] = "michael"
print(f"peserta = {list_copy}")
print(f"peserta = {list_copy}")
