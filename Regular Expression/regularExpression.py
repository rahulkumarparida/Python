#Regualar Expression (reg-ex)
#Strings  validation
# import re(regularExpression)
#Validates the input

import re

#1: Match()

str_1 = "Apple"
str_2 = "Apple" # if i give  AppleAaA then also it returns true

if re.match(str_1,str_2):
    print("True") 
else: 
    print("False")
 
#2: findall()
pattern = "RolllingDownLondonBridge is RollingDownRollingDown"
str_3 = re.findall("Ro", pattern)
print(str_3)

#3: Search()
pattern = "rurfbdgugdrHUH"
if re.search("HUH",pattern, flags=0):
    print("true")
else:
    print("false")


    #4: sub(pattern ,replacement, string , count , flags)

    sentence = "My name is Dwight Schrute"
    pattern = "Dwight Schrute"
    print(sentence)
    print(re.sub(pattern , "Jim Halpert", sentence , count=0 , flags=0))
    


     
#Characters and Chacracters sequence
# ^ - Matches the begining of the line
# $ - Matches the end of the line
# . - Matches any Characters
# \d - Matches any digit
# \D - Matches any Non-digit
# \s - Matches whiteSpace
# \S - Matches any non White space 
#Some more
# * - Repeats a character zero or more times
# + - Repeats a character one or more times
# ( - Indicates where string extraction is to start
# ) - Indicates where string extraction is to end
# ? - Matches the expression 0 to 1 times
#Some More
#[] 
#[aeiou] - Matches a single character in thge list
#[^xyz] - Matches a single charcater
#[a-z 0-9] - set of characters can include range
#{}



str_5 = "Hello my name is andy 69 bernard"
ptn = "^H" #['H']
# ptn = "d$" # ['d']
# ptn = "." #['H', 'e', 'l', 'l', 'o', ' ', 'm', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'a', 'n', 'd', 'y', ' ', '6', '9', ' ', 'b', 'e', 'r', 'n', 'a', 'r', 'd']
# ptn = "^H....." #['Hello ']
# ptn = "......d$" #['bernard']
# ptn = "\d" #['6', '9']
# ptn = "\D" #['H', 'e', 'l', 'l', 'o', ' ', 'm', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'a', 'n', 'd', 'y', ' ', ' ', 'b', 'e', 'r', 'n', 'a', 'r', 'd']
# ptn = "\s" #[' ', ' ', ' ', ' ', ' ', ' ']
# ptn = "\S" #['H', 'e', 'l', 'l', 'o', 'm', 'y', 'n', 'a', 'm', 'e', 'i', 's', 'a', 'n', 'd', 'y', '6', '9', 'b', 'e', 'r', 'n', 'a', 'r', 'd']
# print(re.findall(ptn , str_5 , flags=0))


string_1 = "From rahulroxx098@gmail.com"
# pattern = "ro*" #['ro', 'r', 'ro']
# pattern = "ro+" #['ro', 'r', 'ro']
# pattern = "^F...?"  #['From']
# pattern = "^F.*?" #['F']
# pattern = "^From (\S+@+\S+)" #['rahulroxx098@gmail.com']
# pattern = "(\S)" #['F', 'r', 'o', 'm', 'r', 'a', 'h', 'u', 'l', 'r', 'o', 'x', 'x', '0', '9', '8', '@', 'g', 'm', 'a', 'i', 'l', '.', 'c', 'o', 'm']
pattern = "^From (\S+)" # ['rahulroxx098@gmail.com']
# print(re.findall(pattern , string_1))


string_2 = "pythonn 89464"
# pattern = "[aeiou]" #['o']
# pattern = "[^th]" # ['p', 'y', 'o', 'n']
# pattern = "[a-z]" #['p', 'y', 't', 'h', 'o', 'n']
# pattern = "python{1}" #['p', 'y', 't', 'h', 'o', 'n']

# print(re.findall(pattern , string_2))

string_1 = "From rahulroxx098@gmail.com"
# pattern = ".gmail.com" #['@gmail.com']
pattern = '(@[^ ]*)' #['@gmail.com']
print(re.findall(pattern , string_1))











































