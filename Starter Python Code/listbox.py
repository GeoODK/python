# simple example of a scrollable listbox for Tkinter
# for Python30 use 'import tkinter as tk'

import Tkinter as tk

root = tk.Tk()
root.title('a scrollable listbox')

# create the listbox (height/width in char)
listbox = tk.Listbox(root, width=50, height=20)
listbox.grid(row=0, column=0)

# create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky='n'+'s')
listbox.configure(yscrollcommand=yscroll.set)

# now load the listbox with data
friend_list = [
'Stew', 'Tom', 'Jen', 'Adam', 'Ethel', 'Barb', 'Tiny', 
'Tim', 'Pete', 'Sue', 'Egon', 'Swen', 'Albert']
for item in friend_list:
    # insert each new item to the end of the listbox
    listbox.insert('end', item)

# optionally scroll to the bottom of the listbox
lines = len(friend_list)
listbox.yview_scroll(lines, 'units')

root.mainloop()
