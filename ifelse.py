# no = 10
# print(no)

# # No : 10
# print("No :" + str(no))
# print("No :", no)


# no1 = int(input("Enter a number 1 : "))
# no2 = int(input("Enter a number 2 : "))
# print("No1 :", no1)
# print("No2 :", no2)
# print(no1 + no2)

# age = int(input("Enter a age : "))

# if age >= 18:
#     print("You can vote")
# else:
#     print("You can't vote")


x = 100
y = 20

# result = "x is bigger" if x > y else "y is bigger"
# print(result)

# print("x is bigger") if x > y else print("y is bigger")


# no = 0

# (
#     print("NO is Positive")
#     if no > 0
#     else print("No is Negative") if no < 0 else print("Zero")
# )


# if 5 > 2:
#     pass

"""
day = int(input("Enter a day : "))

match day:
    case 1:
        print("MON")
    case 2:
        print("TUE")
    case 3:
        print("WED")
    case 4:
        print("THU")
    case 5:
        print("FRI")
    case 6:
        print("SAT")
    case 7:
        print("SUN")
    case _:
        print("Invalid Day Number")

match "Hello":
    case "Hello":
        print("Hii")

match 1.2:
    case 1.2:
        print("Hooo")

match True:
    case True:
        print("True")

"""


print("1 -> Gujarati")
print("2 -> Punjabi")

ch = int(input("Choice : "))

match ch:
    case 1:
        print("Gujarati")
        print("1->fafda")
        ch2 = int(input("Choice in Gujarati : "))
        match ch2:
            case 1:
                print("Fafda")


month = 5

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case 2:
        print("28 or 29 days")
    case _:
        print("Invalid month")


name = "Hello"
age = 21

print("Name is " + name + " age is " + str(age))

print(f"Name is {name} and age is {age}")
