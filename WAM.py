# width and multiline
#mengatur tinggi dan lebar

nama = "Riska"
Umur = 18
tinggi = 154.3
sepatu = 39
print(5*"="+"Data Riska"+5*"=")
data_riska = f"Nama = {nama}, Umur = {Umur}, Tinggi = {tinggi}, Sepatu = {sepatu}."
print(data_riska)

#dengan menggunakan enter atau new line \n
print(5*"="+"Dengan enter \\n"+5*"=")
data_riska = f"Nama = {nama} \nUmur = {Umur} \nTinggi = {tinggi} \nSepatu = {sepatu}"
print(data_riska)

#dengan triple kutip
print(5*"="+"Tripple kutip"+5*"=")
data_riska = f"""Nama   = {nama}
Umur   = {Umur}
Tinggi = {tinggi}
Sepatu = {sepatu}"""
print(data_riska)

