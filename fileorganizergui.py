import tkinter as tk
from tkinter import filedialog, Text
import os
from fileorganizer import organizer

folders = []

def add_folder():
    for widget in frame.winfo_children():
        widget.destroy()
    folder_name = filedialog.askdirectory(initialdir="/")
    folders.append(folder_name)
    for folder in folders:
        label = tk.Label(frame, text=folder, bg="gray")
        label.pack()


def organize():
    for path in folders:
        organize(path)



root = tk.Tk()

canvas = tk.Canvas(root, height=200, width=200, bg="#059329")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
open_folder = tk.Button(root, text="Open Folder", padx=10, pady=5, fg="white", bg="#059329", command=add_folder)
open_folder.pack()
organizer_folder = tk.Button(root, text="Organize", padx=10, pady=5, fg="white", bg="#059329")
organizer_folder.pack()

root.mainloop()



