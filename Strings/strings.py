#String: ordered, imnmutable, text representation

my_string = 'Hello, I\'m a leaner programming'
print(my_string)

char = my_string[0]
print(char)

substring = my_string[1:3]
print(substring)

#concate a sentence
greeting = "Hello"
name = "Espoir"
sentence = greeting + "" + name
print(sentence)

for n in name:
  print(n)

#strip methode pour supprimer les espaces

my_string2 = '   je veux vous voir dans l\'immediat    '
my_string2 = my_string2.strip()
print(my_string2.upper()) #upper(): majuscule lower():minuscule

#combine list and string together
my_list = my_string2.split()
print(my_list)