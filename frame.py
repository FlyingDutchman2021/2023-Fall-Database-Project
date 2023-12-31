import customtkinter as ctk
from tkinter import messagebox, ttk
import sql_request
import re


class Base_Frame:

    def __init__(self, master):
        self.tk_frame = ctk.CTkFrame(master)
        self.tk_frame.pack(fill="both", expand=True)

    def switch_Log_In(self, identity):  # 界面切换
        for widget in self.tk_frame.winfo_children():  # 先销毁所有部件
            widget.destroy()
        Log_In_Frame(self.tk_frame, identity) # 加载新界面

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

    def switch_Administrator(self,id):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Administrator_Frame(self.tk_frame, id)

class Identity_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame = ctk.CTkFrame(self.tk_frame)

        # 更突出的标题
        title_label = ctk.CTkLabel(master=self.frame, text="Choose your identity", font=("Arial", 14))
        title_label.grid(row=0, column=0, columnspan=3, padx=20, pady=15)

        # 使用自定义样式的按钮
        patient_button = ctk.CTkButton(master=self.frame, text="Patient", width=120, command=lambda: self.Log_In("patient"))
        doctor_button = ctk.CTkButton(master=self.frame, text="Doctor", width=120, command=lambda: self.Log_In("doctor"))
        nurse_button = ctk.CTkButton(master=self.frame, text="Nurse", width=120, command=lambda: self.Log_In("nurse"))

        patient_button.grid(row=1, column=0, padx=10, pady=10)
        doctor_button.grid(row=1, column=1, padx=10, pady=10)
        nurse_button.grid(row=1, column=2, padx=10, pady=10)

        self.frame.pack(pady=20, expand='yes')

    def Log_In(self, identity):
        self.switch_Log_In(identity)

