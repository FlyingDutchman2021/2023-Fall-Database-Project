import customtkinter as ctk

root = ctk.CTk()
root.geometry("800x800")

def Login():
    print("test")

frame = ctk.CTkFrame(master= root)
frame.pack(padx=60,pady=20,fill="both",expand=True)

label = ctk.CTkLabel(master=frame,text="Test", font=("Roboto", 24))
label.pack(pady=12,padx=10)

entry1 = ctk.CTkEntry(master=frame,placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2 = ctk.CTkEntry(master=frame,placeholder_text="Password")
entry2.pack(pady=12,padx=10)

button = ctk.CTkButton(master=frame,text="Login")
button.pack(pady=12,padx=10)



root.mainloop()