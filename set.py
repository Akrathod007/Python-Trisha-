"""s1 = {1, 2, 3, 4, 5}
print(s1)
print(type(s1))

li = [1, 2, 3, 4, 2, 3, 4, 5]
s2 = set(li)
print(s2)

# print(s2[0]) #Error

# s3 = {[1, 2, 3], [4, 5, 6]}
# print(s3)

s4 = {(1, 2, 3)}
print(s4)

# s5 = {{1, 2, 3}, {4, 5, 6}}
# print(s5)

s5 = {1, 2, 3, 4, 5, 6}
s5.add(7)
print(s5)


s5.remove(4)
# s5.remove(44)

# s5.discard(3)
# s5.discard(33)

elm = s5.pop()
print(elm)
print(s5)

s6 = {"Apple", "Banana", "Kiwi", "Mango"}
print(s6)
elm = s6.pop()
print(elm)
print(s6)


s6.clear()
print(s6)

s7 = {}
print(type(s7))

s8 = set()
print(s8)
print(len(s8))

"""

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
"""
print(a | b)
print(a.union(b))

print("-----------------------------------------------------")
print(a.intersection(b))
print(a & b)

print("-----------------------------------------------------")
print(a - b)
print(b.difference(a))

print("-----------------------------------------------------")
print(a.symmetric_difference(b))
print(b ^ a)

print("-----------------------------------------------------")

x = {1, 2}
y = {1, 2, 3}

print(x <= y)
print(x.issubset(y))
print(y >= x)
print(y.issuperset(x))
print(x.issuperset(y))

print(y == x)
print("-----------------------------------------------------")

l = {1, 2, 3}
m = {4, 5, 6}
print(l.isdisjoint(m))

"""
"""
a = {1,2,3,4}
b = {3,4,5,6}
"""

a.update(b)
print(a)  # {1,2,3,4,5,6}

a.intersection_update(b)
print(a)  # {3,4,5,6}

a.difference_update(b)
print(a)  # set()

a.symmetric_difference_update(b)
print(a)  # {3,4,5,6}

fs = frozenset(a)
print(fs)
# fs.add()
