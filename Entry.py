import tkinter as tk


class Entry:
    def __init__(self, master):
        self.content = tk.StringVar()
        self.entry = tk.Entry(master=master, textvariable=self.content)
        self.entry2 = tk.Entry(master=master)

    def pack(self):
        self.entry.pack()


