#Dictionaries or Dict -- {Key1 : value1 ,key2: value2 } key value pairs
b = {"Name":"Rahul","Age": 21 , "D.O.B.":"29-09-2004"}
# print(b["D.O.B."]) # Dictionaries calling
c = {1:"Hello", 2: "World" , 3: "How are you ?"}

c[4] = " I'm Fine Thank You!!"
del(c[3])
# print(c)
# print(c.keys())
# print(c.values())


#List
# Type -- [1,2,3,4,5] index values
a = [1,2,3,4,5,6,7,8]
# print(a[1]) # prints 2
e = [1,"Harry" , 2 , "Ginny" , 3, "Albus"]
# print(a+e)
# print(a*2)
# print( 9 in a)
# a.append(9)
# print(a)
# a.extend([{1:"Dictionaries inside"},{2: " List "}])
# print(a)
# a.remove({2: " List "})
# print(a)
# del a[9]
# print(a)
# a.clear()
# print(a)
# a.pop(1)
# print(a)
# a.insert(1 , "removed")
# print(a)
# a.reverse()
# print(a)
# print(a.index(8))
# print(len(a))

#a[StartIndex:EndIndex+1:Gaps]
# print(a[0:5:2])

f = []
for i in range(11):
    if i%2 == 0 :
        z = i**2
        f.append(z)
# print(f)
g = [i*2 for i in range(15)]
# print(g)
h = [i**2 for i in range(11) if i%2 == 0]
# print(h)


#Sets {but no key value pairs} similar to list 1. Unordered 2. Unique Elements
j = {1,2,3,4,5,6,7,8}
k = {1,2,6,"laala", "haalala", "dalala" , "salalala"}
j.add(9)
j.remove(3)
# print(j)
# print(2 in j) # Works for List , Dictionaries , Sets
# print(j &k) #Intersect (Common elements)
# print(j.union(k)) # Union Connected but duplicate data is removed
# print(k.issubset(j))

#Strings
a = "rahuL"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.isalpha())
b = "89"
# print(b.isnumeric())
c = "   Rahul is trying to work harder  "
# print(c.replace("Rahul", "Situ"))
# print(c.strip())
# print(c.split())
d = "Rahul" , "Situ" , "Tushar" , "Shruti"
# print(d)
# print(",".join(d))

#Fromatting
l = 'Rahul'
f = 15
# print("Hello {1:.2f}, your number is {0}".format(l,f))



#Tuple - () 1.Immutable(Cannot be changed once fixed)
q = (1,2,3,4,5,6 ,7,8)
w = ("hululu" , "sululu" , "dululu", "mululu")

print(q +w)
print(q.index(6))






