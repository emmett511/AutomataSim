import tkinter as tk
from tkinter import simpledialog
from program_logic import ProgramLogic

class SimulationPage(tk.Frame):
    """Simulation page for inputting automata, strings, and running simulations."""
    
    def __init__(self, parent, program_logic: ProgramLogic):
        super().__init__(parent)
        self.program_logic = program_logic # NOTE: when combining all frames together, this will need to be rethought
        
        # window size
        self.master.geometry("2000x1000") # type: ignore
        # input automata button, opens input text box popup when clicked 
        self.input_button = tk.Button(self, text="Input Automata", command=self.get_automata_input)
        self.input_button.pack(pady=200)
        # Label to display the automata string
        self.automata_def_label = tk.Label(self, text="No automaton inputted yet...")
        self.automata_def_label.pack(pady=10)
        # Store the automata string
        self.automata_description = "Automata yet to be inputted..."

    def get_automata_input(self):
        """Popup for user to enter automata dsl description"""
        # popup window
        popup = tk.Toplevel(self)
        popup.title("Input Automata")
        popup.geometry("800x800") 
        # text box
        text_widget = tk.Text(popup, width=60, height=20)
        text_widget.pack(padx=10, pady=10)
        # compile automata using control object
        def compile_automata():
            self.program_logic.compile_automata(text_widget.get("1.0", "end-1c"))
            self.automata_def_label.config(text=self.program_logic.current_automata)
            popup.destroy()
        # button to accept user input            
        save_button = tk.Button(popup, text="Accept", command=compile_automata)
        save_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulation Page")
    page = SimulationPage(root, ProgramLogic())
    page.pack(fill="both", expand=True)
    root.mainloop()