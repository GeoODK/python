import Tkinter, tkFileDialog, Tkconstants 
from Tkinter import * 
root = Tk() 
root.title('Watermark Image Processing 1.0b')
#Options for buttons
button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
 
#Define asking directory button
dirname = ''
def openDirectory():
	dirname = tkFileDialog.askdirectory(parent=root, initialdir='/home/', title='Select your pictures folder')
	print dirname
x = Button(root, text = 'Select your pictures folder', fg = 'black', command= openDirectory)
x.pack(**button_opt)
 
#Define asking watermark file button
fileName = ''
def openFile():
	fileName = tkFileDialog.askopenfile(parent=root,initialdir='/home/',title='Select your watermark file', filetypes=[('image files', '.png')])
Button(root, text = 'Select your watermark file', fg = 'black', command= openFile).pack(**button_opt)
 
root.mainloop()
