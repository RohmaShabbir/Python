#  WAP to check if a number enterned by the user is odd or even.

num = int(input("Enter number:"))


if (num % 2 == 0):
    print("The number is even.")
else: 
    print("the number is odd.")

# <------------------------->

#  WAP to findest the gratest of 3 number interned by the user.

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if(a >= b and a >= c):
    print("The greatest number is:" , a)
elif(b >= a and b>= c):
    print("The greatest number is:", b)
else:
    print("Ther greatest number is:", c)

# <------------------------->

#  WAP to check if a number is a multiple of 7 or not.

num = int(input("Enter number:"))

if(num % 7 == 0):
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")

