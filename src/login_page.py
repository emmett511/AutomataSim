import tkinter as tk
from tkinter import messagebox
from program_logic import ProgramLogic

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.program_logic = controller.program_logic
        self.master.geometry("600x400")  # window size

        tk.Label(self, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=10)
        tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage")).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success = self.program_logic.login(username, password)
        if success:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            self.controller.show_frame("SimulationPage")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")
