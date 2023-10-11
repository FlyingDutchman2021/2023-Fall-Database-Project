import tkinter as tk


class Base_Frame:
    def __init__(self, master):
        self.tk_frame = tk.Frame(master)


class Frame_3Line(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.line1 = tk.StringVar()
        self.line2 = tk.StringVar()
        self.line3 = tk.StringVar()

        tk.Entry(master=self.tk_frame, textvariable=self.line1).pack(side="left")
        tk.Entry(master=self.tk_frame, textvariable=self.line2).pack(side="left")
        tk.Entry(master=self.tk_frame, textvariable=self.line3).pack(side="left")
