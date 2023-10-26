import customtkinter as ctk


class Base_Frame:
    def __init__(self, master):
        self.tk_frame = ctk.CTkFrame(master)
        self.tk_frame.pack(fill="both", expand=True)

    def switch_Log_In(self):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Log_In_Frame(self.tk_frame)

    def switch_Sign_Up(self):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Sign_up_Frame(self.tk_frame)

    def switch_Sign_Up_Patient(self):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Sign_up_Patient_Frame(self.tk_frame)

    def switch_Sign_Up_Doctor(self):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Sign_up_Doctor_Frame(self.tk_frame)


class Log_In_Frame(Base_Frame):

    def __init__(self, master):
        super().__init__(master)

        self.account = ctk.StringVar()
        self.password = ctk.StringVar()
        self.frame = ctk.CTkFrame(self.tk_frame)

        ctk.CTkLabel(master=self.frame, text='Phone Number').grid(row=0, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.account, width=200).grid(row=0, column=1, columnspan=2,
                                                                                   padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, width=200).grid(row=1, column=1, columnspan=2,
                                                                                    padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Log in", width=10).grid(row=2, column=1, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Sign up", width=10, command=lambda: self.switch_Sign_Up()).grid(row=2,
                                                                                                               column=2,
                                                                                                               padx=10,
                                                                                                               pady=12)
        self.frame.pack()


class Sign_up_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame = ctk.CTkFrame(self.tk_frame)

        ctk.CTkLabel(master=self.frame, text="Choose your identity", width=200).grid(
            row=0, column=0, columnspan=3, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Patient", width=10, command=lambda: self.switch_Sign_Up_Patient()).grid(
            row=1, column=0, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Doctor", width=10, command=lambda: self.switch_Sign_Up_Doctor()).grid(
            row=1, column=2, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.switch_Log_In()).grid(
            row=2, column=1, padx=10, pady=12)
        self.frame.pack()

class Sign_up_Patient_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name = ctk.StringVar()
        self.birthday_year = ctk.StringVar()
        self.birthday_month = ctk.StringVar()
        self.birthday_day = ctk.StringVar()
        self.gender = ctk.StringVar()
        self.contact_number = ctk.StringVar()
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.frame = self.frame = ctk.CTkFrame(self.tk_frame)
        self.year = []
        self.month = []
        self.day = []
        for i in range(100):
            self.year.append((str)(1930+i))
        for i in range(12):
            self.month.append((str)(1+i))
        for i in range(31):
            self.day.append((str)(1+i))


        ctk.CTkLabel(master=self.frame, text="Please enter your message", width=200).grid(
            row=0, column=0, columnspan=4, padx=10, pady=12)

        ctk.CTkLabel(master=self.frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Re-enter Password').grid(row=6, column=0, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkComboBox(master=self.frame, variable=self.birthday_year, values=self.year, width=80).grid(
            row=2, column=1, padx=10, pady=12)
        ctk.CTkComboBox(master=self.frame, variable=self.birthday_month, values=self.month, width=80).grid(
            row=2, column=2, padx=10, pady=12)
        ctk.CTkComboBox(master=self.frame, variable=self.birthday_day, values=self.day, width=80).grid(
            row=2, column=3, padx=10, pady=12)


        ctk.CTkRadioButton(master=self.frame,text="male", variable=self.gender, value=True).grid(
            row=3, column=2, padx=10, pady=12)
        ctk.CTkRadioButton(master=self.frame, text="female", variable=self.gender, value=True).grid(
            row=3, column=3, padx=10, pady=12)


        ctk.CTkEntry(master=self.frame, textvariable=self.contact_number, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, show = '*', width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password_, show = '*', width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)


        ctk.CTkButton(master=self.frame, text="Finish", width=5, command=lambda: self.Password_confirmation()).grid(
            row=7, column=1, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.switch_Sign_Up()).grid(
            row=7, column=2, padx=10, pady=12)
        self.frame.pack()

    def Password_confirmation(self):
        if (self.password.get() == self.password_.get()):
            ctk.CTkLabel(master=self.frame, text='Pass').grid(row=6, column=4, padx=10, pady=12)
            self.switch_Log_In()
        else:
            ctk.CTkLabel(master=self.frame, text='Fail').grid(row=6, column=4, padx=10, pady=12)


class Sign_up_Doctor_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name = ctk.StringVar()
        self.birthday_year = ctk.StringVar()
        self.birthday_month = ctk.StringVar()
        self.birthday_day = ctk.StringVar()
        self.gender = ctk.StringVar()
        self.contact_number = ctk.StringVar()
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.frame = self.frame = ctk.CTkFrame(self.tk_frame)
        self.year = []
        self.month = []
        self.day = []
        for i in range(100):
            self.year.append((str)(1930+i))
        for i in range(12):
            self.month.append((str)(1+i))
        for i in range(31):
            self.day.append((str)(1+i))


        ctk.CTkLabel(master=self.frame, text="Please enter your message", width=200).grid(
            row=0, column=0, columnspan=4, padx=10, pady=12)

        ctk.CTkLabel(master=self.frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Re-enter Password').grid(row=6, column=0, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkComboBox(master=self.frame, variable=self.birthday_year, values=self.year, width=80).grid(
            row=2, column=1, padx=10, pady=12)
        ctk.CTkComboBox(master=self.frame, variable=self.birthday_month, values=self.month, width=80).grid(
            row=2, column=2, padx=10, pady=12)
        ctk.CTkComboBox(master=self.frame, variable=self.birthday_day, values=self.day, width=80).grid(
            row=2, column=3, padx=10, pady=12)


        ctk.CTkRadioButton(master=self.frame,text="male", variable=self.gender, value=True).grid(
            row=3, column=2, padx=10, pady=12)
        ctk.CTkRadioButton(master=self.frame, text="female", variable=self.gender, value=True).grid(
            row=3, column=3, padx=10, pady=12)


        ctk.CTkEntry(master=self.frame, textvariable=self.contact_number, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, show = '*', width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password_, show = '*', width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)


        ctk.CTkButton(master=self.frame, text="Finish", width=5, command=lambda: self.Password_confirmation()).grid(
            row=7, column=1, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.switch_Sign_Up()).grid(
            row=7, column=2, padx=10, pady=12)
        self.frame.pack()

    def Password_confirmation(self):
        if (self.password.get() == self.password_.get()):
            ctk.CTkLabel(master=self.frame, text='Pass').grid(row=6, column=4, padx=10, pady=12)
            self.switch_Log_In()
        else:
            ctk.CTkLabel(master=self.frame, text='Fail').grid(row=6, column=4, padx=10, pady=12)
