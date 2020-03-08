import pyautogui, Pmw, sys
from tkinter import *
win=Tk()
win.geometry("600x600")
filename = "/Users/charlesetienne/git/screenCalipers/object_locations.txt"
xm=1
ym=0
Xoff=0
Yoff=0
top = Frame(win); top.pack(side='top')

location = Pmw.ScrolledText(top,
       borderframe=5, 
       vscrollmode='dynamic', 
       hscrollmode='dynamic',
       labelpos='n', 
       label_text='current location',
       text_width=30, 
       text_height=1,
       text_wrap='none',
       )
location.pack()

custom = Pmw.ScrolledText(top,
       borderframe=5, 
       vscrollmode='dynamic', 
       hscrollmode='dynamic',
       labelpos='n', 
       label_text='custom zero',
       text_width=30, 
       text_height=1,
       text_wrap='none',
       )
custom.pack()

textFile = Pmw.ScrolledText(top,
       borderframe=5, 
       vscrollmode='dynamic', 
       hscrollmode='dynamic',
       labelpos='n', 
       label_text='file %s' % filename,
       text_width=40, 
       text_height=30,
       text_wrap='none',
       )
textFile.pack()

def rezero(event):
    global Xoff
    global Yoff
    Xoff, Yoff = pyautogui.position()

def xy(event):
    global xm
    global ym 
    xm, ym = pyautogui.position()
    xy_data = "%d  %d" % (xm, ym)
    xy_cusdata = "%d  %d" % (xm-Xoff, ym-Yoff)
    location.delete("1.0", "end")
    location.insert('end', xy_data)
    custom.delete("1.0", "end")
    custom.insert('end', xy_cusdata)

    
def spacebar(event):
    f=open("object_locations.txt", "a+")
    f.write("%s   %s    \r\n\r\n" % (xm, ym))

def bigline(event):
    f=open("object_locations.txt", "a+")
    f.write("=" * 40 + "\r\n\r\n")

def refresh(event):
    textFile.insert('end', open(filename,'r').read())

win.bind("<space>", spacebar)
win.bind('r', rezero)
win.bind('l', refresh)
win.bind("s", bigline)
win.bind("<Motion>",xy)
mainloop()