class Log_In_Frame(Base_Frame):

    def __init__(self, master, identity: str):
        super().__init__(master)

        self.identity = identity
        self.account = ctk.StringVar()
        self.password = ctk.StringVar()
        self.frame = ctk.CTkFrame(self.tk_frame)

        # 改进字体和文本标签
        ctk.CTkLabel(master=self.frame, text='Account', font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password', font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=12)

        # 输入框样式优化
        ctk.CTkEntry(master=self.frame, textvariable=self.account, width=200).grid(row=0, column=1, columnspan=2,
                                                                                   padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, show='*', width=200).grid(row=1, column=1,
                                                                                              columnspan=2, padx=10,
                                                                                              pady=12)

        # 按钮样式优化
        ctk.CTkButton(master=self.frame, text="Log in", width=120, command=lambda: self.Log_in()).grid(row=2, column=1,
                                                                                                       padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Sign up", width=120, command=lambda: self.Sign_up()).grid(row=2,
                                                                                                         column=2,
                                                                                                         padx=10,
                                                                                                         pady=12)

        self.frame.pack(pady=20, expand='yes')

    def Log_in(self):
        status, id = sql_request.login(str(self.account.get()),
                                       str(self.password.get()),
                                       self.identity) # 验证账号密码
        if status == 'Success':
            if self.identity == "patient":
                self.switch_Patient(id)
            if self.identity == "doctor":
                if id == "10086":
                    self.switch_Administrator(id)
                else:
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

        # 存储用户输入的内容
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
        self.blood_type = ctk.StringVar()
        self.note = ctk.StringVar()

        # 循环生成时间
        for i in range(100):
            self.year.append(str(1930 + i))
        for i in range(12):
            self.month.append(str(1 + i))

        # 输入内容:标签+输入框
        ctk.CTkLabel(master=self.frame, text="Please enter your message", width=200).grid(
            row=0, column=0, columnspan=4, padx=10, pady=12)

        ctk.CTkLabel(master=self.frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='blood_type(A/B/O/AB)').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Contact number').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Email').grid(row=6, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=7, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Re-enter Password').grid(row=8, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='note').grid(row=9, column=0, padx=10, pady=12)

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

        # 性别选择的单选按钮
        ctk.CTkRadioButton(master=self.frame, text="Male", variable=self.gender, value="Male").grid(
            row=3, column=2, padx=10, pady=12)
        ctk.CTkRadioButton(master=self.frame, text="Female", variable=self.gender, value="Female").grid(
            row=3, column=3, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.blood_type, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.contact_number, width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.email, width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)


        ctk.CTkEntry(master=self.frame, textvariable=self.password, show='*', width=300).grid(
            row=7, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password_, show='*', width=300).grid(
            row=8, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, textvariable=self.Label, width=5).grid(  # pass or fail
            row=8, column=4, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.note, width=300).grid(
            row=9, column=1, columnspan=3, padx=10, pady=12)

        self.password.trace_add("write", self.Password_confirmation)
        self.password_.trace_add("write", self.Password_confirmation)

        # 确认按钮，点击后提交注册
        ctk.CTkButton(master=self.frame, text="Finish", width=5, command=self.register).grid(row=10, column=1, padx=10,
                                                                                             pady=12)


        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.switch_Log_In("patient")).grid(
            row=10, column=3, padx=10, pady=12)
        self.frame.pack(expand='yes')

    # 验证密码
    def Password_confirmation(self, *args):  # 二次确认密码相同，检查密码相同
        self.Label.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():  # 密码是否相等
                self.Label.set('Pass')
            else:
                self.Label.set('Fail')

    def show_day(self, *args): # 显示日期
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

    # 获得输入信息，注册，返回注册结果
    def register(self):
        # 输入是否有空
        if not all([self.name.get(), self.email.get(), self.contact_number.get(), self.password.get(),
                    self.birthday_year.get(), self.birthday_month.get(), self.birthday_day.get(), self.gender.get()]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # 验证联系电话格式
        if not self.validate_contact_number(self.contact_number.get()):
            messagebox.showerror("Error", "Invalid contact number format")
            return

        # 验证电子邮件格式
        if not self.validate_email(self.email.get()):
            messagebox.showerror("Error", "Invalid email format")
            return

        # 验证密码是否匹配
        if self.password.get() != self.password_.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        # 验证血型
        if not self.validate_blood_type(self.blood_type.get()):
            messagebox.showerror("Error", "Invalid blood type. Please choose A, B, AB or O.")
            return

        # 组合生日日期
        birth_date = f"{self.birthday_year.get()}{self.birthday_month.get().zfill(2)}{self.birthday_day.get().zfill(2)}"

        # 如果满足上述条件
        # 调用后端函数进行注册
        result = sql_request.register_patient(
            self.email.get(),
            self.name.get(),
            self.gender.get(),
            birth_date,
            self.blood_type.get(),
            self.contact_number.get(),
            self.note.get(),
            self.password.get()
        )

        if result == 'Success':
            messagebox.showinfo("Success", "Registration successful")
            self.switch_Log_In("patient")
        else:
            messagebox.showerror("Error", result)

    def validate_email(self, email):
        # 电子邮件的基本验证正则表达式
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def validate_contact_number(self, contact_number):
        # 检查是否为11位数字
        return contact_number.isdigit() and len(contact_number) == 11

    def validate_blood_type(self, blood_type):
        return blood_type in ["A", "B", "O", "AB"]

class Sign_up_Doctor_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name = ctk.StringVar()
        self.gender = ctk.StringVar()
        self.contact_number = ctk.StringVar()
        self.email = ctk.StringVar()
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.Label = ctk.StringVar()
        self.frame = ctk.CTkFrame(self.tk_frame)

        ctk.CTkLabel(master=self.frame, text="Please enter your message", width=200).grid(
            row=0, column=0, columnspan=4, padx=10, pady=12)

        ctk.CTkLabel(master=self.frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Gender').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Contact number').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Email').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Re-enter Password').grid(row=6, column=0, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkRadioButton(master=self.frame, text="Male", variable=self.gender, value="Male").grid(
            row=2, column=2, padx=10, pady=12)
        ctk.CTkRadioButton(master=self.frame, text="Female", variable=self.gender, value="Female").grid(
            row=2, column=3, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.contact_number, width=300).grid(
            row=3, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.email, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, show='*', width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password_, show='*', width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, textvariable=self.Label, width=20).grid(
            row=6, column=4, padx=10, pady=12)
        self.password.trace_add("write", self.Password_confirmation)
        self.password_.trace_add("write", self.Password_confirmation)

        ctk.CTkButton(master=self.frame, text="Finish", width=5, command=self.register).grid(
            row=7, column=1, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.switch_Log_In("doctor")).grid(
            row=7, column=3, padx=10, pady=12)
        self.frame.pack(expand='yes')

    def Password_confirmation(self, *args):
        self.Label.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label.set('Pass')
            else:
                self.Label.set('Fail')

    # 获得输入信息，注册，返回注册结果
    def register(self):
        # 输入验证
        if not all([self.name.get(), self.email.get(), self.contact_number.get(), self.password.get(), self.gender.get()]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if not self.validate_contact_number(self.contact_number.get()):
            messagebox.showerror("Error", "Invalid contact number format")
            return

        if not self.validate_email(self.email.get()):
            messagebox.showerror("Error", "Invalid email format")
            return

        if self.password.get() != self.password_.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        # 调用后端注册函数
        result = sql_request.register_doctor(
            self.email.get(),
            self.name.get(),
            self.gender.get(),
            self.contact_number.get(),
            self.password.get()
        )

        if result == 'Success':
            messagebox.showinfo("Success", "Registration successful")
            self.switch_Log_In("doctor")  # 假设有专门的医生登录界面
        else:
            messagebox.showerror("Error", result)

    def validate_email(self, email):
        # 电子邮件的基本验证正则表达式
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def validate_contact_number(self, contact_number):
        # 检查是否为11位数字
        return contact_number.isdigit() and len(contact_number) == 11

class Sign_up_Nurse_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name = ctk.StringVar()
        self.gender = ctk.StringVar()
        self.contact_number = ctk.StringVar()
        self.email = ctk.StringVar()
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.Label = ctk.StringVar()
        self.frame = ctk.CTkFrame(self.tk_frame)

        ctk.CTkLabel(master=self.frame, text="Please enter your message", width=200).grid(
            row=0, column=0, columnspan=4, padx=10, pady=12)

        ctk.CTkLabel(master=self.frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Gender').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Contact number').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Email').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, text='Re-enter Password').grid(row=6, column=0, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkRadioButton(master=self.frame, text="Male", variable=self.gender, value="Male").grid(
            row=2, column=2, padx=10, pady=12)
        ctk.CTkRadioButton(master=self.frame, text="Female", variable=self.gender, value="Female").grid(
            row=2, column=3, padx=10, pady=12)

        ctk.CTkEntry(master=self.frame, textvariable=self.contact_number, width=300).grid(
            row=3, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.email, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password, show='*', width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkEntry(master=self.frame, textvariable=self.password_, show='*', width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=self.frame, textvariable=self.Label, width=20).grid(
            row=6, column=4, padx=10, pady=12)
        self.password.trace_add("write", self.Password_confirmation)
        self.password_.trace_add("write", self.Password_confirmation)

        ctk.CTkButton(master=self.frame, text="Finish", width=5, command=self.register).grid(
            row=7, column=1, padx=10, pady=12)
        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.switch_Log_In("nurse")).grid(
            row=7, column=3, padx=10, pady=12)
        self.frame.pack(expand='yes')

    def Password_confirmation(self, *args):
        self.Label.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label.set('Pass')
            else:
                self.Label.set('Fail')

    def register(self):
        # 输入验证
        if not all(
                [self.name.get(), self.email.get(), self.contact_number.get(), self.password.get(), self.gender.get()]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if not self.validate_contact_number(self.contact_number.get()):
            messagebox.showerror("Error", "Invalid contact number format")
            return

        if not self.validate_email(self.email.get()):
            messagebox.showerror("Error", "Invalid email format")
            return

        if self.password.get() != self.password_.get():
            messagebox.showerror("Error", "Passwords do not match")
            return

        # 调用后端注册函数
        result = sql_request.register_nurse(
            self.email.get(),
            self.name.get(),
            self.gender.get(),
            self.contact_number.get(),
            self.password.get()
        )

        if result == 'Success':
            messagebox.showinfo("Success", "Registration successful")
            self.switch_Log_In("nurse")
        else:
            messagebox.showerror("Error", result)

    def validate_email(self, email):
        # 电子邮件的基本验证正则表达式
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def validate_contact_number(self, contact_number):
        # 检查是否为11位数字
        return contact_number.isdigit() and len(contact_number) == 11

class Patient_Frame(Base_Frame):
    def __init__(self, master, id):
        super().__init__(master)

        self.id = id
        self.frame1 = ctk.CTkFrame(self.tk_frame)
        self.frame2 = ctk.CTkFrame(self.tk_frame)

        print(sql_request.get_personal_info(self.id, 'patient'))
        Info = sql_request.get_personal_info(self.id, 'patient')[1][0]

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
        self.blood_type = ctk.StringVar()
        self.blood_type.set(Info[5])
        self.contact_number = ctk.StringVar()
        self.contact_number.set(Info[6])
        self.email = ctk.StringVar()
        self.email.set(Info[1])
        self.password = ctk.StringVar()
        self.password_ = ctk.StringVar()
        self.password_entry = ctk.StringVar()
        self.note = ctk.StringVar()
        self.note.set(Info[7])
        self.Label1 = ctk.StringVar()
        self.Label2 = ctk.StringVar()

        self.password.set('123456789')

        self.year = []
        self.month = []
        for i in range(100):
            self.year.append(str(1930 + i))
        for i in range(12):
            self.month.append(str(1 + i))

        # 左侧功能按钮区域样式优化
        self.frame1 = ctk.CTkFrame(self.tk_frame, corner_radius=10)  # 添加圆角
        self.frame1.pack(side='left', padx=10, fill='y', expand=False)

        ctk.CTkLabel(master=self.frame1, text="ID: " + str(self.id)).pack(padx=10, pady=12)
        ctk.CTkLabel(master=self.frame1, text="Name: " + self.name.get()).pack(padx=10, pady=12)


        # 按钮样式优化
        ctk.CTkButton(master=self.frame1, text="My medical records", width=200,
                      command=lambda: self.Attendance_records()).pack(padx=10, pady=10)
        ctk.CTkButton(master=self.frame1, text="Personal Information", width=200,
                      command=lambda: self.Personal_Information()).pack(padx=10, pady=10)

        # 右侧信息显示区域
        self.frame2 = ctk.CTkFrame(self.tk_frame, corner_radius=10)  # 添加圆角
        self.frame2.pack(side='left', padx=10, fill='both', expand=True)

    # 仅作展示
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
        tree.pack()
        message, Info = sql_request.find_medical(self.id)
        if message == 'Success':
            tree.delete(*tree.get_children())
            for i in range(len(Info)):
                tree.insert('', i, values=(
                    Info[i][3], Info[i][2], Info[i][4]))

    def Personal_Information(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        frame3 = ctk.CTkFrame(self.frame2)

        ctk.CTkLabel(master=frame3, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Gender').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Blood_type').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Contact number').grid(row=5, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Email').grid(row=6, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Note').grid(row=7, column=0, padx=10, pady=12)

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

        ctk.CTkLabel(master=frame3, textvariable=self.blood_type, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.contact_number, width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.email, width=300).grid(
            row=6, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.note, width=300).grid(
            row=7, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkButton(master=frame3, text='Modify',command=lambda: self.Password_()).grid(
            row=8, column=2, padx=10, pady=12)

        frame3.pack(expand="yes")

    def Modify(self,*args):
        self.Label1.set('')
        if self.password_entry.get() != '':
            if self.password_entry.get() == self.password.get():
                for widget in self.frame2.winfo_children():
                    widget.destroy()
                frame = ctk.CTkFrame(self.frame2)
                frame.pack(expand="yes")

                ctk.CTkLabel(master=frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Birthday').grid(row=2, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Gender').grid(row=3, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='blood_type(A/B/O/AB)').grid(row=4, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Contact number').grid(row=5, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Email').grid(row=6, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Password').grid(row=7, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Re-enter Password').grid(row=8, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='note').grid(row=9, column=0, padx=10, pady=12)

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

                # 性别选择的单选按钮
                ctk.CTkRadioButton(master=frame, text="Male", variable=self.gender, value="Male").grid(
                    row=3, column=2, padx=10, pady=12)
                ctk.CTkRadioButton(master=frame, text="Female", variable=self.gender, value="Female").grid(
                    row=3, column=3, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.blood_type, width=300).grid(
                    row=4, column=1, columnspan=3, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.contact_number, width=300).grid(
                    row=5, column=1, columnspan=3, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.email, width=300).grid(
                    row=6, column=1, columnspan=3, padx=10, pady=12)
    # 输入密码
                ctk.CTkEntry(master=frame, textvariable=self.password, show='*', width=300).grid(
                    row=7, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password_, show='*', width=300).grid(
                    row=8, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkLabel(master=frame, textvariable=self.Label2, width=5).grid(  # pass or fail
                    row=8, column=4, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.note, width=300).grid(
                    row=9, column=1, columnspan=3, padx=10, pady=12)

                self.password.trace_add("write", self.Password_confirmation)
                self.password_.trace_add("write", self.Password_confirmation)

                # 确认按钮，点击后提交修改结果
                ctk.CTkButton(master=frame, text="Finish", width=5, command=self.update).grid(row=10, column=1,
                                                                                                     padx=10,
                                                                                                     pady=12)

                ctk.CTkButton(master=frame, text="Back", width=5,
                              command=lambda: self.switch_Patient(self.id)).grid(
                    row=10, column=3, padx=10, pady=12)
                frame.pack()

                # 验证密码
            else:
                self.Label1.set('The password is wrong')


    def Password_(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        ctk.CTkLabel(master=frame, text='Please enter your password').pack()
        ctk.CTkEntry(master=frame, textvariable=self.password_entry, width=300, show='*').pack()
        ctk.CTkLabel(master=frame, textvariable=self.Label1, width=5).pack()
        self.password_entry.trace_add("write", self.Modify)

    def update(self):
                # 输入是否有空
                if not all([self.name.get(), self.email.get(), self.contact_number.get(), self.password.get(),
                            self.birthday_year.get(),  self.birthday_month.get(),
                            self.birthday_day.get(), self.gender.get()]):
                    messagebox.showerror("Error", "Please fill in all fields")
                    return

                # 验证联系电话格式
                if not self.validate_contact_number(self.contact_number.get()):
                    messagebox.showerror("Error", "Invalid contact number format")
                    return

                # 验证电子邮件格式
                if not self.validate_email(self.email.get()):
                    messagebox.showerror("Error", "Invalid email format")
                    return

                # 验证密码是否匹配
                if self.password.get() != self.password_.get():
                    messagebox.showerror("Error", "Passwords do not match")
                    return

                # 验证血型
                if not self.validate_blood_type(self.blood_type.get()):
                    messagebox.showerror("Error", "Invalid blood type. Please choose A, B, AB or O.")
                    return

                # 组合生日日期
                birth_date = f"{self.birthday_year.get()}{self.birthday_month.get().zfill(2)}{self.birthday_day.get().zfill(2)}"

                # 如果满足上述条件
                # 调用后端函数进行注册
                result = sql_request.update_patient_general(
                    self.id, # 获取ID
                    self.email.get(),
                    self.name.get(),
                    self.gender.get(),
                    birth_date,
                    self.blood_type.get(),
                    self.contact_number.get(),
                    self.note.get()
                )
                sql_request.update_password(
                    self.id,
                    'patient',
                    self.password.get()
                )
                if result == 'Success':
                    messagebox.showinfo("Success", "Successfully modified")
                    self.switch_Patient(self.id)
                else:
                    messagebox.showerror("Error", result)

    def Password_confirmation(self, *args):  # 二次确认密码相同，检查密码相同
                self.Label2.set('')
                if self.password.get() != '' and self.password_.get() != '':
                    if self.password.get() == self.password_.get():  # 密码是否相等
                        self.Label2.set('Pass')
                    else:
                        self.Label2.set('Fail')

    def show_day(self, *args):  # 显示日期
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

                # 获得输入信息，注册，返回注册结果

    def validate_email(self, email):
                # 电子邮件的基本验证正则表达式
                pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                return re.match(pattern, email) is not None

    def validate_contact_number(self, contact_number):
                # 检查是否为11位数字
                return contact_number.isdigit() and len(contact_number) == 11

    def validate_blood_type(self, blood_type):
                return blood_type in ["A", "B", "O", "AB"]

class Doctor_Frame(Base_Frame):
    def __init__(self, master, id):
        super().__init__(master)

        self.id = id
        self.frame1 = ctk.CTkFrame(self.tk_frame)
        self.frame2 = ctk.CTkFrame(self.tk_frame)

        print(self.id)

        print(sql_request.get_personal_info(self.id, 'doctor'))
        Info = sql_request.get_personal_info(self.id, 'doctor')[1][0]

        self.name = ctk.StringVar()
        self.name.set(Info[2])
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
        self.status = ctk.StringVar()
        self.status.set(Info[6])
        self.Label1 = ctk.StringVar()
        self.Label2 = ctk.StringVar()


        self.password.set('123456789')  # 二次输入密码，正确即可进入修改界面


        ctk.CTkLabel(master=self.frame1, text="ID: " + str(self.id)).pack(padx=10, pady=12)
        ctk.CTkLabel(master=self.frame1, text="Name: " + self.name.get()).pack(padx=10, pady=12)
        if self.status.get()=="A":
            ctk.CTkButton(master=self.frame1, text="Patients", width=200,
                      command=lambda: self.My_patient()).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Personal Information", width=200,
                      command=lambda: self.Personal_Information()).pack(padx=10, pady=12)

        self.frame1.pack(side='left', padx=10, fill='y')
        self.frame2.pack(side='left', padx=10, fill='both', expand="yes")

    def My_patient(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        ID = ctk.StringVar()
        ID_ = ctk.StringVar()
        Name = ctk.StringVar()
        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        ctk.CTkLabel(master=frame, text='ID').grid(row=0, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text='Name').grid(row=0, column=1, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID, width=100).grid(
            row=1, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID_, width=100).grid(
            row=2, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Name, width=100).grid(
            row=1, column=1, padx=10, pady=12)
        ctk.CTkButton(master=frame, text="Search", width=100, command=lambda: Search()).grid(
            row=1, column=6, padx=10, pady=12)
        ctk.CTkButton(master=frame, text="Medical records", width=100, command=lambda: medical_records()).grid(
            row=2, column=6, padx=10, pady=12)

        tree = ttk.Treeview(frame,show="headings",height=20)
        tree["columns"] = ("id", "email", "name", "gender", "birthday", "blood_type", "contact number", "note")
        tree.column("id", width=100, anchor='center')
        tree.column("name", width=100, anchor='center')
        tree.column("gender", width=100, anchor='center')
        tree.column("birthday", width=100, anchor='center')
        tree.column("contact number", width=150, anchor='center')
        tree.column("blood_type", width=100, anchor='center')
        tree.column("email", width=100, anchor='center')
        tree.column("note", width=300, anchor='center')
        tree.heading("id", text="ID")
        tree.heading("name", text="Name")
        tree.heading("gender", text="Gender")
        tree.heading("birthday", text="Birthday")
        tree.heading("contact number", text="Contact Number")
        tree.heading("blood_type", text="Blood_type")
        tree.heading("email", text="Email")
        tree.heading("note", text="Note")
        tree.grid(row=3, column=0, columnspan=8, rowspan=5, padx=10, pady=12)
        message, Info = sql_request.universal_find_patient('')
        if message == 'Success':
            tree.delete(*tree.get_children())
            for i in range(len(Info)):
                tree.insert('', i, values=(
                    Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5], Info[i][6], Info[i][7]))

        def Search():
            search_key = ''
            if ID.get() != '':
                search_key = ID.get()
            elif Name.get() != '':
                search_key = Name.get()
            message, Info = sql_request.universal_find_patient(search_key)
            if message == 'Success':
                tree.delete(*tree.get_children())
                for i in range(len(Info)):
                    tree.insert('', i, values=(
                    Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5], Info[i][6], Info[i][7]))

        def medical_records():
            for widget in self.frame2.winfo_children():
                widget.destroy()

            frame = ctk.CTkFrame(self.frame2)
            frame.pack(expand="yes")
            Content = ctk.StringVar()

            tree = ttk.Treeview(frame, show="headings",height=20)
            tree["columns"] = ("Time", "Doctor", "Content")
            tree.column("Time", width=100, anchor='center')
            tree.column("Doctor", width=100, anchor='center')
            tree.column("Content", width=500, anchor='center')
            tree.heading("Time", text="Time")
            tree.heading("Doctor", text="Doctor")
            tree.heading("Content", text="Content")
            tree.grid(row=1, column=0, columnspan=7, rowspan=10, padx=10, pady=12)
            ctk.CTkEntry(master=frame, textvariable=Content, width=300).grid(
                row=0, column=2, padx=10, pady=12)
            ctk.CTkButton(master=frame, text="Add", width=5, command=lambda: add()).grid(
                row=0, column=5, padx=10, pady=12)
            ctk.CTkButton(master=frame, text="Back", width=5, command=lambda: self.switch_Doctor(self.id)).grid(
                row=0, column=6, padx=10, pady=12)
            message, Info = sql_request.find_medical(ID_.get())
            if message == 'Success':
                tree.delete(*tree.get_children())
                for i in range(len(Info)):
                    tree.insert('', i, values=(
                        Info[i][3], Info[i][2], Info[i][4]))

            def add():
                print(int(ID_.get()))
                if Content.get() != '':
                    result = sql_request.prescription_update(int(ID_.get()), self.id, Content.get())
                    if result == 'Success':
                        messagebox.showinfo("Success", "The addition was successful")
                        message, Info = sql_request.find_medical(ID_.get())
                        if message == 'Success':
                            tree.delete(*tree.get_children())
                            for i in range(len(Info)):
                                tree.insert('', i, values=(
                                    Info[i][3], Info[i][2], Info[i][4]))
                    else:
                        messagebox.showerror("Error", "The addition was failed")

    def Personal_Information(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        frame3 = ctk.CTkFrame(self.frame2)

        ctk.CTkLabel(master=frame3, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Gender').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Contact number').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Email').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Department').grid(row=5, column=0, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.gender, width=300).grid(
            row=2, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.contact_number, width=300).grid(
            row=3, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.email, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.department, width=300).grid(
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
            if self.password_entry.get() == self.password.get():
                for widget in self.frame2.winfo_children():
                    widget.destroy()
                frame = ctk.CTkFrame(self.frame2)
                frame.pack(expand="yes")

                ctk.CTkLabel(master=frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Gender').grid(row=2, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Contact number').grid(row=3, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Email').grid(row=4, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Password').grid(row=5, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Re-enter Password').grid(row=6, column=0, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.name, width=300).grid(
                    row=1, column=1, columnspan=3, padx=10, pady=12)

                ctk.CTkRadioButton(master=frame, text="Male", variable=self.gender, value="Male").grid(
                    row=2, column=2, padx=10, pady=12)
                ctk.CTkRadioButton(master=frame, text="Female", variable=self.gender, value="Female").grid(
                    row=2, column=3, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.contact_number, width=300).grid(
                    row=3, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.email, width=300).grid(
                    row=4, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password, show='*', width=300).grid(
                    row=5, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password_, show='*', width=300).grid(
                    row=6, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkLabel(master=frame, textvariable=self.Label2, width=20).grid(
                    row=6, column=4, padx=10, pady=12)
                self.password.trace_add("write", self.Password_confirmation)
                self.password_.trace_add("write", self.Password_confirmation)

                ctk.CTkButton(master=frame, text="Finish", width=5, command=self.update).grid(
                    row=7, column=1, padx=10, pady=12)
                ctk.CTkButton(master=frame, text="Back", width=5,
                              command=lambda: self.switch_Doctor(self.id)).grid(
                    row=7, column=3, padx=10, pady=12)
            else:
                self.Label1.set('The password is wrong')

    def update(self):
                # 输入是否有空
                if not all([self.name.get(), self.email.get(), self.contact_number.get(), self.password.get(),
                         self.gender.get()]):
                    messagebox.showerror("Error", "Please fill in all fields")
                    return

                # 验证联系电话格式
                if not self.validate_contact_number(self.contact_number.get()):
                    messagebox.showerror("Error", "Invalid contact number format")
                    return

                # 验证电子邮件格式
                if not self.validate_email(self.email.get()):
                    messagebox.showerror("Error", "Invalid email format")
                    return

                # 验证密码是否匹配
                if self.password.get() != self.password_.get():
                    messagebox.showerror("Error", "Passwords do not match")
                    return


                # 如果满足上述条件
                # 调用后端函数进行注册
                result = sql_request.update_doctor_general(
                    self.id, # 获取ID
                    self.email.get(),
                    self.name.get(),
                    self.gender.get(),
                    self.contact_number.get(),
                )
                sql_request.update_password(
                    self.id,
                    'doctor',
                    self.password.get()
                )
                if result == 'Success':
                    messagebox.showinfo("Success", "Successfully modified")
                    self.switch_Patient(self.id)
                else:
                    messagebox.showerror("Error", result)

    def Password_confirmation(self, *args):
        self.Label2.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label2.set('Pass')
            else:
                self.Label2.set('Fail')

        # 获得输入信息，注册，返回注册结果

    def validate_email(self, email):
        # 电子邮件的基本验证正则表达式
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def validate_contact_number(self, contact_number):
        # 检查是否为11位数字
        return contact_number.isdigit() and len(contact_number) == 11

class Nurse_Frame(Base_Frame):
    def __init__(self, master, id):
        super().__init__(master)

        self.id = id
        self.frame1 = ctk.CTkFrame(self.tk_frame)
        self.frame2 = ctk.CTkFrame(self.tk_frame)
        Info = sql_request.get_personal_info(self.id, 'nurse')[1][0]

        self.name = ctk.StringVar()
        self.name.set(Info[2])
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
        self.status = ctk.StringVar()
        self.status.set(Info[6])
        self.isMaster = ctk.StringVar()
        self.isMaster.set(Info[7])
        self.Label1 = ctk.StringVar()
        self.Label2 = ctk.StringVar()

        self.password.set('123456789')

        ctk.CTkLabel(master=self.frame1, text="ID: " + str(self.id)).pack(padx=10, pady=12)
        ctk.CTkLabel(master=self.frame1, text="Name: " + self.name.get()).pack(padx=10, pady=12)

        if self.status.get()=="A":
            ctk.CTkButton(master=self.frame1, text="Nursing wards", width=200,
                      command=lambda: self.Nursing_wards()).pack(padx=10, pady=12)
        if self.isMaster.get()=="1":
            ctk.CTkButton(master=self.frame1, text="Work assignments", width=200,
                          command=lambda: self.Assignment()).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Personal Information", width=200,
                      command=lambda: self.Personal_Information()).pack(padx=10, pady=12)

        self.frame1.pack(side='left', padx=10, fill='y')
        self.frame2.pack(side='left', padx=10, fill='both', expand="yes")

    def Nursing_wards(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        tree = ttk.Treeview(frame, show="headings", height=10)
        tree["columns"] = ("name","ward")
        tree.column("name", width=100, anchor='center')
        tree.column("ward", width=100, anchor='center')
        tree.heading("name", text="Name")
        tree.heading("ward", text="Ward")
        tree.grid(row=3, column=0, columnspan=6, rowspan=5, padx=10, pady=12)
        message, Info = sql_request.find_nurse_ward(self.id)
        if message == 'Success':
            tree.delete(*tree.get_children())
            for i in range(len(Info)):
                Info_ = sql_request.get_personal_info(self.id,'nurse')[1][0]
                tree.insert('', i,
                            values=(Info_[2],Info[i][1]))

    def Assignment(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        ID = ctk.StringVar()
        ID_ = ctk.StringVar()
        Name = ctk.StringVar()
        Department = ctk.StringVar()
        Ward = ctk.StringVar()
        Ward_ = ctk.StringVar()
        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        ctk.CTkLabel(master=frame, text='ID').grid(row=0, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text='Name').grid(row=0, column=1, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text="Department").grid(row=0, column=2, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text="Ward").grid(row=0, column=3, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID, width=100).grid(
            row=1, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID_, width=100).grid(
            row=2, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Name, width=100).grid(
            row=1, column=1, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Department, width=100).grid(
            row=1, column=2, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Ward, width=100).grid(
            row=1, column=3, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Ward_, width=100).grid(
            row=2, column=3, padx=10, pady=12)
        ctk.CTkButton(master=frame, text="Search", width=5, command=lambda: Search()).grid(
            row=1, column=5, padx=10, pady=12)
        ctk.CTkButton(master=frame, text='Modify', width=5, command=lambda: Modify()).grid(
            row=2, column=5, padx=10, pady=12)

        tree = ttk.Treeview(frame, show="headings", height=20)
        tree["columns"] = ("id", "email", "name", "gender", "contact number", "department", "ward")
        tree.column("id", width=100, anchor='center')
        tree.column("email", width=100, anchor='center')
        tree.column("name", width=100, anchor='center')
        tree.column("gender", width=100, anchor='center')
        tree.column("contact number", width=150, anchor='center')
        tree.column("department", width=100, anchor='center')
        tree.column("ward", width=100, anchor='center')
        tree.heading("id", text="ID")
        tree.heading("email", text="Email")
        tree.heading("name", text="Name")
        tree.heading("gender", text="Gender")
        tree.heading("department", text="Department")
        tree.heading("contact number", text="Contact Number")
        tree.heading("ward", text="Ward")
        tree.grid(row=3, column=0, columnspan=7, rowspan=5, padx=10, pady=12)
        message, Info = sql_request.universal_find_nurse('', '')
        if message == 'Success':
            tree.delete(*tree.get_children())
            for i in range(len(Info)):
                Info_ = sql_request.find_nurse_ward(Info[i][0])[1]
                tree.insert('', i,
                            values=(Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5], Info_[0][1]))

        def Search():
            search_key = ''
            if ID.get() != '':
                search_key = ID.get()
            elif Name.get() != '':
                search_key = Name.get()
            elif Department.get() != '':
                search_key = Department.get()
            if Ward.get() != '':
                message, Info = sql_request.find_ward_nurse(Ward.get())
                if message == 'Success':
                    tree.delete(*tree.get_children())
                    for i in range(len(Info)):
                        Info_ = sql_request.get_personal_info(Info[i][0],'nurse')[1][0]
                        tree.insert('', i,
                                    values=(
                                        Info_[0], Info_[1], Info_[2], Info_[3], Info_[4], Info_[5], Info[i][1]))
            else:
                message, Info = sql_request.universal_find_nurse(search_key, '')
                if message == 'Success':
                    tree.delete(*tree.get_children())
                    for i in range(len(Info)):
                        Info_ = sql_request.find_nurse_ward(Info[i][0])[1]
                        tree.insert('', i,
                                    values=(Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5],
                                            Info_[0][1]))

        def Modify():
            result = sql_request.assign_ward(int(ID_.get()), int(Ward_.get()))[0]
            if result == 'Success':
                messagebox.showinfo("Success", "Successfully modified")
                message, Info = sql_request.universal_find_nurse('', '')
                if message == 'Success':
                    tree.delete(*tree.get_children())
                    for i in range(len(Info)):
                        tree.insert('', i,
                                    values=(Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5]))
            else:
                messagebox.showerror("Error", result)


    def Personal_Information(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        frame3 = ctk.CTkFrame(self.frame2)

        ctk.CTkLabel(master=frame3, text='Name').grid(row=1, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Gender').grid(row=2, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Contact number').grid(row=3, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Email').grid(row=4, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, text='Department').grid(row=5, column=0, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.name, width=300).grid(
            row=1, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.gender, width=300).grid(
            row=2, column=1, columnspan=3, padx=10, pady=12)

        ctk.CTkLabel(master=frame3, textvariable=self.contact_number, width=300).grid(
            row=3, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.email, width=300).grid(
            row=4, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame3, textvariable=self.department, width=300).grid(
            row=5, column=1, columnspan=3, padx=10, pady=12)
        ctk.CTkButton(master=frame3, text='Modify', command=lambda: self.Password_()).grid(
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

    def Modify(self, *args):
        self.Label1.set('')
        if self.password_entry.get() != '':
            if self.password_entry.get() == self.password.get():
                for widget in self.frame2.winfo_children():
                    widget.destroy()
                frame = ctk.CTkFrame(self.frame2)
                frame.pack(expand="yes")

                ctk.CTkLabel(master=frame, text='Name').grid(row=1, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Gender').grid(row=2, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Contact number').grid(row=3, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Email').grid(row=4, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Password').grid(row=5, column=0, padx=10, pady=12)
                ctk.CTkLabel(master=frame, text='Re-enter Password').grid(row=6, column=0, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.name, width=300).grid(
                    row=1, column=1, columnspan=3, padx=10, pady=12)

                ctk.CTkRadioButton(master=frame, text="Male", variable=self.gender, value="Male").grid(
                    row=2, column=2, padx=10, pady=12)
                ctk.CTkRadioButton(master=frame, text="Female", variable=self.gender, value="Female").grid(
                    row=2, column=3, padx=10, pady=12)

                ctk.CTkEntry(master=frame, textvariable=self.contact_number, width=300).grid(
                    row=3, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.email, width=300).grid(
                    row=4, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password, show='*', width=300).grid(
                    row=5, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkEntry(master=frame, textvariable=self.password_, show='*', width=300).grid(
                    row=6, column=1, columnspan=3, padx=10, pady=12)
                ctk.CTkLabel(master=frame, textvariable=self.Label2, width=20).grid(
                    row=6, column=4, padx=10, pady=12)
                self.password.trace_add("write", self.Password_confirmation)
                self.password_.trace_add("write", self.Password_confirmation)

                ctk.CTkButton(master=frame, text="Finish", width=5, command=self.update).grid(
                    row=7, column=1, padx=10, pady=12)
                ctk.CTkButton(master=frame, text="Back", width=5,
                              command=lambda: self.switch_Nurse(self.id)).grid(
                    row=7, column=3, padx=10, pady=12)
            else:
                self.Label1.set('The password is wrong')
    def update(self):
                # 输入是否有空
                if not all([self.name.get(), self.email.get(), self.contact_number.get(), self.password.get(),
                         self.gender.get()]):
                    messagebox.showerror("Error", "Please fill in all fields")
                    return

                # 验证联系电话格式
                if not self.validate_contact_number(self.contact_number.get()):
                    messagebox.showerror("Error", "Invalid contact number format")
                    return

                # 验证电子邮件格式
                if not self.validate_email(self.email.get()):
                    messagebox.showerror("Error", "Invalid email format")
                    return

                # 验证密码是否匹配
                if self.password.get() != self.password_.get():
                    messagebox.showerror("Error", "Passwords do not match")
                    return


                # 如果满足上述条件
                # 调用后端函数进行注册
                result = sql_request.update_nurse_general(
                    self.id, # 获取ID
                    self.email.get(),
                    self.name.get(),
                    self.gender.get(),
                    self.contact_number.get(),
                )
                sql_request.update_password(
                    self.id,
                    'nurse',
                    self.password.get()
                )
                if result == 'Success':
                    messagebox.showinfo("Success", "Successfully modified")
                    self.switch_Patient(self.id)
                else:
                    messagebox.showerror("Error", result)

    def Password_confirmation(self, *args):
        self.Label2.set('')
        if self.password.get() != '' and self.password_.get() != '':
            if self.password.get() == self.password_.get():
                self.Label2.set('Pass')
            else:
                self.Label2.set('Fail')

        # 获得输入信息，注册，返回注册结果

    def validate_email(self, email):
        # 电子邮件的基本验证正则表达式
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def validate_contact_number(self, contact_number):
        # 检查是否为11位数字
        return contact_number.isdigit() and len(contact_number) == 11

class Administrator_Frame(Base_Frame):
    def __init__(self, master, id):
        super().__init__(master)

        self.id = id
        self.frame1 = ctk.CTkFrame(self.tk_frame)
        self.frame2 = ctk.CTkFrame(self.tk_frame)

        ctk.CTkLabel(master=self.frame1, text=self.id).pack(padx=10, pady=12)
        ctk.CTkLabel(master=self.frame1, text="Administrator").pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Doctor", width=200,
                      command=lambda: self.Doctor()).pack(padx=10, pady=12)
        ctk.CTkButton(master=self.frame1, text="Nurse", width=200,
                      command=lambda: self.Nurse()).pack(padx=10, pady=12)

        self.frame1.pack(side='left', padx=10, fill='y')
        self.frame2.pack(side='left', padx=10, fill='both', expand="yes")

    def Doctor(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        ID = ctk.StringVar()
        ID_ = ctk.StringVar()
        Name = ctk.StringVar()
        Department = ctk.StringVar()
        Department_ = ctk.StringVar()
        Status = ctk.IntVar()
        Status_ = ctk.IntVar()
        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")

        ctk.CTkLabel(master=frame, text='ID').grid(row=0, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text='Name').grid(row=0, column=1, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text="Department").grid(row=0, column=2, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text="Status").grid(row=0, column=3, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID, width=100).grid(
            row=1, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID_, width=100).grid(
            row=2, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Name, width=100).grid(
            row=1, column=1, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Department, width=100).grid(
            row=1, column=2, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Department_, width=100).grid(
            row=2, column=2, padx=10, pady=12)
        ctk.CTkCheckBox(master=frame, text="P", variable=Status, width=100).grid(
            row=1, column=3, padx=10, pady=12 )
        ctk.CTkCheckBox(master=frame, text="A", variable=Status_, width=100).grid(
            row=2, column=3, padx=10, pady=12)
        ctk.CTkButton(master=frame, text="Search", width=5, command=lambda: Search()).grid(
            row=1, column=4, padx=10, pady=12)
        ctk.CTkButton(master=frame, text='Modify', width=5, command=lambda: Modify()).grid(
            row=2, column=4, padx=10, pady=12)

        tree = ttk.Treeview(frame,show="headings",height=20)
        tree["columns"] = ("id", "email", "name", "gender", "contact number", "department", "status")
        tree.column("id", width=100, anchor='center')
        tree.column("email", width=100, anchor='center')
        tree.column("name", width=100, anchor='center')
        tree.column("gender", width=100, anchor='center')
        tree.column("contact number", width=100, anchor='center')
        tree.column("department", width=100, anchor='center')
        tree.column("status", width=100, anchor='center')
        tree.heading("id", text="ID")
        tree.heading("email", text="Email")
        tree.heading("name", text="Name")
        tree.heading("gender", text="Gender")
        tree.heading("department", text="Department")
        tree.heading("contact number", text="Contact Number")
        tree.heading("status", text="Status")
        tree.grid(row=3, column=0, columnspan=7, rowspan=5, padx=10, pady=12)
        message, Info = sql_request.universal_find_doctor('', '')
        if message == 'Success':
            tree.delete(*tree.get_children())
            for i in range(len(Info)):
                tree.insert('', i,
                            values=(Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5], Info[i][6]))


        def Search():
            search_key = ''
            status = ''
            if Status.get() == 1:
                status = 'P'
            if ID.get()!='':
                search_key = ID.get()
            elif Name.get()!='':
                search_key = Name.get()
            elif Department.get()!='':
                search_key = Department.get()
            message,Info = sql_request.universal_find_doctor(search_key,status)
            if message == 'Success':
                tree.delete(*tree.get_children())
                for i in range(len(Info)):
                    tree.insert('', i, values=(Info[i][0],Info[i][1],Info[i][2],Info[i][3],Info[i][4],Info[i][5],Info[i][6]))

        def Modify():
            if Status_.get() == 1:
                status = 'A'
            else:
                status = 'P'

            # 调用后端函数进行搜索
            result = sql_request.update_doctor_admin(
                int(ID_.get()),  # 获取ID
                Department_.get(),
                status
            )

            if result == 'Success':
                messagebox.showinfo("Success", "Successfully modified")
                message, Info = sql_request.universal_find_doctor('', '')
                if message == 'Success':
                    tree.delete(*tree.get_children())
                    for i in range(len(Info)):
                        tree.insert('', i,
                                    values=(
                                    Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5], Info[i][6]))
            else:
                messagebox.showerror("Error", result)


    def Nurse(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        ID = ctk.StringVar()
        ID_ = ctk.StringVar()
        Name = ctk.StringVar()
        Department = ctk.StringVar()
        Department_ = ctk.StringVar()
        Status = ctk.IntVar()
        Status_ = ctk.IntVar()
        isMaster = ctk.IntVar()
        isMaster_ = ctk.IntVar()
        frame = ctk.CTkFrame(self.frame2)
        frame.pack(expand="yes")


        ctk.CTkLabel(master=frame, text='ID').grid(row=0, column=0, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text='Name').grid(row=0, column=1, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text="Department").grid(row=0, column=2, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text="Status").grid(row=0, column=3, padx=10, pady=12)
        ctk.CTkLabel(master=frame, text="isMaster").grid(row=0, column=4, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID, width=100).grid(
            row=1, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=ID_, width=100).grid(
            row=2, column=0, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Name, width=100).grid(
            row=1, column=1, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Department, width=100).grid(
            row=1, column=2, padx=10, pady=12)
        ctk.CTkEntry(master=frame, textvariable=Department_, width=100).grid(
            row=2, column=2, padx=10, pady=12)
        ctk.CTkCheckBox(master=frame, text="P" ,variable=Status, width=100).grid(
            row=1, column=3, padx=10, pady=12)
        ctk.CTkCheckBox(master=frame, text="A", variable=Status_, width=100).grid(
            row=2, column=3, padx=10, pady=12)
        ctk.CTkCheckBox(master=frame, text="Yes", variable=isMaster, width=100).grid(
            row=1, column=4, padx=10, pady=12)
        ctk.CTkCheckBox(master=frame, text="Yes", variable=isMaster_, width=100).grid(
            row=2, column=4, padx=10, pady=12)
        ctk.CTkButton(master=frame, text="Search", width=5, command=lambda: Search()).grid(
            row=1, column=5, padx=10, pady=12)
        ctk.CTkButton(master=frame, text='Modify', width=5, command=lambda: Modify()).grid(
            row=2, column=5, padx=10, pady=12)

        tree = ttk.Treeview(frame, show="headings", height=20)
        tree["columns"] = ("id", "email", "name", "gender", "contact number", "department", "status", "isMaster")
        tree.column("id", width=100, anchor='center')
        tree.column("email", width=100, anchor='center')
        tree.column("name", width=100, anchor='center')
        tree.column("gender", width=100, anchor='center')
        tree.column("contact number", width=150, anchor='center')
        tree.column("department", width=100, anchor='center')
        tree.column("status", width=100, anchor='center')
        tree.column("isMaster", width=100, anchor='center')
        tree.heading("id", text="ID")
        tree.heading("email", text="Email")
        tree.heading("name", text="Name")
        tree.heading("gender", text="Gender")
        tree.heading("department", text="Department")
        tree.heading("contact number", text="Contact Number")
        tree.heading("status", text="Status")
        tree.heading("isMaster", text="isMaster")
        tree.grid(row=3, column=0, columnspan=8, rowspan=5, padx=10, pady=12)
        message, Info = sql_request.universal_find_nurse('', '')
        if message == 'Success':
            tree.delete(*tree.get_children())
            for i in range(len(Info)):
                tree.insert('', i,
                            values=(Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5], Info[i][6], Info[i][7]))

        def Search():
            search_key = ''
            status = ''
            ismaster: bool = False
            if Status.get() == 1:
                status = 'P'
            if isMaster.get() == 1:
                ismaster = True
            if ID.get() != '':
                search_key = ID.get()
            elif Name.get() != '':
                search_key = Name.get()
            elif Department.get() != '':
                search_key = Department.get()
            message, Info = sql_request.universal_find_nurse(search_key, status, ismaster)
            if message == 'Success':
                tree.delete(*tree.get_children())
                for i in range(len(Info)):
                    tree.insert('', i,
                                values=(
                                Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5], Info[i][6],
                                Info[i][7]))

        def Modify():
            if Status_.get() == 1:
                status = 'A'
            else:
                status = 'P'
            if isMaster_.get() == 1:
                ismaster = True
            else:
                ismaster = False


            # 调用后端函数进行搜索
            result = sql_request.update_nurse_admin(
                int(ID_.get()),  # 获取ID
                Department_.get(),
                status,
                ismaster)

            if result == 'Success':
                messagebox.showinfo("Success", "Successfully modified")
                message, Info = sql_request.universal_find_nurse('', '')
                if message == 'Success':
                    tree.delete(*tree.get_children())
                    for i in range(len(Info)):
                        tree.insert('', i,
                                    values=(
                                    Info[i][0], Info[i][1], Info[i][2], Info[i][3], Info[i][4], Info[i][5], Info[i][6],
                                    Info[i][7]))
            else:
                messagebox.showerror("Error", result)


# TODO   管理员界面，开药方的界面，开检查单的界面，分配病房的界面（护士长），病房查看的界面，药房的界面
