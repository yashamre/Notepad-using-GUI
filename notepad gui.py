from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)
    # 1-1st line
    # 0-0th character
    #Till end

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    # all types of files  
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file+"-Notepad"))
        TextArea.delete(1.0,END)
        f=open(file,"r")
        #deleting whatever was there originally 
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])

        if file=="":
            file=None
    
        else:
            #save as a new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

        root.title(os.path.basename(file)+"-Notepad")
        showinfo("Save File","File Saved Successfully")
    
    else:
        #save existing file
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))#inbuilt in tkinter handled by itself

def copy():
    TextArea.event_generate(("<<Copy>>"))
    
def paste():
    TextArea.event_generate(("<<Paste>>"))
    

def about():
    showinfo("Notepad using GUI","Notepad by: Yash Amre")

def darkTheme():
    # TextArea.tag_config("here",background="black")
    # Text.config(foreground="white", background='black')
    # pass
    TextArea.config(bg="#373737",fg="#FFFFFF",insertbackground="#FFFFFF")


def lightTheme():
    TextArea.config(bg="#FFFFFF",fg="#000000",insertbackground="#000000")

if __name__ == '__main__':
    #basic tkinter setup
    root = Tk()
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("download.ico")
    root.geometry("644x788")
    # root.mainloop()   

    #AddtextArea
    TextArea =Text(root, font="lucida 13")
    file=None
    #no file is opened initially
    TextArea.pack(expand=True,fill=BOTH)
    #fill-resizes in both x and y axes
    #expand-textarea occupies parent's width

    #creating menu bar
    MenuBar=Menu(root)
    
    
    #FILEMENU
    FileMenu =Menu(MenuBar,tearoff=0)
    #open new file
    FileMenu.add_command(label="New",command=newFile)
    #to open already existing file
    FileMenu.add_command(label="Open",command=openFile)
    #saves current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)#adding filemenu to menubar
    #FILEMENU


    #EDITMENU
    EditMenu =Menu(MenuBar,tearoff=0)
    #Cut
    EditMenu.add_command(label="Cut",command=cut)
    # Copy 
    EditMenu.add_command(label="Copy",command=copy)
    # paste 
    EditMenu.add_separator()
    EditMenu.add_command(label="Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)#adding editmenu to menubar
    #EDITMENU
   
    #HELPMENU
    HelpMenu =Menu(MenuBar,tearoff=0)
    # about 
    HelpMenu.add_command(label="About",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)#adding editmenu to menubar
    #HELPMENU


    #THEMEMENU
    ThemeMenu=Menu(MenuBar,tearoff=0) 
    ThemeMenu.add_command(label="Dark Theme",command=darkTheme)
    ThemeMenu.add_command(label="Light Theme",command=lightTheme)
    MenuBar.add_cascade(label="Theme",menu=ThemeMenu)
    #THEMEMENU  
   
    root.config(menu=MenuBar)

    #Scrollbar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    # Scroll.config(command=TextArea.xview)
    TextArea.config(yscrollcommand=Scroll.set)
    # TextArea.config(xscrollcommand=Scroll.set)
    root.mainloop()