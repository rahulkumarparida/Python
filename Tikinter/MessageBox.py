from tkinter import *
import tkinter.messagebox

window = Tk()
window.geometry("800x600")
#Shows a dialog box with diffrent symbols and the message
# tkinter.messagebox.showinfo("Info" ," opened the box")
# tkinter.messagebox.showerror("Info" ,"There is a error in the code")
# tkinter.messagebox.showwarning("Info" ,"Warning whats happening")

# rain = tkinter.messagebox.askyesno("Weather" , "Will it Rain Today?")
# bug = tkinter.messagebox.askyesnocancel("Bug" , "Are the Bugs Resolved yet ?")
# tkinter.messagebox.askretrycancel("Error" , "There was an error trying.\n Should i try again ?")
# tkinter.messagebox.askquestion("Vote" , "Are you 18+ ?")

# if rain == True:
#     print("The trip to puri is cancelled.")

# if bug == False:
#     tkinter.messagebox.showerror("Bug Test","Bug not resolved yet , Try agin Try Harder")



#Part 2 : How to display in the window

# message = Message( window , text="Pyhton"  )
# message.pack()

# var = StringVar()
# message = Message(window , textvariable=var ,padx=20 , pady=20)
# var.set("Hello Sire")
# message.pack()

name = StringVar()
getVar = StringVar()
def getData():
    getD = getVar.get()
    name.set(getD)
msg2 = Message(window , textvariable=name  , relief=RAISED)
e1 = Entry(window , textvariable=getVar)
btn1 = Button(window, text="OK" , command=getData)

msg2.pack()
e1.pack()
btn1.pack()



#Checkcoxes

chk1 = Checkbutton(window ,text="Apple" , onvalue=1 , offvalue=0 , height=3 ,width=15)
chk2 = Checkbutton(window ,text="Mango" , onvalue=1 , offvalue=0 , height=3 ,width=15)
chk3 = Checkbutton(window ,text="Guava" , onvalue=1 , offvalue=0 , height=3 ,width=15)

chk1.place(x=250 , y=0)
chk2.place(x=250 , y=50)
chk3.place(x=250 , y=100)





window.mainloop()

