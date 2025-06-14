#Functional Programming
from operator import add

a = add
b =a(1,2)
# print(b)

def ad(i,j):
    return add(i,j)
# print(ad(2,2))

def fncAdd(i,j,fnc):
    return fnc(i,j)
# print(fncAdd(5,3,add))

#lamda Function
lamdafncMul = lambda a,b: a*b
# print(lamdafncMul(2,3))

#Filter
def even(a):
    return a%2== 0
b = [1,2,3,4,5,6,7,8,9,0]
# print(set(filter(even , b)))
# print(list(filter(lambda a:a%2==0,range(1,17)))) #Filiters by checking the condition is true and returns the value


#Map
def square(a):
    return a**2
b = [1,3,5,7,9,11]
# print(set(map(square , b)))
# print(list(map(lambda a:a**2,b)))#maps all the elements and performs function in all of them returns the value it found after performing


#Iterator

iteration = iter(range(1,15))
# print(iteration.__next__())#prints only one value
# print(list(iteration))#prints all

#Generator
def generate(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b
res = generate(100,20) #prints -- [[1,2,3,4,5,6,7,8,......19]]
# print(res.__next__())
# for re in res:
#     print(re)

def squareGenerator(a,b):
    f = range(a,b+1)
    yield list(map(lambda a : a**2,f))

g = squareGenerator(1,9)
for i in g:
    print(i)




