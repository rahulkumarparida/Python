#Task 1: Read a File and Handle Errors

try:
    SampleFile = open("Sample.txt" , 'r+')
    a = SampleFile.read()
    print(a)
    SampleFile.close()
except FileNotFoundError:
    print("The File you asked Does not exist")
finally:
    print("task executed ")


#Task 2: Write and Append Data to a File
a =  input("Enter the Statement you want to enter in the file : ")
OutputFile = open("Output.txt" , "r+")
OutputFile.write(a)
print("Data sucessfully written to Output.txt\n")
OutputFile.close()

b = input("Enter additional text to append : ")
OutputFile = open("Output.txt" , "a")
OutputFile.write("\n"+b)
print("Data sucessfully appended\n")
OutputFile.close()

OutputFile = open("Output.txt" , "r+")
e =OutputFile.read()
print(e)
OutputFile.close()
