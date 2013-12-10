#!/usr/bin/env python

# TODO: This is lovely for showing an idea, but seriously, ugly.
# clean this up.

from Tkinter import *
from os import getenv
from os.path import join, exists
from sys import argv

args = argv[1:]
if args:
    clipboard_path = args[0]
else:
    clipboard_path = join(getenv("HOME"), "clipboard")

if not exists(clipboard_path):
    open(clipboard_path, "w")

def onclick():
   pass


def copy_to_clipboard():
    import pyperclip
    global txt_content
    val = txt_content.get(1.0,END)
    pyperclip.copy(val)



def save_content():
    global txt_content
    global clipboard_path

    with open(clipboard_path, "w") as output:
        output.write(txt_content.get(1.0, END))


def load_content():
    global txt_content
    global clipboard_path

    content = open(clipboard_path, "r").read()
    if content:
        txt_content.delete(1.0,END)
        txt_content.insert(INSERT, content)

root = Tk()
txt_content = Text(root)
txt_content.pack()

btn_copy = Button(root,text="Copy",command=copy_to_clipboard)
btn_copy.pack()

btn_save = Button(root,text="Save",command=save_content)
btn_save.pack()

btn_load = Button(root,text="Refresh",command=load_content)
btn_load.pack()

load_content()

root.mainloop()
