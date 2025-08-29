import socket

from tkinter import *

s = socket.socket()
HOST_NAME = socket.gethostname()
PORT = 6969
s.connect((HOST_NAME, PORT))

def send(entry, listbox):
    msg = entry.get()
    listbox.insert('end', "Client: " + msg)
    s.send(bytes(msg, 'utf-8'))
    entry.delete(0, END)
    
    
def receive(listbox):
    recv = s.recv(100)
    listbox.insert('end', recv.decode('utf-8'))


root = Tk()
root.title("Client Chat")

listbox = Listbox(root, width=60, height=20)
listbox.pack(padx=10, pady=10)

entry = Entry(root, width=50)
entry.pack(side=LEFT, padx=10, pady=10)

sendBtn = Button(root, text="Send", command=lambda: send(entry, listbox))
sendBtn.pack(side=BOTTOM, padx=10, pady=10)

recvBtn = Button(root , text="Receive" , command=lambda:receive(listbox))
recvBtn.pack(side=BOTTOM, padx=10, pady=10)
root.mainloop()
