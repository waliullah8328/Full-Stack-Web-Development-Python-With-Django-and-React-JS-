#  list - [] er mod a some data
l = [1,2,5,6,89.7,12,78.9,'name','age',12,56.4]
print(l)
print(type(l))
print(l[0])
print(type(l[0]))
#Slicing
print(l[2 : 5])
print(l[0 : 5])
print(l[: 5])
print(l[: ])
print(l[: -2])
print(l[:: -1])
print(l[:]*2)

# Pop function - pop man a ber kor a niye as a
pop_value = l.pop(2)
print(pop_value)
print(l)

# List compare
l4 = [i for i in range (11)]
print(l4)
print(l.count(6))
l.remove('name')
l.remove('age')
print(l)
l.reverse()
print(l)
l.sort()
print(l)
l.append(100)
print(l)