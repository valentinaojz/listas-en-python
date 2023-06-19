#Metodo append
list = []
list.append("Xiaomi")
list.append("Motorola")
print(list)

#Método insert 
list.insert(1,"Huawei")
print(list)

#Método extend: agrega elementos de otro iterable (como otra lista) al final de la lista actual. 
list_2 = ["Samsung","apple","toshiba"]
list.extend(list_2)
