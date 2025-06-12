a =int(input("Enter a Number : "))
b = int(input("Enter another Number (try 0 ) : "))
try:
    print(a/b)
except ZeroDivisionError:
    print("There is an Error ")
finally:
    print("The task has came to an end")