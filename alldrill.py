import os
import shutil
import sqlite3
import tkinter
import time
from tkinter import *
from tkinter.filedialog import askdirectory


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)        
        self.master.resizable(width = False, height=False)
        self.master.geometry("425x160")
        self.master.title('Directory Drill')
        self.master.config(bg="#F9F7F6")

        self.sourceDir = StringVar()
        self.destDir = StringVar()

        self.btnSource = Button(self.master, text="Source", command=self.askdir, width=15 )
        self.btnSource.grid(row=0, column=0, padx=(10,0), pady=(20,0))

        self.txtDirect = Entry(self.master, text="", font=("Times New Roman", 16), fg="black", bg="white")
        self.txtDirect.grid(row=0, column=1, padx=(30,0), pady=(20,0))

        self.btnDestination = Button(self.master, text="Destination", command=self.askdir2, width=15 )
        self.btnDestination.grid(row=1, column=0, padx=(10,0), pady=(20,0))

        self.txtDirect2 = Entry(self.master,text="", font=("Times New Roman", 16), fg="black", bg="white")
        self.txtDirect2.grid(row=1, column=1, padx=(30,0), pady=(10,0))

        self.btnCheck = Button(self.master,text="Check for files...", command=self.get_filez, width=15, height=2)
        self.btnCheck.grid(row=2, column=1, padx=(10,0), pady=(10,0))
        

        

    def askdir(self):        
        direct = askdirectory()
        self.sourceDir = direct + '/'
        self.txtDirect.insert(INSERT,direct)        
        return direct



    def askdir2(self):        
        direct2 = askdirectory()
        self.destDir = direct2 + '/'
        self.txtDirect2.insert(INSERT,direct2)        
        return direct2


    def get_filez (self):      
        for file in os.listdir(self.sourceDir):
            if file.endswith(".txt"):
                print(file)
                abPath=os.path.join(self.sourceDir,file)
                print(abPath)
                modtime = time.ctime(os.path.getmtime(abPath))
                print(modtime)
                shutil.move(abPath, self.destDir)
                print ("Successfully moved {}".format(file))

        conn = sqlite3.connect("filedrill.db")

        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_filename TEXT, col_modtime DATETIME)")
            def data_entry():
                for file in os.listdir(self.destDir):
                    if file.endswith(".txt"):
                        abPath=os.path.join(self.destDir,file)
                        modtime = time.ctime(os.path.getmtime(abPath))
                        cur.execute("INSERT INTO tbl_files(col_filename, col_modtime) VALUES(?,?)", (file, modtime))
                        conn.commit()
            data_entry()

        conn.close()


        


if __name__ == "__main__":
    MyFrame().mainloop()

    
