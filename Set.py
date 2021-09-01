# Set
s = {1, 2, 3, 4, 5, 6, 7, 9, 10, 15}
print(s)
print(type(s))
s.add(20)
print(s)
s.remove(9)
print(s)
# set no index
s1 = {1, 2, 2, 3, 3, 4, 5, 6, 7, 9, 10, 15}
print(s1)
print(s.union(s1))  # common uncommon all print
print(s.intersection(s1))  # shudhu common gula
print(s.issubset(s1))  # uposet as a ki na
print(s.difference(s1))  # ki vinno asa
