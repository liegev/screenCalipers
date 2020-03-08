from tkinter import *
import Pmw, sys
filename = "/Users/charlesetienne/git/screenCalipers/object_locations.txt"
root = Tk()            
top = Frame(root); top.pack(side='top')
text = Pmw.ScrolledText(top,
       borderframe=5, 
       vscrollmode='dynamic', 
       hscrollmode='dynamic',
       labelpos='n', 
       label_text='file %s' % filename,
       text_width=40, 
       text_height=60,
       text_wrap='none',
       )
text.pack()

text.insert('end', open(filename,'r').read())
Button(top, text='Quit', command=root.destroy).pack(pady=15)
root.mainloop()

   