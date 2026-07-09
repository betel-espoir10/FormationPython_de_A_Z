#declaration d'une dictionnaire: key-value pairs, unordered, mutable
mydict = {"name": "Alex", "age": 20, "ville": "Kelo"}
mydict2 = dict(name= "Idrissou", age=30, position= "Ingenieur")
print(mydict)

#Ajout d'element dans le dictionnaire
mydict["email"] = "alex@gmail.com"
print(mydict)

mydict["pays"] = "Tchad"
print(mydict)

#suppression d'elements dans un dictionnaire
del mydict["ville"]
print(mydict)

#Affichage des cles et valeurs
for key in mydict.keys():
  print(key)

for value in mydict.values():
  print(value)

for key, value in mydict.items():
  print(key, value)

#update a dictionnaire
mydict.update(mydict2)
print(mydict2)