import tkinter as tk


class Frame_Basic:
    def __init__(self, master):
        self.frame = tk.Frame(master=master)


class Frame_with_3_line(Frame_Basic):
    def pack(self, *, after=..., **kw) -> None:
        if kw:
            print(kw)
        self.frame.pack()

    def __init__(self, master):
        super().__init__(master)
        self.line1 = tk.StringVar()
        self.line2 = tk.StringVar()
        self.line3 = tk.StringVar()

        tk.Entry(master=self.frame, textvariable=self.line1).pack()
        tk.Entry(master=self.frame, textvariable=self.line2).pack()
        tk.Entry(master=self.frame, textvariable=self.line3).pack()

        self.pack()


class MainWindow:
    def setup_main_window(self):
        full_width = self.window.winfo_screenwidth()
        full_height = self.window.winfo_screenheight()
        width_percentage = 0.82
        height_percentage = 0.79
        self.window.geometry(
            '%dx%d+%d+%d' % (full_width * width_percentage, full_height * height_percentage,
                             full_width * (1 - width_percentage) / 2,
                             full_height * ((1 - height_percentage) / 2 - 0.015)))
        self.window.title('This Is A Test')

    def __init__(self):
        self.window = tk.Tk()
        self.setup_main_window()

        self.frame1 = Frame_with_3_line(self.window)

        # Main loop
        self.window.mainloop()


main_window = MainWindow()
