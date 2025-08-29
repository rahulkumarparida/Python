import socket
from tkinter import *

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
print(HOST_NAME)
PORT = 6969

s.bind((HOST_NAME,PORT))

s.listen(4)
client , address = s.accept()

def send(entry , listbox):
    msg = entry.get()
    listbox.insert('end',"Server: "+msg)
    client.send(bytes("Server: "+msg,'utf-8'))
    entry.delete(0,END)
    
def recive(listbox):
    recv = client.recv(50)
    print("User : ", recv.decode('utf-8'))
    listbox.insert('end', "Client: "+recv.decode('utf-8'))

root = Tk()
root.title("Server chat")

listbox = Listbox(root, width=60, height=20)
listbox.pack(padx=10, pady=10)

entry = Entry(root, width=50)
entry.pack(side=LEFT, padx=10, pady=10)

sendBtn = Button(root , text="Send" , command=lambda:send(entry ,listbox))
sendBtn.pack(side=BOTTOM)

recvBtn = Button(root , text="Recive" , command=lambda:recive(listbox))
recvBtn.pack(side=BOTTOM)

    
root.mainloop()
