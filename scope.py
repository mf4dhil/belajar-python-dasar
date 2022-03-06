#scope
"""
Variabelnya hanya tersedia di dalam lingkup fungsinya saja, itulah yang disebut dengan scope

lingkup lokal
variable yang ada di dalam fungsi hanya bisa di acces di lingkup lokal itu
tidak bisa di acces diluar lingkup fungsi
"""


def myfunc():
    x = 90
    print(x)
    
myfunc()

print(20*"-")
"""
seperti yang dijelaskan di atas fungsi didalam fungsi dapat digunakan tetapi jika
digunakan untuk fungsi yang berada diluar lingkup lokal atau diluar fungsi itu sendiri
maka akan terjadi eror
"""
def myfunc():
    x = 80
    def minerfunc():
        print(x)
    minerfunc()
myfunc()

print(20*"-")
"""
lingkup global
lingkup adalah sebuah variable yg dapat kita acces secara global atau didalam ataupun dkiluar fungsi
seperti yang dapat kita lihat dibawah ini
"""
x = 90
def myfunc():
    print(x)
    
myfunc()

print(x)

print(20*"-")
"""
jika anda membuat variable dengan nama yang sama dengan lingkup yang berbada
seperti, misalkan salah satunya berada diluar fungsi, dan yang satunya lagi berada 
didalam fungsi, maka kedua variable itu diperlakukan secara terpisah
"""
x = 100
def myfunc():
    x = 200
    print(x)
    print(f"adress id = {hex(id(x))}")

myfunc()

print(x)
print(f"adress id = {hex(id(x))}")

print(20*"-")
"""
jika ingin membuat varible lokal menjadi variable global maka kita perlu menggunakan
keyword 'global' agar variablenya dapat diacces secara global
"""
def myfunc():
    global x
    x = 300
    
myfunc()
print(x)

print(20*"-")
"""
kamu juga bisa merubah nilai varible global didalam sebuah fungsi
"""
x = 200
f = "sisi"
def myfunc():
    global x
    x = 100
    global f
    f = "fadhil"
myfunc()
print(x)
print(f)

    

