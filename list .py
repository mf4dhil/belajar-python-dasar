## membuat list

# data list dengan numbers
data_list = [0,1,2,3,4,5] # --> tanda kurung kotak itu adalah list
print(data_list)
print(30*"=")

#List dengan string
data_list = ["fadhil", "riska" ,"blabla"]
print(data_list)
print(30*"=")

#list string dengan numbers
data_list = [1,"fadhil",3,"riska",6,"blabla"]
print(data_list)
print(30*"=")

#list bolean
data_list = [False,True,True,False]
print(data_list)
print(30*"=")

#list numbers string dan bolean
data_list = ["fadhil",False,10,"riska",True,20]
print(data_list)
print(30*"=")

#cara alternatife membuat list
data_range = range(0,10,2)#--> range (star stop step)
print(data_range)
data_list = list(data_range)
print(data_list)

#membuat list menggunakan for loop, list comprehenshion
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

list_pake_for = [i**2 for i in range(0,10)] # dengan pangkat
print(list_pake_for)

print(30*"=")

#membuat list dengan for dan if
list_pake_for_if = [i for i in range(0,10) if i != 5] #--> menghilangkan angka 5
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 == 0] #--> menampilkan numbers genap
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 != 0] #--> menammpilkan numbers ganjil
print(list_pake_for_if)
