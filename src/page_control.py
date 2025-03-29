import tkinter as tk
from program_logic import ProgramLogic
from login_page import LoginPage
from create_account_page import CreateAccountPage
from home_page import HomePage

class AppController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Automata Simulator")
        self.geometry("600x400")

        self.program_logic = ProgramLogic()
        self.frames = {}

        # map classes to names
        page_classes = {
            "HomePage": HomePage,
            "LoginPage": LoginPage,
            "CreateAccountPage": CreateAccountPage
        }

        # Create and pack each page
        for name, PageClass in page_classes.items():
            frame = PageClass(parent=self, controller=self)
            self.frames[name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = AppController()
    app.mainloop()
