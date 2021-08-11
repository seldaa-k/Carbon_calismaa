from re import split

liste: str = input('bana alisveris listeni yaz')

print (str.split(liste))
liste= str.split(liste)

print (len(liste))

a= liste[0]
b= liste[1]
print("1. eleman =", a , "", "2. eleman =", b)

txt= "1. eleman = {}, 2. eleman = {}"
print(txt.format(liste[0], liste[1]))

print(liste[-1]+" "+ liste[-2])

liste.append("erik")
print (liste)

liste.pop(-1)
print (liste)

eleman2= liste[1]
print (eleman2[:3])

eleman3 = liste[2]
print(eleman3.upper())

unique=set (liste)
print (unique)

#  Kullanicidan alisveris lisresi yazmasini iste -> sut yougurt kavun
#  string -> list bosluklara gore ayirarak
#  listenin eleman sayisini yazdir.
#  su stringi bastir: "1. eleman = liste[0] , 2. eleman = liste[1]"
#  listenin sondan 2 elemanini yazdir
#  listenin 1. elemanina istedigin herhangi meyveyi ekle
#  listenin son elemanini sil
#  listenin 2. elemaninin ilk 3 karakterini yazdir
#  listenin 3. elemanini tamamen buyuk harflerle yazdir
#  listedeki unique itemlari yazdir.
