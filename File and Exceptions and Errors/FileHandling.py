# Method 1
# operatiuon here such as read , write append
file1 = open("file1.txt", "r")
a = file1.read(5) ##inside argumnents are for the number of characters printed
print(a)
file1.close()

# method 2
# with open("file1.txt" , "w") as  file1:
# statements

# write
file2 = open("file1.txt" , "w")
b =file2.write("Hello Guys Welcome back to my channel") ##erases all the previous data
print(b)
file2.close()


# append
file3 = open('file2.txt', "a")
c = file3.write("HOPE EVERY ONE IS DOING WELL THIS THE ONE I WROTE USING PYHTON\n")
# print(c)
file3.close()

file3 = open('file2.txt', "r")
d = file3.read()
print(d)
file3.close()


# r+ to read and write
file4 = open("file1.txt", "r+")
e = file4.write("this can read and write at the same time but have to have two diffrent methods so i don't see the use of this\n")
print(e)
file4.close()
file4 = open("file1.txt", "r+")
f = file4.read()
print(f)
file4.close()
