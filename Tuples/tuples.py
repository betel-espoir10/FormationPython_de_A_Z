mytuple = tuple(["Rodri","Betel", 30, "Espoir", 10, "Brya"])
print(mytuple)
print(type(mytuple))

item = mytuple[-1]
print(item)

for i in mytuple:
  print(i)

if "Betel" in mytuple:
  print("Yes")
else:
  print("No")

print(len(mytuple))

print(mytuple.index('Brya'))