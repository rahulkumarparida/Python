from tkinter import *

def send(entry , listbox):
    msg = entry.get()
    listbox.insert('end',msg)
root = Tk()



listbox = Listbox(root)
listbox.pack()

entry = Entry()
entry.pack()

sendBtn = Button(root , text="Send" , command=lambda:send(entry ,listbox))
sendBtn.pack(side=BOTTOM)




root.mainloop()

