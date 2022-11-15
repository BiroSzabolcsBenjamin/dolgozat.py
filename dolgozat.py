import random


list=[]

for i in range(27):
    list.append(random.randint(160,200))

print("Tanulók magassága",list)

#1
atlagm= sum(list)/len(list)
tizedes= atlagm

print("Az osztály átlagmagassága: ",round(atlagm,2),"cm")

#2
print("Legmagasabb tanuló: ",max(list),"cm")


#3
kul= max(list) - min(list)
print("A legmagasabb és a legalacsonyabb tanuló közötti különbség: ",kul,"cm")

#4
torony= sum(list)
print("Egymás válára állva a tanulók magassága: ",torony,"m")


#5
ujtanulo= [182]
osztaly= list + ujtanulo
print("Tanulók magasság az új tanulóval: ", osztaly)

#6
osztaly.sort()
osztaly.reverse()
print("Tornasorba rendezve: ",osztaly)

#7
if(list==list):
    print("Vannak egyformán magas tanulók")
else:
    print("Nincsenek egyformán magas tanulók")


