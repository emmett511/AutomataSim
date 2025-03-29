import tkinter as tk
from tkinter import messagebox

class CreateAccountPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.program_logic = controller.program_logic
        self.master.geometry("600x400")

        tk.Label(self, text="Create Account").pack(pady=10)

        tk.Label(self, text="Username:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Create Account", command=self.create_account).pack(pady=10)
        tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage")).pack()

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success = self.program_logic.create_account(username, password)
        if success:
            messagebox.showinfo("Account Created", "Account successfully created!")
            self.controller.show_frame("LoginPage")
        else:
            messagebox.showerror("Account Creation Failed", "Invalid credentials or username taken.")
