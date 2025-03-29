import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.master.geometry("600x400")

        tk.Label(self, text="Welcome to Automata Simulator", font=("Arial", 16)).pack(pady=30)

        tk.Button(self, text="Log In", command=lambda: controller.show_frame("LoginPage")).pack(pady=10)
        tk.Button(self, text="Create Account", command=lambda: controller.show_frame("CreateAccountPage")).pack(pady=10)
        tk.Button(self, text="Exit", command=self.master.quit).pack(pady=10)
