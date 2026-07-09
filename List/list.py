mylist = ["banana", "carrot", "patotoes"]
mylist2 = [3, 5, 8, -5, -1, -9, 4]
print(mylist)

item = mylist[0] #indexer un element de la liste
print(item)

for i in mylist:
  print(i)

print(len(mylist))
mylist.append("lemon") #ajout element a la fin de la liste
print(len(mylist))

mylist.insert(1, "apple") #ajout element dans un espace specifie
print(mylist)

rm = mylist.pop() #supprimer la derniere valeur dans la liste
print(rm)

print(mylist)

rm = mylist.reverse() #Inverser les valeurs dans une liste
print(mylist)

print(mylist2)
mylist2.sort()  #Arranger les valeurs par croissant
print(mylist2)

#concatener deux liste
mylist3 = mylist + mylist2
print(mylist3)

#Especifier les valeurs a afficher
a= mylist3[1:6]
print(a)