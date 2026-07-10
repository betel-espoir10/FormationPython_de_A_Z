#Itertools: product, permutation, combination, accumulation, groupby and infinite iterators.

from itertools import product, permutations, combinations,combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator


#PRODUCT : pour creer de couple (a, b) pour chaque valeur

a = [1,3]
b = [2, 4]
prod = product(a,b, repeat=2) #afficher le nombre de repetition entre les valeur
prod = product(a, b)
print(list(prod))

#PERMUTQTIONS
a = [1, 2, 3]
perm = permutations(a) #2: pour specifier la taille de la permutation
print(list(perm))

#COMBINATIONS
a = [1, 2, 3, 4]
comb = combinations(a, 3) #3: nombre de combinaison possible a faire
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

#ACCUMULATE
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

#GROUPBY
def smaller_than_3(x):
  return x<3

a = [1, 2, 3, 4]
group_obj = groupby(a, key= smaller_than_3)
for key, value in group_obj:
  print(key, list(value))

#FONCTION COUNT
a = [1, 2, 3, 4]
for i in count(10):
  print(i)
  if i == 15:
    break
#FONCTION CYCLE
# a = [1, 2, 3, 4]
# for i in cycle(a):
#   print(i)
#   if i == 5:
#     break
  
#FONCTION REPEAT
a = [1, 2, 3, 4]
for i in repeat(a, 3):
  print(i)

