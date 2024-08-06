#Challenge 1
var_1=12
var_2=12.93
var_3="123"
print(var_1)
print(var_2)
print(var_3)
print(type(var_1))
print(type(var_2))
print(type(var_3))

#Challenge 2
str1=str(input("Enter a number:"))
print(str1)
c=(int(str1))
print(f"The integer value is {c}")

#Challenge 3
name="Kayla"
age=14
myInfo=f"My name is {name} and I am {age} years old"
print(myInfo)

#Challenge 4
my_Hobbies=["Art",5,68.7,956,9+6j]
for a in my_Hobbies:
    print(type(a))

#Challenge 5
from types import SimpleNamespace
'''myDict={
    "name":"Kayla",
    "age":14,
    "city":"Tipton"
}'''
myDict=SimpleNamespace(name="Kayla",age=14,city="Tipton")
print(myDict)


#Challenge 6
var_1=5
var_2=10
print(f"Before swapping var_1 = {var_1} and var_2 = {var_2}")
var_1,var_2=var_2,var_1
print(f"After swapping var_1 = {var_1} and var_2 = {var_2}")

#Challenge 7
DAYS_IN_WEEK=7
print(DAYS_IN_WEEK)

#Challenge 8
def check_type(var):
    if isinstance(var, int):
        print("The variable is of type int.")
    elif isinstance(var, float):
        print("The variable is of type float.")
    elif isinstance(var, str):
        print("The variable is of type str.")
    else:
        print("Unknown type.")

check_type(10)
check_type(3.14)
check_type("Hello")
check_type([10,3.14,"Hello"])

#Challenge 9
myDict.age=9
print(myDict)

#Challenge 10
myFoods=["cheese","beans","potatoes","tomatoes","lamb"]
print(myFoods[0])
print(myFoods[-1])