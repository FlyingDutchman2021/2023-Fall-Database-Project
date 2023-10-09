import tkinter as tk


class Entry:
    def __init__(self, master=None, **kwargs):
        self.content = tk.StringVar()
        self.entry = tk.Entry(master=master, **kwargs)

    def pack(self, **kwargs):
        self.entry.pack(kwargs)

