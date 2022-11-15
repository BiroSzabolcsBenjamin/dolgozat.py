import random
list=[]

for i in range(27):
    list.append(random.randint(160,200))

#1
atlagm= sum(list)/len(list)
tizedes= atlagm
print(atlagm,"cm")
#2
print("Legmagasabb tanuló: ",max(list),"cm")

#3
kul= max(list) - min(list)

#4
torony= sum(list)
print("Egymás válára állva a tanulók magassága: ",torony,"m")

#5

#6

#7