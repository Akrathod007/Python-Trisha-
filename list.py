"""
Types of collections :
1.List
2.Tupel
3.Dictionary
4.Set


1. List : It is collections of mix types data and is ordered and mutable
list is created by []
"""

# l1 = [1, 2, 3, 4, 5]
# print(l1)
# print(type(l1))
# l2 = [1, 3.4, "Hello", True]
# print(l2)

# l3 = []
# print(l3)

# print(len(l1))
# print(len(l3))


# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(l1)
# print(l1[3])
# print(l1[8])
# print(l1[-2])
# print(l1[-7])

# slicing
# syntax : l1[start:end:step]

# print(l1[0:5])  # 0 -> 4
# print(l1[:7])
# print(l1[2:])
# print(l1[:])
# print(l1[2:8:2])
# print(l1[1:10:4])
# print(l1[::3])
# print(l1[::-1])
# print(l1[-2:-8])
# print(l1[-8:-2])
# print(l1[-2:-8:-1])
# print(l1[::-4])
# print(l1[3:-2])

# using index:

# for i in range(0, len(l1)):
#     print(i, "->", l1[i])


# direct element access:
# for i in l1:
#     print(i)


# Methods

li = [1, 2, 3, 4, 5]
print(li)
li.append(7)
print(li)
li.insert(3, 3000)
print(li)

l2 = [11, 12, 13, 14, 15]
# result = li + l2
# result = li + "ABC"
# print(result)
# print(li)

# li.extend(l2)
# l2.extend(li)
# l2.extend("ABC")
# l2.extend((100, 200, 300))
# l2.extend(("x", "y", "z"))
# print(li)
# print(l2)


# print(l2 * 5)

# l2[3] = 300
# print(l2)
# l2[10] = 1000
# print(l2)

# l2[0:3] = 1, 2, 3
# print(l2)


# elm = l2.pop()
# print(elm)
# print(l2)

# elm = l2.pop(2)
# print(elm)
# print(l2)

# # l2.pop(11)

# l2.remove(11)
# # l2.remove(111)
# print(l2)

# l3 = []
# l3.pop()

# l2.clear()
# print(l2)


# l3 = [1, 2, 3, 4, 3, 4, 5, 3, 2, 3, 4, 5]
# print(l3.count(3))
# print(l3.index(2, 3, 9))
# # print(l3.index(2, 3, 7))
# print(l3.index(2, 3))

# l3.sort()
# print(l3)
# l3.reverse()
# print(l3)

# print(l3)
# l4 = l3  # shallow copy
# l4 = l3.copy()  # deep copy
# l4 = l3[:]
# l4[0] = 100
# print(l3)
# print(l4)


# l = []
# n = int(input("Enter a n : "))

# for i in range(1, n + 1):
#     # no = int(input("Enter a element : "))
#     # l.append(no)
#     l.append(int(input("Enter a element : ")))

# print(l)


# names = ["madam", "sir", "hello", "bob", "bye"]

# palindrome = []

# for i in names:
#     if i == i[::-1]:
#         palindrome.append(i)

# print(palindrome)


# nums = [1, 2, 3, 4, 5, 3, 4, 2, 6, 7, 5, 8, 6, 9, 5]
# unique = []
# duplicate = []
# for i in nums:
#     if nums.count(i) == 1:
#         unique.append(i)
#     else:
#         if i not in duplicate:
#             duplicate.append(i)
# print(unique)
# print(duplicate)

# li = [1, 4, 0, 6, 7, 0, 2, 3, 0, 0, 9]

# [1,4,6,7,2,3,9,0,0,0,0]
# x = []

# for i in li:
#     if i != 0:
#         x.append(i)

# zeroCount = li.count(0)
# print(x)

# for _ in range(1, zeroCount + 1):
#     x.append(0)

# print(x)


# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 4, 5, 6]

# common = []

# for i in l1:
#     if i in l2:
#         common.append(i)

# print(common)


# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7, 8]

# x = []
# for i in l1:
#     if i not in l2:
#         x.append(i)

# for i in l2:
#     if i not in l1:
#         x.append(i)

# print(x)

# li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(li)
# print(len(li))
# print(li[2])
# print(li[2][2])
# print(li[1][1:2])

# for i in li:
#     print(i)
#     for j in i:
#         print(j)


# for i in range(0, len(li)):
#     print(i, "->", li[i])
#     for j in range(0, len(li[i])):
#         print(j, "->", li[i][j])


r = int(input("Enter a row : "))
c = int(input("Enter a column : "))
# ol = []
# for i in range(1, r + 1):
#     il = []
#     for j in range(1, c + 1):
#         # elm = int(input("Enter a element : "))
#         # il.append(elm)  # [1,2,3,4,5]
#         il.append(int(input("Enter a element : ")))
#     ol.append(il)

# print(ol)

ol = [[int(input("Enter the element :")) for i in range(r)] for j in range(c)]


# ol = [
#     [int(input("Enter a element : ")) for j in range(1, c + 1)] for i in range(1, r + 1)
# ]
print(ol)
