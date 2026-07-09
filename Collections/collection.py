#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = "aaaaaaabbbbbcccccdddeeee"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys()) #determiner les cles
print(my_counter.values()) #determiner les valeurs

print(my_counter.most_common(1)) #determine la plus grande valeur
print(my_counter.most_common(1)[0]) #indexer la cle et la valeur du premier
#affichage du nbre d'apparition des elements sous forme de liste
print(list(my_counter.elements()))

#NAMETUPLES
point = namedtuple("Point", 'a,b')
pt = point(2, -6)
print(pt)
print(pt.a, pt.b)

#ORDEREDDICT: est comme le dictionnaire ordinaire dans python
ordered_dict = OrderedDict() #ou simple dict avec ordered_dict={}
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)

#DEFAULTDICT : prends une valeur par default dans les parametres
d = defaultdict(int) # int: is a default value here
d['a'] = 2
d['b'] = 1
print(d['b'])

#DEQUE
d = deque()
d.append(3)
d.append(-2)
d.appendleft(5)
print(d)

#remove the last element using pop() or popleft()
d.pop()
print(d)

d.extend([10, -1, 8, -4]) #on peut utiliser extendleft()
print(d)

#rotate elements
d.rotate(1) # all elements are rotate one place to the right
print(d)


