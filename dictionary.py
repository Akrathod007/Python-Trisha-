# person = {"Name": "Ram", "Age": 22, "City": "Ahm"}

# print(person)
# print(type(person))

# marks = dict(Raju=90, Kaju=94, Maju=86, Taju=79)
# print(marks)

# print(marks["Raju"])
# print(marks.get("Maju"))
# # print(marks["Riya"])
# print(marks.get("Riya", "Not Found"))

# marks["Raju"] = 98
# print(marks)

# marks.update({"Raju": 70, "Priya": 98})
# print(marks)
# del marks["Taju"]
# print(marks)

# val = marks.pop("Maju")
# print(val)
# print(marks)

# val = marks.popitem()
# print(val)
# print(marks)

# marks.clear()
# print(marks)

# marks.popitem()

# print(marks.keys())
# print(marks.values())
# print(marks.items())

# for i in marks:
#     print(i, "->", marks[i])

# for i in marks.keys():
#     print(i, "->", marks.get(i))

# for v in marks.values():
#     print(v)

# for k, v in marks.items():
#     print(k, "->", v)


# marks2 = marks.copy()
# print("--------------------------------------------------------------------------")

# print(marks)
# print(marks2)

# marks2["Raju"] = 50
# print("--------------------------------------------------------------------------")

# print(marks)
# print(marks2)

# marks["Priya"] = 100
# print("--------------------------------------------------------------------------")
# print(marks)
# print(marks2)

# marks3 = marks
# print("--------------------------------------------------------------------------")
# print(marks3)

# marks3["Kaju"] = 97
# print("--------------------------------------------------------------------------")

# print(marks)
# print(marks3)


# li = ["Maths", "Science", "Arts"]

# d = dict.fromkeys(li, 0)
# print(d)

# d.setdefault("Hindi", 100)
# print(d)

# print(d.setdefault("Maths"))

# keys = ["Name", "Age", "City"]
# values = ["Ram", 21, "Ahm"]

# d = dict(zip(keys, values))
# print(d)


"""
1. Count Frequency of Characters
word = "python"

freq = {
    "p":1
}
"""

# word = "Mississippi"

# d = {}

# for ch in word:
#     d[ch] = d.get(ch, 0) + 1

# print(d)


"""
2. Count Frequency of Words
sentence = "python is easy python is powerful"
"""

# d = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20, "f": 40, "g": 20}

# values = list(d.values())

# duplicate = []

# for v in values:
#     if values.count(v) > 1 and v not in duplicate:
#         duplicate.append(v)

# print(duplicate)


# d = {
#     "Rakesh": {"Maths": 90, "Hindi": 95, "Science": 85},
#     "Mahesh": {"Maths": 80, "Hindi": 85, "Science": 75},
#     "Suresh": {"Maths": 70, "Hindi": 75, "Science": 95},
#     "Paresh": {"Maths": 85, "Hindi": 85, "Science": 65},
#     "Rajesh": {"Maths": 95, "Hindi": 77, "Science": 92},
# }

# print(d)
# print(d.get("Mahesh").get("Hindi"))

# d.get("Paresh")["Science"] = 95
# print(d)

# for i in d:
#     total = 0
#     print(i, "->", d.get(i))
#     for j in d.get(i).values():
#         total = total + j

#     print(f"{i}'s total = {total}")


# d = {
#     "Virat": [90, 85, 76, 95, 67],
#     "Dhoni": [67, 88, 92, 85, 79],
#     "Gill": [80, 76, 69, 50, 91],
#     "Rohit": [67, 89, 56, 81, 85],
#     "Sachin": [97, 78, 93, 85, 73],
# }


"""
d = {
    1:1,
    2:4
}
"""

d = {i: i * i for i in range(1, 11)}
print(d)

even = {i: i * i for i in range(1, 11) if i % 2 == 0}
print(even)

evenOdd = {i: (i * i if i % 2 == 0 else i**3) for i in range(1, 11)}
print(evenOdd)

# words = ["Apple", "Banana", "Mango", "Kiwi", "Watermelon"]
# Task 1 : "Apple":5
# Task 2 : "Apple":"elppA"

"""
{
    "Apple":5,
}
"""

"""
Create a dictionary using two lists.

keys = ["name", "age", "city"]
values = ["Ram", 11, "Surat"]
"""


words = ["Apple", "Banana", "Mango", "Kiwi"]
"""
{
    "Apple": "A5",
    "Banana": "B6",
    "Mango": "M5",
    "Kiwi": "K4"
}
"""

d = {fruit: fruit[0] + str(len(fruit)) for fruit in words}
print(d)


d = {}

for i in words:
    d[i] = i[0] + str(len(i))

print(d)
