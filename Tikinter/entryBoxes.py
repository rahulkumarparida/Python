from tkinter import *

window = Tk()

# label1 = Label(window , text="Mail" , bg="black" , fg="white")
# e1 = Entry(window , borderwidth=5 , bg="black" , fg="white")
# label2 = Label(window , text="Password" , bg="gray")
# e2 = Entry(window , borderwidth=5 , bg="gray")
# label1.grid(row=0,column=1)
# label2.grid(row=1,column=1)
# e1.grid(row=0,column=2)
# e2.grid(row=1,column=2)

# label3 = Label(window , text="label3" , bg="gray")
# label4 = Label(window , text="label4" , bg="aqua")
# label5 = Label(window , text="label5" , bg="red")
# label3.pack(side=TOP , fill=X , expand=False)
# label4.pack(side=LEFT , fill=Y , expand=False)
# label5.pack(side=BOTTOM , fill=X , expand=False)


def Loggin():
    print("Logged in Sucessfully")

button1 = Button(window , text="LogIn" , width=12 , height=4 , bg="aqua" , fg="green" , activebackground="green" , activeforeground="aqua" , command= Loggin)
button1.grid(row=2 , column=1)

window.geometry("200x500")
window.mainloop()
