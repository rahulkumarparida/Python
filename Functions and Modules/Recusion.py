#Recusion

import  sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(50)
n = 0
print(sys.getrecursionlimit())
def Hello(n):
    print("Hello" , n)
    n= n + 1
    Hello(n)
# Hello(n)

##Factorial

# n = int(input("Enter a Number : "))

def Factorial(m):
    if m < 2 :
        return 1
    else:
        return  m * (Factorial(m-1))
# print(Factorial(n))


#Simple Scope trick
b = 1

def inx():
    global b
    b = 3
    print(b)
inx()
print(b)
