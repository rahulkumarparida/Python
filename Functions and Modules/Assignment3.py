#Task 1: Calculate Factorial Using a Function

n = int(input("Enter a number : "))

def Fact(n):
    if n < 2: return 1
    else: return n * (Fact(n-1))
print("Factorial  of " , n , " is: ", Fact(n))


# Using the Math Module for Calculations
import  math
m = int(input("Enter another number : "))
print(" SquareRoot: ",math.sqrt(m))
print(" Logarithmic: ",math.log(m))
print(" Sine: ",math.sin(m))