import tkinter as tk


class Base_Frame:
    def __init__(self, master):
        self.tk_frame = tk.Frame(master)


class Frame_3Line(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
