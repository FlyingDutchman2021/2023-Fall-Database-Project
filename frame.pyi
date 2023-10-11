# class Frame_Basic:
#     def __init__(self, master):
#         self.frame = tk.Frame(master=master)
#
#
# class Frame_with_3_line(Frame_Basic):
#     def pack(self, *, after=..., **kw) -> None:
#         if kw:
#             print(kw)
#         self.frame.pack()
#
#     def __init__(self, master):
#         super().__init__(master)
#         self.line1 = tk.StringVar()
#         self.line2 = tk.StringVar()
#         self.line3 = tk.StringVar()
#
#         tk.Entry(master=self.frame, textvariable=self.line1).pack()
#         tk.Entry(master=self.frame, textvariable=self.line2).pack()
#         tk.Entry(master=self.frame, textvariable=self.line3).pack()
#
#         self.pack()
import tkinter as tk

class Base_Frame:
    def __init__(self, master):
        self.tk_frame = None

class Frame_3Line(Base_Frame):
    def __init__(self,
                 master: tk.Misc):
        self.line1 = None
        self.line2 = None
        self.line3 = None