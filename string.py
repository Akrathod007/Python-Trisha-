# s1 = "hello"
# s2 = """Good"""

# print(s1)
# print(s2)


# print(s1[-2:-4])
# s = "Mississippi"
# print(s.rfind("i"))
# print(s.rfind("i", 7))
# print(s.rfind("i", 0, 6))
# print(s.count("i", 3, 7))


# name = "Ram"
# age = 25

# print("Name is {} and age is {} {} {}{}".format(name, age, name, name, name))
# print("Name is {} and age is {}".format(age, name))

# print("Name is {name}".format_map({"name": name}))

# print("\042")
# print("\101")
# print("\x41")


# x = chr(101)
# print(x)
# x = chr(111)
# print(x)

# y = ord("w")
# print(y)


# using index
# s = "Mississippi"
# for i in range(0, len(s)):
#     print(i, "->", s[i])


# direct element access
# for i in s:
#     print(i)


s = input("Enter a string : ")
vc = 0

for i in s:
    # if (
    #     i == "A"
    #     or i == "E"
    #     or i == "I"
    #     or i == "O"
    #     or i == "U"
    #     or i == "a"
    #     or i == "e"
    #     or i == "i"
    #     or i == "o"
    #     or i == "u"
    # ):
    #     vc += 1

    if i in "AEIOUaeiou":
        vc += 1

print("Vowel Count is", vc)



# scan string
# find count of alphabet,digit and special symbol

# Ex : ansh123@gamil.com
# ac = 12
# dc = 3
# sc = 2