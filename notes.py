import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notes:
    
    __root = Tk()

    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):

        try:
                self.__root.wm_iconbitmap("Notepad.ico") 
        except:
                pass

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        self.__root.title("Untitled - notes")

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFileMenu.add_command(label="Open",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save",command=self.__saveFile)
        self.__thisMenuBar.add_cascade(label="Files",menu=self.__thisFileMenu)

        self.__root.config(menu=self.__thisMenuBar)
def __quitApplication(self):
        self.__root.destroy()

    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - EditZ")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()
        
    def __newFile(self):
        self.__root.title("Nenumit - EditZ")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - Notes")
                            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def run(self):

        self.__root.mainloop()

notepad = Notes(width=600,height=400)

notepad.run()
