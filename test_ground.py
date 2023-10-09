import tkinter as tk


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












        # Main loop
        self.window.mainloop()


main_window = MainWindow()
