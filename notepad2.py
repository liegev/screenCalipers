import pyautogui, Pmw, sys, os
from tkinter import *
win=Tk()
win.geometry("400x1000+2040+106")
filename = "/Users/charlesetienne/git/screenCalipers/notes.txt"
top = Frame(win); top.pack(side='top')

instruct = Label(win, 
text='my simple notepad')
instruct.pack()



textFile = Pmw.ScrolledText(top,
       borderframe=5, 
       vscrollmode='dynamic', 
       hscrollmode='dynamic',
       labelpos='n', 
       label_text='saved locations',
       text_width=50, 
       text_height=60,
       text_wrap='none',
       )
textFile.pack()




def deletefile(event):
    os.remove(filename)
    f=open(filename, "a+")

def bigline(event):
    f=open(filename, "a+")
    f.write("=" * 40 + "\r\n\r\n")

def refresh(event):
    textFile.delete("1.0", "end") 
    textFile.insert('end', open(filename,'r').read())

# win.bind("<space>", spacebar)
# win.bind('r', rezero)
# win.bind('l', refresh)
# win.bind("s", bigline)
# win.bind('d', deletefile)
mainloop()