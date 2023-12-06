import customtkinter as ctk
from tkinter import messagebox, ttk
import sql_request


class Base_Frame:
    def __init__(self, master):
        self.tk_frame = ctk.CTkFrame(master)
        self.tk_frame.pack(fill="both", expand=True)

    def switch_Log_In(self, identity):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Log_In_Frame(self.tk_frame, identity)

    def switch_Sign_Up_Patient(self):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Sign_up_Patient_Frame(self.tk_frame)

    def switch_Sign_Up_Doctor(self):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Sign_up_Doctor_Frame(self.tk_frame)

    def switch_Sign_Up_Nurse(self):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Sign_up_Nurse_Frame(self.tk_frame)

    def switch_Patient(self, id):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Patient_Frame(self.tk_frame, id)

    def switch_Doctor(self, id):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Doctor_Frame(self.tk_frame,id)

    def switch_Nurse(self, id):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Nurse_Frame(self.tk_frame, id)


class Identity_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame = ctk.CTkFrame(self.tk_frame)

        ctk.CTkLabel(master=self.frame, text="Choose your identity", width=200).grid(
            row=0, column=0, columnspan=3, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Patient", width=10, command=lambda: self.Log_In("patient")).grid(
            row=1, column=0, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Doctor", width=10, command=lambda: self.Log_In("doctor")).grid(
            row=1, column=1, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Nurse", width=10, command=lambda: self.Log_In("nurse")).grid(
            row=1, column=2, padx=10, pady=12)

        self.frame.pack()

    def Log_In(self, identity):
        self.switch_Log_In(identity)


class Log_In_Frame(Base_Frame):

    def __init__(self, master, identity: str):
        super().__init__(master)

        self.identity = identity
        self.account = ctk.StringVar()
        self.password = ctk.StringVar()
        self.frame = ctk.CTkFrame(self.tk_frame)

        ctk.CTkLabel(master=self.frame, text='Account').grid(row=0, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.account, width=200).grid(
            row=0, column=1, columnspan=2, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, width=200).grid(
            row=1, column=1, columnspan=2, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Log in", width=10, command=lambda: self.Log_in()).grid(
            row=2, column=1, padx=10, pady=12)

        ctk.CTkButton(master=self.frame, text="Sign up", width=10, command=lambda: self.Sign_up()).grid(
            row=2, column=2, padx=10, pady=12)

        self.frame.pack()

    def Log_in(self):
        status, id = sql_request.login(str(self.account.get()), str(self.password.get()), self.identity)
        if status == 'Success':
            if self.identity == "patient":
                self.switch_Patient(id)
            if self.identity == "doctor":
                self.switch_Doctor(id)
            if self.identity == "nurse":
                self.switch_Nurse(id)
        else:
            messagebox.showerror('Error', status)


    def Sign_up(self):
        if self.identity == "patient":
            self.switch_Sign_Up_Patient()
        if self.identity == "doctor":
            self.switch_Sign_Up_Doctor()
        if self.identity == "nurse":
            self.switch_Sign_Up_Nurse()


