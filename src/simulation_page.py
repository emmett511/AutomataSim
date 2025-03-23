import tkinter as tk
from tkinter import simpledialog


class SimulationPage(tk.Frame):
    """Simulation page for inputting automata, strings, and running simulations."""
    
    def __init__(self, parent):
        super().__init__(parent)

        self.master.geometry("2000x1000")
        
        # input automata button, opens input text box popup when clicked 
        self.input_button = tk.Button(self, text="Input Automata", command=self.get_automata_input)
        self.input_button.pack(pady=200)

        # Label to display the automata string
        self.result_label = tk.Label(self, text="Automata: yet to be inputted...")
        self.result_label.pack(pady=10)

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
        
        def save_input():
            user_input = text_widget.get("1.0", "end-1c")
            if user_input:
                self.automata_description = user_input
                self.result_label.config(text=f"Automata: {user_input}")
            popup.destroy()
        # button to accept user input            
        save_button = tk.Button(popup, text="Accept", command=save_input)
        save_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulation Page")
    page = SimulationPage(root)
    page.pack(fill="both", expand=True)
    root.mainloop()