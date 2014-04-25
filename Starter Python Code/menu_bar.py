# menu-example-3.py

from Tkinter import *
from tkMessageBox import *
from tkColorChooser import askcolor              
from tkFileDialog   import askopenfilename

root = Tk()

def hello():
    print "hello!"

def callback():
    filename = askopenfilename()
    return filename


menubar = Menu(root)
errmsg = 'Error!'
##listbox = Listbox(root,width=50)
##listbox.pack()

Button(text='Find', command=callback).pack(fill=X)
button1= Button(root, text='Clip',command=hello)
button1.pack(fill=X)

textBox1=Entry(root)
textBox1.pack()


# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu



# create a canvas
frame = Frame(root, width=512, height=512)
frame.pack()


root.config(menu=menubar)

mainloop()

