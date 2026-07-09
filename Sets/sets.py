#Sets: unordered, mutables, no duplicates

mysets = {1,4, 5, 0, 3, 1,4, -5, 7}
myset2 = {"Gonbeloum Espoir"}
print(mysets)
print(myset2)

#Ajout d'un element dans le set
mysets.add(12)
print(mysets)

#utilisation de union et intersection dans set
odd = {1,4,5,6,7,10,23,3}
evens = {1,-3,-2,5, 6,8}
u = odd.union(evens)
print(u)

i = odd.intersection(evens)
print(i)