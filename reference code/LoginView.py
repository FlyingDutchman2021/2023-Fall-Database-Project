import tkinter as tk


class LoginView:
    def __init__(self, window, status, login_function):
        # Tracking
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()

        # Create Main Frame
        self.main_frame = tk.Frame(window)

        self.label_user_name = tk.Label(self.main_frame, text='User Name', font='Arial 20')
        self.label_user_name.pack(pady=8)

        self.entry_user_name = tk.Entry(self.main_frame, textvariable=self.user_name, font='Arial 20')
        self.entry_user_name.pack(pady=4)

        self.label_password = tk.Label(self.main_frame, text='Password', font='Arial 20')
        self.label_password.pack(pady=8)

        self.entry_password = tk.Entry(self.main_frame, textvariable=self.password, font='Arial 20', show='*')
        self.entry_password.pack(pady=4)

        self.button_login = tk.Button(self.main_frame, text='Login',
                                      command=lambda: self.login(status=status, login_function=login_function),
                                      font='Arial, 24', pady=8, padx=50)
        self.button_login.pack(pady=10)

    def show(self):
        self.main_frame.pack()

    def hide(self):
        self.main_frame.pack_forget()
        self.user_name.set('')
        self.password.set('')

    def login(self, status, login_function):
        if self.user_name.get() == 'admin' and self.password.get() == 'admin':
            status.pop()
            status.append('Admin')
            login_function()
        elif self.user_name.get() == 'teacher' and self.password.get() == 'ta006':
            status.pop()
            status.append('Teacher')
            login_function()
        else:
            status.pop()
            status.append('Student')
            login_function()
