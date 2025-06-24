from tkinter import *

window  = Tk()
window.geometry("500x600")
window.config(bg="gray")

e = Entry(window , width=50  , bg="black" , fg="white" , borderwidth=8 )
e.place(x=100 , y=50)

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result) + str(num))



b = Button(window , text="1" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black" , command=lambda:click(1))
b.place(x=80 , y=100)

b = Button(window , text="2" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=lambda:click(2))
b.place(x=200 , y=100)

b = Button(window , text="3" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=lambda:click(3))
b.place(x=320 , y=100)

b = Button(window , text="4" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=lambda:click(4))
b.place(x=80 , y=150)

b = Button(window , text="5" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=lambda:click(5))
b.place(x=200 , y=150)

b = Button(window , text="6" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=lambda:click(6))
b.place(x=320 , y=150)

b = Button(window , text="7" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=lambda:click(7))
b.place(x=80 , y=200)

b = Button(window , text="8" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=lambda:click(8))
b.place(x=200 , y=200)

b = Button(window , text="9" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=lambda:click(9))
b.place(x=320 , y=200)

b = Button(window , text="0" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=lambda:click(0))
b.place(x=80 , y=250)




      
def div():
    n1 = e.get()
    global math
    global i
    math = "div"
    i  = int(n1)
    e.delete(0,END)
    

b = Button(window , text="/" , width=10 , bg="black" , fg="white" ,activebackground="white" , activeforeground="black", command=div)
b.place(x=320 , y=250)
  
def mod():
    n1 = e.get()
    global math
    global i
    math = "mod"
    i  = int(n1)
    e.delete(0,END)

    
b = Button(window , text="%" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black" , command=mod)
b.place(x=200 , y=250)



def add():
    n1 = e.get()
    global math
    global i
    math = "add"
    i  = int(n1)
    e.delete(0,END)
    
    
b = Button(window , text="+" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black" , command=add)
b.place(x=80 , y=300 )

def sub():
    n1 = e.get()
    global math
    global i
    math = "sub"
    i  = int(n1)
    e.delete(0,END)
    

b = Button(window , text="-" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=sub)
b.place(x=200 , y=300)

def mul():
    n1 = e.get()
    global math
    global i
    math = "mul"
    i  = int(n1)
    e.delete(0,END)
    

b = Button(window , text="*" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=mul)
b.place(x=320 , y=300)


def equal():
    n2 = e.get()
    e.delete(0 , END)
    match math:
        case 'mod':
            e.insert(0,i % int(n2))    
        case 'add':
            e.insert(0,i + int(n2))    
        case 'sub':
            e.insert(0,i - int(n2))    
        case 'mul':
            e.insert(0,i * int(n2))    
        case 'div':
            e.insert(0,i / int(n2))    
        case _ :
            e.insert(0 , "NOT FOUND")
      

b = Button(window , text="=" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=equal)
b.place(x=80 , y=350)

def clear():
    e.delete(0,END)

b = Button(window , text="clear" , width=10 , bg="black" , fg="white" , activebackground="white" , activeforeground="black", command=clear)
b.place(x=200 , y=350)




window.mainloop()


