import tkinter as tk
import tkinter.font
from tkinter import ttk

import config


class Base_Frame:
    def __init__(self, master):
        self.tk_frame = tk.Frame(master)


class Log_In_Frame(Base_Frame):

    def __init__(self, master):
        super().__init__(master)

        self.line = []
        self.entry = []

        for i in range(2):
            self.line.append(tk.StringVar())
            self.entry.append(ttk.Entry(master=self.tk_frame,
                                        textvariable=self.line[i]))
            self.entry[i].config(font=tkinter.font.Font(family=config.DEFAULT_FAMILY,
                                                        size=config.DEFAULT_SIZE))
            self.entry[i].pack(padx=10, pady=10, ipady=2)
