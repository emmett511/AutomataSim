import tkinter as tk
from tkinter import simpledialog
from program_logic import ProgramLogic

class LoginPage(tk.Frame):
    """Simulation page for inputting automata, strings, and running simulations."""
    default_input_string = "No input string inputted yet..."
    default_automata_definition = "No automata definition inputted yet..."

    def __init__(self, parent, program_logic: ProgramLogic):
        super().__init__(parent)

        # NOTE: when combining all frames together, this will need to be rethought
        self.program_logic = program_logic 

        # window size
        self.master.geometry("2000x1000") # type: ignore
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulation Page")
    page = LoginPage(root, ProgramLogic())
    page.pack(fill="both", expand=True)
    root.mainloop()