a = 8
#if
if a > 9:
    print("Greater than 9")
if a < 9 :
    print("Lesser than 9")

#if-else
b = int(input("Enter you age : "))
if  b > 18:
    print("Eligible for Voting")
else:
    print("Not Eligible for voting")
print("thank you")

#elif
operand1 = int(input("Enter the first number : "))
operand2 = int(input("Enter the Second number : "))
operator = input("Enter the operator (+,-,*,/): ")

if operator == "+":
    print("Addition : " , operand1+operand2)
elif operator == "-":
    print("Substraction : ", operand1 - operand2)
elif operator == "*":
    print("Multiplacation : ", operand1* operand2)
elif operator == "/":
    print("Division : " , operand1/operand2)
else:
    print("Invalid Operator")

#Range Function
n = list(range(10))
print(n)
#Start Value : 2
#End Value : 16
#Step : 2
m = list(range(2 , 17 , 2))
print(m)






