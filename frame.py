import tkinter.font
import customtkinter as ctk
import config

class Base_Frame:
    def __init__(self, master):
        self.tk_frame = ctk.CTkFrame(master)
        self.tk_frame.pack(fill="both",expand=True)

    def Log_In(self):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Log_In_Frame(self.tk_frame)

    def Sign_Up(self):
        for widget in self.tk_frame.winfo_children():
            widget.destroy()
        Sign_up_Frame(self.tk_frame)


class Log_In_Frame(Base_Frame):

    def __init__(self, master):
        super().__init__(master)

        self.account = ctk.StringVar()
        self.password = ctk.StringVar()
        self.frame = ctk.CTkFrame(self.tk_frame)


        ctk.CTkLabel(master=self.frame,text='Account').grid(row=0, column=0, padx=10,pady=12)
        ctk.CTkLabel(master=self.frame, text='Password').grid(row=1, column=0, padx=10,pady=12)
        ctk.CTkEntry(master=self.frame, textvariable = self.account, width=200).grid(row=0, column=1, columnspan=2, padx=10,pady=12)
        ctk.CTkEntry(master=self.frame, textvariable = self.password, width=200).grid(row=1, column=1, columnspan=2, padx=10,pady=12)
        ctk.CTkButton(master=self.frame, text="Log in", width=10).grid(row=2, column=1, padx=10,pady=12)
        ctk.CTkButton(master=self.frame, text="Sign up", width=10, command=lambda: self.Sign_Up()).grid(row=2, column=2, padx=10,pady=12)
        self.frame.pack()



        # for i in range(2):
        #     self.line.append(tk.StringVar())
        #
        #     self.entry[i].config(font=tkinter.font.Font(family=config.DEFAULT_FAMILY,
        #                                                 size=config.DEFAULT_SIZE))
        #     self.entry[i].pack(padx=10, pady=10, ipady=2)


class Sign_up_Frame(Base_Frame):
    def __init__(self, master):
        super().__init__(master)
        self.frame = self.frame = ctk.CTkFrame(self.tk_frame)




        ctk.CTkLabel(master=self.frame, text="Choose your identity",width=200).grid(row=0, column=0, columnspan=2, padx=10,pady=12)
        ctk.CTkButton(master=self.frame, text="Patient", width=10).grid(row=1, column=0, padx=10,pady=12)
        ctk.CTkButton(master=self.frame, text="Doctor", width=10).grid(row=1, column=1, padx=10,pady=12)
        ctk.CTkButton(master=self.frame, text="Back", width=5, command=lambda: self.Log_In()).grid(row=0, column=2, padx=10, pady=12)
        self.frame.pack()

