from  tkinter import *
window = Tk()

c = Canvas(window , width=600 , height=600)
c.pack()

c.create_line(0,0,600,600 , width=6 , fill="aqua" , dash=(3,3))
c.create_line(0,600,600,0 , width=6 , fill="green" , dash=(3,3))
c.create_line(0,300,600,300 , width=6 , fill="blue" , dash=(3,3))
c.create_line(300,600,300,0, width=6 , fill="red" , dash=(3,3))
c.create_rectangle(250 , 225, 350 ,375  , outline="aqua" , width=5)

window.mainloop()



