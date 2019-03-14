from tkinter import *
from tkinter.filedialog import askdirectory


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.resizable(width = False, height=False)
        self.master.geometry("425x75")
        self.master.title('Ask Directory Drill')
        self.master.config(bg="#F9F7F6")

        self.button = Button(self.master, text="Select Directory", command=self.askdir, width=15 )
        self.button.grid(row=0, column=0, padx=(10,0), pady=(20,0))

        self.txtDirect = Entry(self.master, text="", font=("Times New Roman", 16), fg="black", bg="white")
        self.txtDirect.grid(row=0, column=1, padx=(30,0), pady=(20,0))

    def askdir(self):
        direct = askdirectory()
        self.txtDirect.insert(INSERT,direct)


        


if __name__ == "__main__":
    MyFrame().mainloop()



