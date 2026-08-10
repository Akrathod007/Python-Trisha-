# t1 = (1, 2, 3)
# print(t1)
# print(type(t1))

# li = [1, 2, 3, 4, 5]
# t2 = tuple(li)
# print(t2)

# t3 = ()
# print(t3)

# t4 = (10, "Ram", 8.5, True)
# print(t4)

# t5 = 10, 20, 30, 40
# print(t5)

# t6 = ((1, 2, 3), (4, 5, 6))
# print(t6)
# t7 = ([1, 2, 3], (4, 5, 6))
# print(t7)
# t7[0].append(10)
# print(t7[0])
# print(t7[1])


# t8 = (10,)
# print(t8)
# print(type(t8))

# result = t6 + t7
# print(result)


# n = int(input("Enter a number : "))
# li = []
# for i in range(1, n + 1):
#     no = int(input("Enter a element : "))
#     li.append(no)

#     t = tuple(li)
# print(li)
# print(t)


t = (1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 9, True)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))

s = "Hello"

t2 = tuple(s)
print(t2)

print(t.count(5))
print(t.index(5))
print(t.index(5, 5))
# print(t.index(5, 5, 7))


# t = 1, "Ram", 98, 10, 20, 30, 40, 50
# print(t)

# roll, name, marks, *other, x, y = t
# print(roll)
# print(name)
# print(marks)
# print(other)
# print(x)
# print(y)


for i in t:
    print(i)

for i in range(len(t)):
    print(i, "->", t[i])
