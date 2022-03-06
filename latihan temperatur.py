#latihan konversi temperatur

fahrenheit = float(input("Masukkan Suhu Fahrenheit = "))
print("Suhu fahrenheit adalah = ",fahrenheit,"fahrenheit")

kelvin = ((5/9) * (fahrenheit - 32)) + 273
print("Suhu fahrenheit ke kelvin adalah = ",kelvin,"kelvin")

fahrenheit = ((kelvin - 273) * (9/5)) + 32
print("suhu kelvin ke fahrenheit adalah = ",fahrenheit,"fahrenheit")

