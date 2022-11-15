import random
list=[]

for i in range(27):
    list.append(random.randint(160,200))

print(list)
#1
atlagm= sum(list)/len(list)
tizedes= atlagm
print("Az osztály átlagmagassága: ",atlagm,"cm")

#2
print("Legmagasabb tanuló: ",max(list),"cm")


#3
kul= max(list) - min(list)


#4
torony= sum(list)
print("Egymás válára állva a tanulók magassága: ",torony,"m")


#5
#osztaly= list + 182
#print("Osztály átlag az évközben érkezett tanulóval: ",sum(osztaly)/len(osztaly))


#6
list.sort()
list.reverse()
print(list)


#7

