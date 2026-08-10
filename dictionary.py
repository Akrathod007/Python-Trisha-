person = {"Name": "Ram", "Age": 22, "City": "Ahm"}

print(person)
print(type(person))

marks = dict(Raju=90, Kaju=94, Maju=86, Taju=79)
print(marks)

print(marks["Raju"])
print(marks.get("Maju"))
# print(marks["Riya"])
print(marks.get("Riya", "Not Found"))

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

print(marks.keys())
print(marks.values())
print(marks.items())

for i in marks:
    print(i, "->", marks[i])

for i in marks.keys():
    print(i, "->", marks.get(i))

for v in marks.values():
    print(v)

for k, v in marks.items():
    print(k, "->", v)
