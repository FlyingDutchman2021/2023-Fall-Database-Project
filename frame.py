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


# From Yangjun waiting for manual merge
class Sign_up_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame1 = tk.Frame(master)
        self.frame2 = tk.Frame(master)
        tk.Label(master=self.frame1, text="Choose your identity").pack()
        tk.Button(master=self.frame2, text="Patient").pack(side="left")
        tk.Button(master=self.frame2,text="Doctor").pack(side="left")
        self.frame1.pack()
        self.frame2.pack()

class Log_In_frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.account = tk.StringVar()
        self.password = tk.StringVar()
        self.frame1 = tk.Frame(master)
        self.frame2 = tk.Frame(master)
        self.frame3 = tk.Frame(master)

        tk.Label(master=self.frame1,text="Account").pack(side="left")
        tk.Entry(master=self.frame1, textvariable=self.account).pack(side="left")
        tk.Label(master=self.frame2, text="Password").pack(side="left")
        tk.Entry(master=self.frame2, textvariable=self.password).pack(side="left")
        tk.Button(master=self.frame3, text="Sign up").pack(side="left")
        tk.Button(master=self.frame3, text="Log in").pack(side="left")
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
