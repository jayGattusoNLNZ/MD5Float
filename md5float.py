import sys
import hashlib
if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *
from TkinterDnD2 import *

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def drop_a(event):
    my_file_hash = (md5(event.data.replace("{", "").replace("}", "")))
    text_a.delete('1.0', END)
    text_a.insert(END, event.data.replace("{", "").replace("}", ""))
    my_hash_sv_a.set("{}".format(my_file_hash ))
    set_check_colour()

def drop_b(event):
    my_file_hash = (md5(event.data.replace("{", "").replace("}", "")))
    text_b.delete('1.0', END)
    text_b.insert(END, event.data.replace("{", "").replace("}", ""))
    my_hash_sv_b.set("{}".format(my_file_hash ))
    set_check_colour()

def set_check_colour():
    if my_hash_sv_a.get() == my_hash_sv_b.get():
        check.configure(background="green")
    else:
        check.configure(background="red")

root = TkinterDnD.Tk()

my_hash_sv_a = StringVar()
my_hash_sv_b = StringVar()
my_hash_sv_a.set("")
my_hash_sv_b.set("")

text_a = Text(root, width=50, height=10)
text_a.insert(END,'Drop Here...')
my_hash_a = Entry(root, textvar=my_hash_sv_a, width=50)

text_b =  Text(root, width=50, height=10)
text_b.insert(END,'Drop Here...')
my_hash_b = Entry(root, textvar=my_hash_sv_b, width=50)

check = Frame(height=100, width=800, relief=SUNKEN, background="white")

text_a.grid( padx=10, pady=10, row=0, column=0)
text_b.grid(padx=10, pady=10, row=0, column=1)
my_hash_a.grid(padx=10, pady=10, row=1, column=0)
my_hash_b.grid( padx=10, pady=10, row=1, column=1)

check.grid(padx=10, pady=10, row=2, columnspan=2)

text_a.drop_target_register(DND_FILES)
text_b.drop_target_register(DND_FILES)
text_a.dnd_bind('<<Drop>>', drop_a)
text_b.dnd_bind('<<Drop>>', drop_b)

root.attributes('-topmost', 'true')

root.mainloop()
