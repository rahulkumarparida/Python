from tkinter import *

window = Tk()

inp = Label(window , text="Hello World")

window.title("Learning Tkinter")
window.geometry("600x800")
window.config(bg="black" )


frame1 = Frame(window , bg="gray" , width=200 , height=300 , cursor="dot" , border="1", borderwidth="28")
frame2 = Frame(window , bg="blue" , width=200 , height=300 , cursor="dotbox" ,border="1", borderwidth="28")
button1 = Button(frame1 , bg="blue" , activebackground="red", text="Button")
button2 = Button(frame2 , bg="gray" , activebackground="orange", text="Button")

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
inp.pack(side= LEFT)    
button1.pack()
button2.pack()
window.mainloop()  