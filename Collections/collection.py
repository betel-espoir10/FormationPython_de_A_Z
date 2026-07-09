#Collections: Counter, namedtuple, OrderedDict, defaultdict

from collections import Counter

a = "aaaaaaabbbbbcccccdddeeee"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys()) #determiner les cles
print(my_counter.values()) #determiner les valeurs

print(my_counter.most_common(1)) #determine la plus grande valeur