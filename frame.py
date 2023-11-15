import customtkinter as ctk
from tkinter import messagebox
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

        ctk.CTkButton(master=self.frame1, text="Attendance records", width=5).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Personal Information", width=5).pack(padx=10, pady=12)

        self.frame1.pack(side='left', padx=10, fill='y')
        self.frame2.pack(side='left', padx=10, fill='both', expand="yes")


class Doctor_Frame(Base_Frame):
    def __init__(self, master, id):
        super().__init__(master)

        self.id = id
        self.frame1 = ctk.CTkFrame(self.tk_frame)
        self.frame2 = ctk.CTkFrame(self.tk_frame)

        ctk.CTkButton(master=self.frame1, text="My patients", width=5).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Personal Information", width=5).pack(padx=10, pady=12)

        self.frame1.pack(side='left', padx=10, fill='y')
        self.frame2.pack(side='left', padx=10, fill='both', expand=True)


class Nurse_Frame(Base_Frame):
    def __init__(self, master, id):
        super().__init__(master)

        self.id = id
        self.frame1 = ctk.CTkFrame(self.tk_frame)
        self.frame2 = ctk.CTkFrame(self.tk_frame)

        ctk.CTkButton(master=self.frame1, text="Work room", width=5).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Personal Information", width=5).pack(padx=10, pady=12)

        self.frame1.pack(side='left', padx=10, fill='y')
        self.frame2.pack(side='left', padx=10, fill='both', expand=True)
