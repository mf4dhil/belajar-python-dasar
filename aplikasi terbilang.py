# program sederhana yang menerjemahkan angka

angka = input("masukkan angka = ")


variable = {
    "1" : "satu",
    "2" : "dua",
    "3" : "tiga",
    "4" : "empat",
    "5" : "lima",
    "6" : "enam",
    "7" : "tujuh",
    "8" : "delapan",
    "9" : "sembilan",
     
}

output = ""

for i in angka:
    terjemah = variable.get(i,"not understand")
    output = output + terjemah + " "
    
print(output)