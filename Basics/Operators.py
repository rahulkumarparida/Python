''''
#Operators
a = 2
b = 3
b+=a
print(b)
b-=a
print(b)
b*=a
print(b)
b/=a
print(b)
b**=a
print(b)
b//=a
print(b)
e = input("Enter a number : \n")
f = input("Enter another number : \n")
print( int(e)*int(f) , " is the product of the input")
'''
# Simple Intrest Calculator
p = int(input("Enter the amount : "))
r = float(input("Enter the rate of intrest : "))
t = float(input("Enter the time in years : "))
SI = p*r*t/100
print("You Simple Intrest will be : " , SI , "\nYour Have to pay a Total of " , SI+p)
