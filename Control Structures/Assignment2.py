#Task 1: Check if a Number is Even or Odd
a = int(input("Enter a Number : "))
if a%2 == 0:
    print("It is an Even Number")
else:
    print("It is an Odd Number")

#Task 2: Sum of Integers from 1 to 50 Using a Loop
a = 0
b=0
while a <= 50:
    b += a
    a += 1
print(b)