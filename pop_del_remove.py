n = [1, 3, 5]
# Remove the first item in the list here
n.remove(1)
print n
n.append(123)
n.append(1)
print n

# pop returns and deletes at index
# del deletes at index and not return
#  remove the actual item passed and not index based
n.pop(1)
print n

n.remove(123)
print n

n.remove(1)
n.append(3)
print n
del(n[1])
del(n[1])
print n
del(n[0])
n.append(5)