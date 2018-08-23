"""
TO DO:

main.py
    append text_message.py to main.py and delete text_message.py
    fix clickp() function in OCR.py to run the picture window like a browser to slect image
    give a more aesthetic look to the windows
    display appropriate error or affirmative messages
    Add a button to show the total amount spent in  the entire month
    correct the function naming in several instances, for ex: clickp has a collision with one of the OCR packages

"""



from OCR import final_image
from tkinter import *
from datetime import datetime as dt
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk
global Xpend

##Message Logic ##########################################################################

def mess(self):
    # Open the file with read only permit
    f = open('bank1.txt', "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    # close the file after reading the lines.
    amt1 = ''
    for i in lines:
        i = i.lower()

        if i.startswith('rs.'):
            for j in i:
                if not j.isalpha():
                    amt1 = amt1 + j
                    a = (amt1.split())
                    print(a[1])
                    for i in lines:
                        i = i.lower()
                        if i.find('debited') != -1:
                            (a[1]) = -float(a[1])
    print(float(a[1]))
    f.close()
    #change Xpnse to return the credited or debited amount and adjust accordingly in the calling function
    Xpnse = Xpnse + a[1]
    return Xpnse


######################End of message################################################



########################## OCR Text recognition ####################################

def textext(self):
  # Open the file with read only permit
  f = open('prctxt.txt', "r")
  # use readlines to read all lines in the file
  # The variable "lines" is a list containing all lines in the file
  lines = f.readlines()
  # close the file after reading the lines.

  amt1=''
  for i in lines:
     i = i.lower()

     if i.startswith('net amount '):
        for j in i:
            if not j.isalpha():
               amt1 = amt1 + j
  a=(amt1.split())
  print(a[1])
  Xpnse+=a[1]
  f.close()


############## End of textext ########################################################



class hello:
    def __init__(self):
        self.file1 = open('ords.txt', "a")
        self.root = tk.Tk()
        self.root.title("Finance")
        self.root = tk.Tk("Xpend")
        self.root.title("")
        #self.root.iconbitmap(self, default="images\icon.ico")
        self.topFrame=Frame(self.root)
        self.topFrame.pack()
        self.bottomFrame=Frame(self.root)
        self.bottomFrame.pack(side="bottom")
        self.mainp()
        self.root.mainloop()
    def but1fun(self):
         mamt = int(self.entryamt.get())
         mtag = self.entrytag.get()
         time = dt.now()
         text1 = str((mamt, mtag, time))
         self.file1.write(text1)
         self.label2 = Label(self.manualw, text="Transaction is successfully saved.")
         self.label2.grid(row=6, columnspan=3)
         self.file1.close()
    def manualp(self):
        self.manualw = Tk()
        #self.manualw.iconbitmap(self, default="images\icon.ico")
        label1 = Label(self.manualw, text="Enter the amount").grid(row=0)
        self.entryamt = Entry(self.manualw)
        self.entryamt.grid(row=0, column=1)
        label1 = Label(self.manualw, text="Enter the tag").grid(row=1)
        self.entrytag = Entry(self.manualw)
        self.entrytag.grid(row=1, column=1)
        self.bsubmit = Button(self.manualw, text="Enter into file", command=self.but1fun)
        self.bsubmit = ttk.Button(self.manualw, text="Enter into file", command=self.but1fun)
        self.bsubmit.grid(row=4, columnspan=3)
        # self.bclear=Button(self.manualw,text="Clear contents",command=self.file1.truncate(0))
        # self.bclear.grid(row=5,columnspan=3)
        self.manualw.mainloop()
    def clickp(self):
        self.clickw = Tk()
        pass
        self.clickw.mainloop()
        #self.clickw = Tk()
        file_path =str(askopenfilename())
        amt=final_image(str(file_path))
        label=Label(self.clickw,text=amt).grid(row=0)
        #self.clickw.mainloop()
    def msgp(self):
        #this functions will be improvied in a later build
        self.msgp = Tk()
        pass
        self.msgp.mainloop()
    def mainp(self):
        self.manualb = Button(self.root, text="Enter transaction manually", command=self.manualp)
        #this is the first window which displays as soon as the program runs
        self.manualb = ttk.Button(self.root, text="Enter transaction manually", command=self.manualp)
        self.manualb.pack()
        self.clickb = Button(self.root, text="Enter transaction by picture", command=self.clickp)
        self.clickb = ttk.Button(self.root, text="Enter transaction by picture", command=self.clickp)
        self.clickb.pack()
        self.msgb = Button(self.root, text="Enter transaction from messages", command=self.msgp)
        self.msgb.pack()
        #the following comments are commented out as it belongs to message reading which will be added on in a later build
        #self.msgb = Button(self.root, text="Enter transaction from messages", command=self.msgp)
        #self.msgb.pack()
if __name__ == '__main__':
    hello()

  

