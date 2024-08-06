#Challenge 1
n=int(input("Enter a number:"))
v=int(input("Enter a number:"))
print(n+v,n-v,n*v)

#Challenge 2
f=float(input("Enter a float:"))
c=float(input("Enter a float:"))
print(f/c)

#Challenge 3
print(1j+3j,2j-7j)

#Challenge 4
n=int(input("Enter a number:"))
s=int(input("Enter a number:"))
if n>s:
    print("4 is greater than 5")
elif n==s:
    print("4 is equal to 5")
else:
    print("4 is less than 5")

#Challenge 5
num=int(input("Enter a number:"))
if num % 2:
    print("The number is odd")
else:
    print("The number is even")

#Challenge 6
c=3.2
print(c)
print(int(c))

#Challenge 7
myList=[3,6,8,4,5,6]
avg=sum(myList[:5])
favg=avg/len(myList)
print(favg)

#Challenge 8
Min1= min(myList)
Max1= max(myList)
print(Max1,Min1)

#Challenge 9
n=5

#Challenge 10
x= 8
def factorial(x):
    x=int(input("Enter a number:"))
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
        
print('Factorial:',factorial(80)) #error fixed name error corrected x to 80