class Sign_up_Patient_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name = ctk.StringVar()
        self.birthday = ctk.StringVar()
        self.birthday_year = ctk.StringVar()
        self.birthday_month = ctk.StringVar()
        self.birthday_day = ctk.StringVar()
        self.gender = ctk.StringVar()
        self.contact_number = ctk.StringVar()
        self.email = ctk.StringVar()
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.Label = ctk.StringVar()
        self.frame = ctk.CTkFrame(self.tk_frame)
        self.year = []
        self.month = []
        for i in range(100):
            self.year.append(str(1930 + i))
        for i in range(12):
            self.month.append(str(1 + i))

        ctk.CTkLabel(master=self.frame, text="Please enter your message", width=200).grid(
            row=0, column=0, columnspan=4, padx=10, pady=12)

        ctk.CTkLabel(master=self.frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Email').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=6, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Re-enter Password').grid(row=7, column=0, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkComboBox(master=self.frame, variable=self.birthday_year, values=self.year, width=80).grid(
            row=2, column=1, padx=10, pady=12)
        ctk.CTkComboBox(master=self.frame, variable=self.birthday_month, values=self.month, width=80).grid(
            row=2, column=2, padx=10, pady=12)
        self._day = ctk.CTkComboBox(master=self.frame, variable=self.birthday_day, width=80)
        self._day.grid(row=2, column=3, padx=10, pady=12)
        self.birthday_month.trace_add("write", self.show_day)
        self.birthday_year.trace_add("write", self.show_day)

        ctk.CTkRadioButton(master=self.frame, text="male", variable=self.gender, value=True).grid(
            row=3, column=2, padx=10, pady=12)
        ctk.CTkRadioButton(master=self.frame, text="female", variable=self.gender, value=True).grid(
            row=3, column=3, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.contact_number, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.email, width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, show='*', width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password_, show='*', width=300).grid(
            row=7, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, textvariable=self.Label, width=5).grid(
            row=7, column=4, padx=10, pady=12)
        self.password.trace_add("write", self.Password_confirmation)
        self.password_.trace_add("write", self.Password_confirmation)

        ctk.CTkButton(master=self.frame, text="Finish", width=5, command=lambda: self.Password_confirmation()).grid(
            row=8, column=1, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.switch_Log_In("Patient")).grid(
            row=8, column=3, padx=10, pady=12)
        self.frame.pack()

    def Password_confirmation(self, *args):
        self.Label.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label.set('Pass')
            else:
                self.Label.set('Fail')

    def show_day(self, *args):
        self._day.set('')
        day = []
        if self.birthday_month.get() != '' and self.birthday_year.get() != '':
            month = int(self.birthday_month.get())
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                for i in range(31):
                    day.append(str(1 + i))
            elif month != 2:
                for i in range(30):
                    day.append(str(1 + i))
            else:
                year = int(self.birthday_year.get())
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    for i in range(29):
                        day.append(str(1 + i))
                else:
                    for i in range(28):
                        day.append(str(1 + i))
            self._day.configure(values=day)


class Sign_up_Doctor_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name = ctk.StringVar()
        self.birthday = ctk.StringVar()
        self.birthday_year = ctk.StringVar()
        self.birthday_month = ctk.StringVar()
        self.birthday_day = ctk.StringVar()
        self.gender = ctk.StringVar()
        self.contact_number = ctk.StringVar()
        self.email = ctk.StringVar()
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.Label = ctk.StringVar()
        self.frame = ctk.CTkFrame(self.tk_frame)
        self.year = []
        self.month = []
        for i in range(100):
            self.year.append(str(1930 + i))
        for i in range(12):
            self.month.append(str(1 + i))

        ctk.CTkLabel(master=self.frame, text="Please enter your message", width=200).grid(
            row=0, column=0, columnspan=4, padx=10, pady=12)

        ctk.CTkLabel(master=self.frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Email').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=6, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Re-enter Password').grid(row=7, column=0, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkComboBox(master=self.frame, variable=self.birthday_year, values=self.year, width=80).grid(
            row=2, column=1, padx=10, pady=12)
        ctk.CTkComboBox(master=self.frame, variable=self.birthday_month, values=self.month, width=80).grid(
            row=2, column=2, padx=10, pady=12)
        self._day = ctk.CTkComboBox(master=self.frame, variable=self.birthday_day, width=80)
        self._day.grid(row=2, column=3, padx=10, pady=12)
        self.birthday_month.trace_add("write", self.show_day)
        self.birthday_year.trace_add("write", self.show_day)

        ctk.CTkRadioButton(master=self.frame, text="male", variable=self.gender, value=True).grid(
            row=3, column=2, padx=10, pady=12)
        ctk.CTkRadioButton(master=self.frame, text="female", variable=self.gender, value=True).grid(
            row=3, column=3, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.contact_number, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.email, width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, show='*', width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password_, show='*', width=300).grid(
            row=7, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, textvariable=self.Label, width=20).grid(
            row=7, column=4, padx=10, pady=12)
        self.password.trace_add("write", self.Password_confirmation)
        self.password_.trace_add("write", self.Password_confirmation)

        ctk.CTkButton(master=self.frame, text="Finish", width=5, command=lambda: self.Password_confirmation()).grid(
            row=8, column=1, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.switch_Log_In("Patient")).grid(
            row=8, column=3, padx=10, pady=12)
        self.frame.pack()

    def Password_confirmation(self, *args):
        self.Label.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label.set('Pass')
            else:
                self.Label.set('Fail')

    def show_day(self, *args):
        self._day.set('')
        day = []
        if self.birthday_month.get() != '' and self.birthday_year.get() != '':
            month = int(self.birthday_month.get())
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                for i in range(31):
                    day.append(str(1 + i))
            elif month != 2:
                for i in range(30):
                    day.append(str(1 + i))
            else:
                year = int(self.birthday_year.get())
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    for i in range(29):
                        day.append(str(1 + i))
                else:
                    for i in range(28):
                        day.append(str(1 + i))
            self._day.configure(values = day)


class Sign_up_Nurse_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name = ctk.StringVar()
        self.birthday = ctk.StringVar()
        self.birthday_year = ctk.StringVar()
        self.birthday_month = ctk.StringVar()
        self.birthday_day = ctk.StringVar()
        self.gender = ctk.StringVar()
        self.contact_number = ctk.StringVar()
        self.email = ctk.StringVar()
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.Label = ctk.StringVar()
        self.frame = ctk.CTkFrame(self.tk_frame)
        self.year = []
        self.month = []
        for i in range(100):
            self.year.append(str(1930 + i))
        for i in range(12):
            self.month.append(str(1 + i))

        ctk.CTkLabel(master=self.frame, text="Please enter your message", width=200).grid(
            row=0, column=0, columnspan=4, padx=10, pady=12)

        ctk.CTkLabel(master=self.frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Email').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=6, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Re-enter Password').grid(row=7, column=0, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkComboBox(master=self.frame, variable=self.birthday_year, values=self.year, width=80).grid(
            row=2, column=1, padx=10, pady=12)
        ctk.CTkComboBox(master=self.frame, variable=self.birthday_month, values=self.month, width=80).grid(
            row=2, column=2, padx=10, pady=12)
        self._day = ctk.CTkComboBox(master=self.frame, variable=self.birthday_day, width=80)
        self._day.grid(row=2, column=3, padx=10, pady=12)

        self.birthday_month.trace_add("write", self.show_day)
        self.birthday_year.trace_add("write", self.show_day)

        ctk.CTkRadioButton(master=self.frame, text="male", variable=self.gender, value=True).grid(
            row=3, column=2, padx=10, pady=12)
        ctk.CTkRadioButton(master=self.frame, text="female", variable=self.gender, value=True).grid(
            row=3, column=3, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.contact_number, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.email, width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, show='*', width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password_, show='*', width=300).grid(
            row=7, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, textvariable=self.Label, width=5).grid(
            row=7, column=4, padx=10, pady=12)

        self.password.trace_add("write", self.Password_confirmation)
        self.password_.trace_add("write", self.Password_confirmation)

        ctk.CTkButton(master=self.frame, text="Finish", width=5, command=lambda: self.Password_confirmation()).grid(
            row=8, column=1, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.switch_Log_In("Patient")).grid(
            row=8, column=3, padx=10, pady=12)
        self.frame.pack()

    def Password_confirmation(self, *args):
        self.Label.set('')
        if  self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label.set('Pass')
            else:
                self.Label.set('Fail')

    def show_day(self, *args):
        self._day.set('')
        day = []
        if self.birthday_month.get() != '' and self.birthday_year.get() != '':
            month = int(self.birthday_month.get())
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                for i in range(31):
                    day.append(str(1 + i))
            elif month != 2:
                for i in range(30):
                    day.append(str(1 + i))
            else:
                year = int(self.birthday_year.get())
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    for i in range(29):
                        day.append(str(1 + i))
                else:
                    for i in range(28):
                        day.append(str(1 + i))
            self._day.configure(values=day)


class Patient_Frame(Base_Frame):
    def __init__(self, master, id):
        super().__init__(master)

        self.id = id
        self.frame1 = ctk.CTkFrame(self.tk_frame)
        self.frame2 = ctk.CTkFrame(self.tk_frame)
        Info = sql_request.get_personal_info(self.id, 'patient')

        self.name = ctk.StringVar()
        self.name.set(Info[2])
        self.birthday = ctk.StringVar()
        self.birthday.set(Info[4])
        self.birthday_year = ctk.StringVar()
        self.birthday_month = ctk.StringVar()
        self.birthday_day = ctk.StringVar()
        self.birthday_year.set(str(int(int(self.birthday.get()) / 10000)))
        self.birthday_month.set(str(int(int(self.birthday.get()) %10000 /100)))
        self.birthday_day.set(str(int(int(self.birthday.get()) %10000 %100 /1)))
        self.gender = ctk.StringVar()
        self.gender.set(Info[3])
        self.contact_number = ctk.StringVar()
        self.contact_number.set(Info[6])
        self.email = ctk.StringVar()
        self.email.set(Info[1])
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.password_entry = ctk.StringVar()
        self.Label1 = ctk.StringVar()
        self.Label2 = ctk.StringVar()

        self.year = []
        self.month = []
        for i in range(100):
            self.year.append(str(1930 + i))
        for i in range(12):
            self.month.append(str(1 + i))


        ctk.CTkLabel(master=self.frame1, text=self.id).pack(padx=10, pady=12)
        ctk.CTkLabel(master=self.frame1, textvariable=self.name).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="My medical records", width=5, command=lambda: self.Attendance_records()).pack(
            padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Personal Information", width=5, command=lambda: self.Personal_Information()).pack(
            padx=10, pady=12)

        self.frame1.pack(side='left', padx=10, fill='y')
        self.frame2.pack(side='left', padx=10, fill='both', expand="yes")

    def Attendance_records(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        tree = ttk.Treeview(frame, show="headings")
        tree["columns"] = ("Time", "Doctor", "Content")
        tree.column("Time", width=100,anchor='center')
        tree.column("Doctor", width=100,anchor='center')
        tree.column("Content", width=500,anchor='center')
        tree.heading("Time", text="Time")
        tree.heading("Doctor", text="Doctor")
        tree.heading("Content", text="Content")
        tree.insert("",0,values=("20231205","Mr.1","111111111"))
        tree.pack()

    def Personal_Information(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        frame3 = ctk.CTkFrame(self.frame2)

        ctk.CTkLabel(master=frame3, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Email').grid(row=5, column=0, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.birthday_year, width=80).grid(
            row=2, column=1, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.birthday_month, width=80).grid(
            row=2, column=2, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.birthday_day, width=80).grid(
            row=2, column=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.gender, width=300).grid(
            row=3, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.contact_number, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.email, width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkButton(master=frame3, text='Modify',command=lambda: self.Password_()).grid(
            row=6, column=2, padx=10, pady=12)

        frame3.pack(expand="yes")

    def Password_(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        ctk.CTkLabel(master=frame, text='Please enter your password').pack()
        ctk.CTkEntry(master=frame, textvariable=self.password_entry, width=300).pack()
        ctk.CTkLabel(master=frame, textvariable=self.Label1, width=5).pack()
        self.password_entry.trace_add("write", self.Modify)


    def Modify(self,*args):
        self.Label1.set('')
        if self.password_entry.get() != '':
            if self.password_entry.get() == "123456789":
                for widget in self.frame2.winfo_children():
                    widget.destroy()
                frame = ctk.CTkFrame(self.frame2)
                frame.pack(expand="yes")

                ctk.CTkLabel(master=frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Email').grid(row=5, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Password').grid(row=6, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Re-enter Password').grid(row=7, column=0, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.name, width=300).grid(
                    row=1, column=1, columnspan=3, padx=10, pady=12)

                ctk.CTkComboBox(master=frame, variable=self.birthday_year, values=self.year, width=80).grid(
                    row=2, column=1, padx=10, pady=12)
                ctk.CTkComboBox(master=frame, variable=self.birthday_month, values=self.month, width=80).grid(
                    row=2, column=2, padx=10, pady=12)
                self._day = ctk.CTkComboBox(master=frame, variable=self.birthday_day, width=80)
                self._day.grid(row=2, column=3, padx=10, pady=12)
                self.birthday_month.trace_add("write", self.show_day)
                self.birthday_year.trace_add("write", self.show_day)

                ctk.CTkRadioButton(master=frame, text="male", variable=self.gender, value=True).grid(
                    row=3, column=2, padx=10, pady=12)
                ctk.CTkRadioButton(master=frame, text="female", variable=self.gender, value=True).grid(
                    row=3, column=3, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.contact_number, width=300).grid(
                    row=4, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.email, width=300).grid(
                    row=5, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password, show='*', width=300).grid(
                    row=6, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password_, show='*', width=300).grid(
                    row=7, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkLabel(master=frame, textvariable=self.Label2, width=5).grid(
                    row=7, column=4, padx=10, pady=12)
                self.password.trace_add("write", self.Password_confirmation)
                self.password_.trace_add("write", self.Password_confirmation)

                ctk.CTkButton(master=frame, text="Finish", width=5, command=lambda: self.Password_confirmation()).grid(
                    row=8, column=1, padx=10, pady=12)
                ctk.CTkButton(master=frame, text="Back", width=5, command=lambda: self.Personal_Information()).grid(
                    row=8, column=3, padx=10, pady=12)
            else:
                self.Label1.set('The password is wrong')


    def show_day(self, *args):
        self._day.set('')
        day = []
        if self.birthday_month.get() != '' and self.birthday_year.get() != '':
            month = int(self.birthday_month.get())
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                for i in range(31):
                    day.append(str(1 + i))
            elif month != 2:
                for i in range(30):
                    day.append(str(1 + i))
            else:
                year = int(self.birthday_year.get())
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    for i in range(29):
                        day.append(str(1 + i))
                else:
                    for i in range(28):
                        day.append(str(1 + i))
            self._day.configure(values=day)

    def Password_confirmation(self, *args):
        self.Label2.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label2.set('Pass')
            else:
                self.Label2.set('Fail')


class Doctor_Frame(Base_Frame):
    def __init__(self, master, id):
        super().__init__(master)

        self.id = id
        self.frame1 = ctk.CTkFrame(self.tk_frame)
        self.frame2 = ctk.CTkFrame(self.tk_frame)
        Info = sql_request.get_personal_info(self.id, 'doctor')

        self.name = ctk.StringVar()
        self.name.set(Info[2])
        self.birthday = ctk.StringVar()
        self.birthday_year = ctk.StringVar()
        self.birthday_month = ctk.StringVar()
        self.birthday_day = ctk.StringVar()
        self.gender = ctk.StringVar()
        self.gender.set(Info[3])
        self.contact_number = ctk.StringVar()
        self.contact_number.set(Info[4])
        self.email = ctk.StringVar()
        self.email.set(Info[1])
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.password_entry = ctk.StringVar()
        self.department = ctk.StringVar()
        self.department.set(Info[5])
        self.Label1 = ctk.StringVar()
        self.Label2 = ctk.StringVar()

        self.year = []
        self.month = []
        for i in range(100):
            self.year.append(str(1930 + i))
        for i in range(12):
            self.month.append(str(1 + i))

        ctk.CTkLabel(master=self.frame1, text=self.id).pack(padx=10, pady=12)
        ctk.CTkLabel(master=self.frame1, textvariable=self.name).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="My patients", width=5,
                      command=lambda: self.My_patient()).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Personal Information", width=5,
                      command=lambda: self.Personal_Information()).pack(padx=10, pady=12)

        self.frame1.pack(side='left', padx=10, fill='y')
        self.frame2.pack(side='left', padx=10, fill='both', expand="yes")

    def My_patient(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        ID = ctk.StringVar()
        Name = ctk.StringVar()
        Gender = ctk.StringVar()
        Birthday = ctk.StringVar()
        Contact_Number = ctk.StringVar()
        Doctor = ctk.StringVar()
        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        ctk.CTkLabel(master=frame, text='ID').grid(row=0, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text='Name').grid(row=0, column=1, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text='Gender').grid(row=0, column=2, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text='Birthday').grid(row=0, column=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text='Contact Number').grid(row=0, column=4, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text='Doctor').grid(row=0, column=5, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID, width=100).grid(
            row=1, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID, width=100).grid(
            row=2, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Name, width=100).grid(
            row=1, column=1, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Gender, width=100).grid(
            row=1, column=2, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Birthday, width=100).grid(
            row=1, column=3, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Contact_Number, width=100).grid(
            row=1, column=4, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Doctor, width=100).grid(
            row=1, column=5, padx=10, pady=12)
        ctk.CTkButton(master=frame, text="Search", width=5, command=lambda: Search()).grid(
            row=1, column=6, padx=10, pady=12)
        ctk.CTkButton(master=frame, text="Medical records", width=5, command=lambda: medical_records()).grid(
            row=2, column=6, padx=10, pady=12)

        tree = ttk.Treeview(frame,show="headings",height=20)
        tree["columns"] = ("id", "name", "gender", "birthday", "contact number", "doctor")
        tree.column("id", width=100, anchor='center')
        tree.column("name", width=100, anchor='center')
        tree.column("gender", width=100, anchor='center')
        tree.column("birthday", width=100, anchor='center')
        tree.column("contact number", width=100, anchor='center')
        tree.column("doctor", width=100, anchor='center')
        tree.heading("id", text="ID")
        tree.heading("name", text="Name")
        tree.heading("gender", text="Gender")
        tree.heading("birthday", text="Birthday")
        tree.heading("contact number", text="Contact Number")
        tree.heading("doctor", text="Doctor")
        tree.grid(row=3, column=0, columnspan=6, rowspan=5, padx=10, pady=12)

        Info = sql_request.get_personal_info(self.id, 'patient')
        tree.insert("",0,values=(Info[0],Info[2],Info[3],Info[4],Info[6]))

        def Search():
            pass

        def medical_records():
            for widget in self.frame2.winfo_children():
                widget.destroy()

            frame = ctk.CTkFrame(self.frame2)
            frame.pack(expand="yes")
            text = ctk.StringVar()

            tree = ttk.Treeview(frame, show="headings",height=20)
            tree["columns"] = ("Time", "Doctor", "Content")
            tree.column("Time", width=100, anchor='center')
            tree.column("Doctor", width=100, anchor='center')
            tree.column("Content", width=500, anchor='center')
            tree.heading("Time", text="Time")
            tree.heading("Doctor", text="Doctor")
            tree.heading("Content", text="Content")
            tree.insert("", 0, values=("20231205", "Mr.1", "111111111"))
            tree.grid(row=1, column=0, columnspan=7, rowspan=10, padx=10, pady=12)
            ctk.CTkEntry(master=frame, textvariable=text, width=300).grid(
                row=0, column=2, padx=10, pady=12)
            ctk.CTkButton(master=frame, text="Add", width=5, command=lambda: add()).grid(
                row=0, column=5, padx=10, pady=12)
            ctk.CTkButton(master=frame, text="Back", width=5, command=lambda: self.switch_Doctor(self.id)).grid(
                row=0, column=6, padx=10, pady=12)

            def add():
                pass


    def Personal_Information(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        frame3 = ctk.CTkFrame(self.frame2)

        ctk.CTkLabel(master=frame3, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Email').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Department').grid(row=6, column=0, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.birthday_year, width=80).grid(
            row=2, column=1, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.birthday_month, width=80).grid(
            row=2, column=2, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.birthday_day, width=80).grid(
            row=2, column=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.gender, width=300).grid(
            row=3, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.contact_number, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.email, width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.department, width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkButton(master=frame3, text='Modify',command=lambda: self.Password_()).grid(
            row=7, column=2, padx=10, pady=12)

        frame3.pack(expand="yes")

    def Password_(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        ctk.CTkLabel(master=frame, text='Please enter your password').pack()
        ctk.CTkEntry(master=frame, textvariable=self.password_entry, width=300).pack()
        ctk.CTkLabel(master=frame, textvariable=self.Label1, width=5).pack()
        self.password_entry.trace_add("write", self.Modify)

    def Modify(self,*args):
        self.Label1.set('')
        if self.password_entry.get() != '':
            if self.password_entry.get() == "123456789":
                for widget in self.frame2.winfo_children():
                    widget.destroy()
                frame = ctk.CTkFrame(self.frame2)
                frame.pack(expand="yes")

                ctk.CTkLabel(master=frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Email').grid(row=5, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Password').grid(row=6, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Re-enter Password').grid(row=7, column=0, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.name, width=300).grid(
                    row=1, column=1, columnspan=3, padx=10, pady=12)

                ctk.CTkComboBox(master=frame, variable=self.birthday_year, values=self.year, width=80).grid(
                    row=2, column=1, padx=10, pady=12)
                ctk.CTkComboBox(master=frame, variable=self.birthday_month, values=self.month, width=80).grid(
                    row=2, column=2, padx=10, pady=12)
                self._day = ctk.CTkComboBox(master=frame, variable=self.birthday_day, width=80)
                self._day.grid(row=2, column=3, padx=10, pady=12)
                self.birthday_month.trace_add("write", self.show_day)
                self.birthday_year.trace_add("write", self.show_day)

                ctk.CTkRadioButton(master=frame, text="male", variable=self.gender, value=True).grid(
                    row=3, column=2, padx=10, pady=12)
                ctk.CTkRadioButton(master=frame, text="female", variable=self.gender, value=True).grid(
                    row=3, column=3, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.contact_number, width=300).grid(
                    row=4, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.email, width=300).grid(
                    row=5, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password, show='*', width=300).grid(
                    row=6, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password_, show='*', width=300).grid(
                    row=7, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkLabel(master=frame, textvariable=self.Label2, width=5).grid(
                    row=7, column=4, padx=10, pady=12)
                self.password.trace_add("write", self.Password_confirmation)
                self.password_.trace_add("write", self.Password_confirmation)

                ctk.CTkButton(master=frame, text="Finish", width=5, command=lambda: self.Password_confirmation()).grid(
                    row=8, column=1, padx=10, pady=12)
                ctk.CTkButton(master=frame, text="Back", width=5, command=lambda: self.Personal_Information()).grid(
                    row=8, column=3, padx=10, pady=12)
            else:
                self.Label1.set('The password is wrong')

    def show_day(self, *args):
        self._day.set('')
        day = []
        if self.birthday_month.get() != '' and self.birthday_year.get() != '':
            month = int(self.birthday_month.get())
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                for i in range(31):
                    day.append(str(1 + i))
            elif month != 2:
                for i in range(30):
                    day.append(str(1 + i))
            else:
                year = int(self.birthday_year.get())
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    for i in range(29):
                        day.append(str(1 + i))
                else:
                    for i in range(28):
                        day.append(str(1 + i))
            self._day.configure(values=day)

    def Password_confirmation(self, *args):
        self.Label2.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label2.set('Pass')
            else:
                self.Label2.set('Fail')


class Nurse_Frame(Base_Frame):
    def __init__(self, master, id):
        super().__init__(master)

        self.id = id
        self.frame1 = ctk.CTkFrame(self.tk_frame)
        self.frame2 = ctk.CTkFrame(self.tk_frame)
        Info = sql_request.get_personal_info(self.id, 'doctor')

        self.name = ctk.StringVar()
        self.name.set(Info[2])
        self.birthday = ctk.StringVar()
        self.birthday_year = ctk.StringVar()
        self.birthday_month = ctk.StringVar()
        self.birthday_day = ctk.StringVar()
        self.gender = ctk.StringVar()
        self.gender.set(Info[3])
        self.contact_number = ctk.StringVar()
        self.contact_number.set(Info[4])
        self.email = ctk.StringVar()
        self.email.set(Info[1])
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.password_entry = ctk.StringVar()
        self.department = ctk.StringVar()
        self.department.set(Info[5])
        self.Label1 = ctk.StringVar()
        self.Label2 = ctk.StringVar()

        self.year = []
        self.month = []
        for i in range(100):
            self.year.append(str(1930 + i))
        for i in range(12):
            self.month.append(str(1 + i))

        ctk.CTkLabel(master=self.frame1, text=self.id).pack(padx=10, pady=12)
        ctk.CTkLabel(master=self.frame1, textvariable=self.name).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Nursing wards", width=5,
                      command=lambda: self.Nursing_wards()).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Personal Information", width=5,
                      command=lambda: self.Personal_Information()).pack(padx=10, pady=12)

        self.frame1.pack(side='left', padx=10, fill='y')
        self.frame2.pack(side='left', padx=10, fill='both', expand="yes")

    def Nursing_wards(self):
        pass

    def Personal_Information(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        frame3 = ctk.CTkFrame(self.frame2)

        ctk.CTkLabel(master=frame3, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Email').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Department').grid(row=6, column=0, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.birthday_year, width=80).grid(
            row=2, column=1, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.birthday_month, width=80).grid(
            row=2, column=2, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.birthday_day, width=80).grid(
            row=2, column=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.gender, width=300).grid(
            row=3, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.contact_number, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.email, width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.department, width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkButton(master=frame3, text='Modify', command=lambda: self.Password_()).grid(
            row=7, column=2, padx=10, pady=12)

        frame3.pack(expand="yes")

    def Password_(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        ctk.CTkLabel(master=frame, text='Please enter your password').pack()
        ctk.CTkEntry(master=frame, textvariable=self.password_entry, width=300).pack()
        ctk.CTkLabel(master=frame, textvariable=self.Label1, width=5).pack()
        self.password_entry.trace_add("write", self.Modify)


    def Modify(self,*args):
        self.Label1.set('')
        if self.password_entry.get() != '':
            if self.password_entry.get() == "123456789":
                for widget in self.frame2.winfo_children():
                    widget.destroy()
                frame = ctk.CTkFrame(self.frame2)
                frame.pack(expand="yes")

                ctk.CTkLabel(master=frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Contact number').grid(row=4, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Email').grid(row=5, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Password').grid(row=6, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Re-enter Password').grid(row=7, column=0, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.name, width=300).grid(
                    row=1, column=1, columnspan=3, padx=10, pady=12)

                ctk.CTkComboBox(master=frame, variable=self.birthday_year, values=self.year, width=80).grid(
                    row=2, column=1, padx=10, pady=12)
                ctk.CTkComboBox(master=frame, variable=self.birthday_month, values=self.month, width=80).grid(
                    row=2, column=2, padx=10, pady=12)
                self._day = ctk.CTkComboBox(master=frame, variable=self.birthday_day, width=80)
                self._day.grid(row=2, column=3, padx=10, pady=12)
                self.birthday_month.trace_add("write", self.show_day)
                self.birthday_year.trace_add("write", self.show_day)

                ctk.CTkRadioButton(master=frame, text="male", variable=self.gender, value=True).grid(
                    row=3, column=2, padx=10, pady=12)
                ctk.CTkRadioButton(master=frame, text="female", variable=self.gender, value=True).grid(
                    row=3, column=3, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.contact_number, width=300).grid(
                    row=4, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.email, width=300).grid(
                    row=5, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password, show='*', width=300).grid(
                    row=6, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password_, show='*', width=300).grid(
                    row=7, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkLabel(master=frame, textvariable=self.Label2, width=5).grid(
                    row=7, column=4, padx=10, pady=12)
                self.password.trace_add("write", self.Password_confirmation)
                self.password_.trace_add("write", self.Password_confirmation)

                ctk.CTkButton(master=frame, text="Finish", width=5, command=lambda: self.Password_confirmation()).grid(
                    row=8, column=1, padx=10, pady=12)
                ctk.CTkButton(master=frame, text="Back", width=5, command=lambda: self.Personal_Information()).grid(
                    row=8, column=3, padx=10, pady=12)
            else:
                self.Label1.set('The password is wrong')


    def show_day(self, *args):
        self._day.set('')
        day = []
        if self.birthday_month.get() != '' and self.birthday_year.get() != '':
            month = int(self.birthday_month.get())
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                for i in range(31):
                    day.append(str(1 + i))
            elif month != 2:
                for i in range(30):
                    day.append(str(1 + i))
            else:
                year = int(self.birthday_year.get())
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    for i in range(29):
                        day.append(str(1 + i))
                else:
                    for i in range(28):
                        day.append(str(1 + i))
            self._day.configure(values=day)

    def Password_confirmation(self, *args):
        self.Label2.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label2.set('Pass')
            else:
                self.Label2.set('Fail')

# TODO   管理员界面，开药方的界面，开检查单的界面，分配病房的界面（护士长），病房查看的界面，药房的界面
