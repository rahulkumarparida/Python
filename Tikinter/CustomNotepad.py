from tkinter import *
import tkinter.filedialog

window = Tk()
window.title("Custom Notepad")
def NewFile():
    NewWindow = Toplevel(window)
    NotePadCreation(NewWindow)
    
    


def NotePadCreation(Window):

    menu = Menu(Window)
    TextFile = Text(Window)
    TextFile.grid(row=1 , column=2)

    def OpeningFile():
        var = tkinter.filedialog.askopenfilename()
        openFile = open(var ,"r")
        val = openFile.read()
        TextFile.delete("1.0" , END)
        TextFile.insert("1.0", val)
        openFile.close()

    def SavingFile():
        TextContent = TextFile.get("1.0" , END)
        var = tkinter.filedialog.asksaveasfilename( defaultextension=".txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")] )
        saveFile = open(var , "w+")
        saveFile.write(TextContent)
        saveFile.close()
        Window.destroy()
        

    class fileOne:
        def New():
            NewFile()
            print("New is Clicked")
        def NewWindow():
            print("NewWindow is Clicked")
        def Open():
            OpeningFile()
            print("Open is Clicked")               
        def Save():
            SavingFile()
            print("Save is Clicked")
        def Saveas():
            SavingFile()
        def Pagesetup():
            print("Pagesetup is Clicked")
        def Print():
            print("Print is Clicked")
        def Exit():
            return Window.destroy()




    file1 = Menu(menu , tearoff=0)
    file1.add_command(label="New", command=fileOne.New)
    file1.add_command(label="New Window" , command=fileOne.NewWindow)
    file1.add_command(label="Open...",command=fileOne.Open)
    file1.add_command(label="Save",command=fileOne.Save)
    file1.add_command(label="Save as",command=fileOne.Saveas)
    file1.add_separator()
    file1.add_command(label="Page setup...",command=fileOne.Pagesetup)
    file1.add_command(label="Print",command=fileOne.Print)
    file1.add_separator()
    file1.add_command(label="Exit",command=fileOne.Exit)


    file2 = Menu(menu , tearoff=0)
    file2.add_command(label="Undo")
    file2.add_separator()
    file2.add_command(label="Cut")
    file2.add_command(label="Copy")
    file2.add_command(label="Paste")
    file2.add_command(label="Delete")
    file2.add_separator()
    file2.add_command(label="Replace...")
    file2.add_command(label="GoTo..")
    file2.add_separator()
    file2.add_command(label="Select All")
    file2.add_command(label="Time/Date")



    file3 = Menu(menu , tearoff=0)
    file3.add_command(label="Word Wrap")
    file3.add_command(label="Font")


    file4 = Menu(menu , tearoff=0)
    file4.add_command(label="Zoom" )
    file4.add_command(label="Status Bar")


    file5 = Menu(menu , tearoff=0)
    file5.add_command(label="View Help" )
    file5.add_command(label="Send Feedback")
    file5.add_separator()
    file5.add_command(label="About Notepad")


    menu.add_cascade(label="File" , menu=file1)
    menu.add_cascade(label="Edit" , menu=file2) 
    menu.add_cascade(label="Format",menu=file3) 
    menu.add_cascade(label="View" , menu=file4) 
    menu.add_cascade(label="Help" , menu=file5) 
    Window.config(menu=menu, width=500 , height=600)
    
 
window.withdraw()

NewFile()




window.mainloop()