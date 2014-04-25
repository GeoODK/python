import os
from Tkinter import *
from tkMessageBox import *
from tkFileDialog   import askopenfilename, askdirectory

def dir_browser():
    dirname = askdirectory(initialdir='~')
    input_entry.insert(END,dirname)

def run_program():    
    directory = input_entry.get()
    os.chdir(directory)
    name=rename_entry.get()

    count=0
    for filename in os.listdir('./'):
        os.rename(filename,name+str(count)+'.JPG')
        print filename
        count=count+1


    
root=Tk()
root.title('Renaming JPG')
root.resizable(width=FALSE, height=FALSE)
root.geometry('538x365+100+100')

header= Label(root, text="Rename", font=('Arial', 30 ,'bold'), anchor="center")
header.grid(column=0,row=0,pady=5,padx=5)


inputfile_button= Button(text='Input File', command=dir_browser,width=20)
inputfile_button.grid(column=0,row=1,pady=5,padx=5)

input_entry= Entry(root,width=50)
input_entry.grid(column=1,row=1,pady=30,padx=5)

rename_label=Label(root, text="Rename As: ")
rename_label.grid(column=0,row=2,pady=5,padx=5)

rename_entry=Entry(root,width=50)
rename_entry.grid(column=1,row=2,pady=5,padx=5)

run_button = Button(text='Run',font=('Arial', 15 ,'bold'), command=run_program, width=2, height=2)
run_button.grid(column=1,row=3,pady=4,ipadx=40)

root.mainloop()

