#Challenge 1
myname="Kayla"
print("Hello"+myname)

#Challenge 2
import datetime
print('My current year is:', datetime.datetime.now().year)

#Challenge 3
def firstname(myname):
    print(f"My name is {myname}")
firstname("Kayla")

def info(name="Jane",age=7,Class="9Y",bestfriend="Katy"):
    print(f"My name is {name}, I'll be {age+2} in two years, i am in {Class} and my best friend is {bestfriend} ")
info("Kayla",16,"8X","Nancy")


#Challenge 4
firstnum=int(input("Enter the first number:"))
secondnum=int(input("Enter the second number:"))
print(firstnum+secondnum)

#Challenge 5
myName="John"
myAge=19
print(f"My name is {myName} and I am {myAge} years old")

#Challenge 6
fav_food=str(input("What is your favourite food?:"))
fav_drink=str(input("What is your favourite drink?:"))
print(f"My favourite food is {fav_food} and my favourite drink is {fav_drink}")

#Challenge 7
myHobby="""My favourite hobby is baking because it is fun.
I also like drawing because it is peaceful and relaxing"""
print(myHobby)

#Challenge 8
fav_colour=str(input("What is your favourite colour?:"))
print(fav_colour)

#Challenge 9
float1=9.1
int1=8
str1="10"
print(type(int1))
print(type(float1))
print(type(str1))

#Challenge 10
for a in range(1,11):
    print(a)