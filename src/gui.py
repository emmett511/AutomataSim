import tkinter as tk
from tkinter import messagebox, simpledialog
from program_logic import ProgramLogic
from PIL import Image, ImageTk
from PIL.Image import Resampling

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.master.geometry("600x400")

        tk.Label(self, text="Welcome to Automata Simulator", font=("Arial", 16)).pack(pady=30)

        tk.Button(self, text="Log In", command=lambda: controller.show_frame("LoginPage")).pack(pady=10)
        tk.Button(self, text="Create Account", command=lambda: controller.show_frame("CreateAccountPage")).pack(pady=10)
        tk.Button(self, text="Exit", command=self.master.quit).pack(pady=10)

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


class SimulationPage(tk.Frame):
    """Simulation page for inputting automata, strings, and running simulations."""
    default_input_string = "No input string inputted yet..."
    default_automata_definition = "No automata definition inputted yet..."

    def __init__(self, parent, program_logic: ProgramLogic, controller):
        super().__init__(parent)

        # NOTE: when combining all frames together, this will need to be rethought
        self.program_logic = program_logic 

        self.controller = controller
        self.logged_in_label = tk.Label(self, text=f"Logged in as: {self.program_logic.current_user}")
        self.logged_in_label.pack(pady=5)
        tk.Button(self, text="Logout", command=self.logout).pack(pady=5)

        self.accept = None 

        # window size
        self.master.geometry("1000x500") # type: ignore
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        # input automata button, opens input text box popup when clicked 
        self.input_automata_button = tk.Button(
            button_frame, 
            text="Input Automata", 
            command=self.input_automata
            )
        self.input_automata_button.pack(side=tk.LEFT, padx=5)
        
        # input string button, opens input text box popup when clicked
        self.input_string_button = tk.Button(
            button_frame, 
            text="Input String", 
            command=self.input_string
            )
        self.input_string_button.pack(side=tk.LEFT, padx=5)
        
        # displays input string
        self.input_string_label = tk.Label(self, text=self.default_input_string)
        self.input_string_label.pack(pady=10)

        # Store the automata string
        self.automata_description = self.default_automata_definition

        # prev and next buttons
        self.bottom_button_frame = tk.Frame(self)
        self.button1 = tk.Button(self.bottom_button_frame, text="Previous state", command=self.prev)
        self.button2 = tk.Button(self.bottom_button_frame, text="Next State", command=self.next)
        self.button3 = tk.Button(self.bottom_button_frame, text="Reset to Beginning", command=self.reset)
        self.button4 = tk.Button(self.bottom_button_frame, text="Run to Complete", command=self.runToComplete)
        self.bottom_button_frame.pack(pady=10, after=button_frame)

    def check_accept(self):
        if self.accept:
            self.accept.destroy()

        if self.program_logic.current_automata.isAccepted():
            self.accept = tk.Label(self, text="The automata accepts the input string")
            self.accept.pack(pady=10)

    def display_input_info(self):
        if hasattr(self, 'input_info'):
            self.input_info.destroy()
        
        next_index = self.program_logic.current_automata.getIndex()
        try:
            next_symbol = self.program_logic.input_string[next_index]
        except IndexError:
            next_symbol = "N/A"
        
        info_text = f"Next Index: {next_index}  Next Input Symbol: {next_symbol}"
        
        self.input_info = tk.Label(self, text=info_text)
        self.input_info.pack(pady=10)

    def input_automata(self):
        """Popup for user to enter automata dsl description"""
        # popup window
        popup = tk.Toplevel(self)
        popup.title("Input Automata")
        popup.geometry("800x800") 
        # text box
        text_widget = tk.Text(popup, width=60, height=20)
        text_widget.pack(padx=10, pady=10)
        # button to accept user input       
        
        # clear automata when inputting a new one
        if hasattr(self, 'canvas'):
            self.canvas.destroy() 
     
        def compile_automata():
            self.program_logic.compile_automata(text_widget.get("1.0", "end-1c"))
            self.input_string_label.config(text="No input string inputted yet...") # reset for new automaton
            popup.destroy()

            self.program_logic.visualizeAutomata(self.program_logic.current_automata)  
            self.display_automata()

        save_button = tk.Button(popup, text="Accept", command=compile_automata)
        save_button.pack(pady=10)
        self.button1.pack_forget()
        self.button2.pack_forget()
        self.button3.pack_forget()
        self.button4.pack_forget()
        self.bottom_button_frame.pack_forget()

        if self.accept:
            self.accept.destroy()
            self.accept = None

    def input_string(self):
        if self.program_logic.valid_automata:
            popup = tk.Toplevel(self)
            popup.title("Input String")
            popup.geometry("800x800")
            text_widget = tk.Text(popup, width=60, height=20)
            text_widget.pack(padx=10, pady=10)
            # button to accept user input
            def accept_input_string():
                self.program_logic.set_input_string(text_widget.get("1.0", "end-1c"))
                self.input_string_label.config(text=self.program_logic.input_string)
                popup.destroy()
                
                # re display from start state when new valid input inputted
                self.program_logic.current_automata.set_input(self.program_logic.input_string)
                self.program_logic.visualizeAutomata(self.program_logic.current_automata)
                self.display_automata()

                self.program_logic.current_automata.set_input(self.program_logic.input_string)
                # show prev and next buttons after accepted input
                self.bottom_button_frame.pack(side=tk.BOTTOM, pady=2)
                self.button1.pack(side=tk.LEFT, padx=10)
                self.button2.pack(side=tk.LEFT, padx=10)
                self.button3.pack(side=tk.LEFT, padx=10)
                self.button4.pack(side=tk.LEFT, padx=10)
                self.display_input_info()
                
                if self.accept:
                    self.accept.destroy()
                    self.accept = None

            save_button = tk.Button(popup, text="Accept", command=accept_input_string)
            save_button.pack(pady=10)
        else:
            tk.messagebox.showerror(
                "Error", 
                "Valid automata must be inputted before inputting strings."
                )

    def display_automata(self):
        if hasattr(self, 'canvas'):
            self.canvas.destroy()
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill='both', expand=True)
        try:
            # load and bind image w/ resizing function for dynamic resizing
            self.original_image = Image.open("automata_visualization.png")
            self.canvas.bind("<Configure>", self._resize_image)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not visualize automata: {e}")

    def _resize_image(self, event):

        # Get current aspect ratio of img and canvas 
        image_ratio = self.original_image.width / self.original_image.height
        canvas_ratio = event.width / event.height

        # ensure image fits from top to bottom w/ same aspect ratio
        width, height = event.width, event.height
        if canvas_ratio > image_ratio:
            width = int(image_ratio * height) # make image skinnier
        else:
            height = int(width / image_ratio) # make image fatter

        # resize the image w/ PIL 
        resized = self.original_image.resize((width, height), Resampling.LANCZOS)
        self.automata_img = ImageTk.PhotoImage(resized)

        # place resized image into the center of the canvas
        x, y = event.width // 2, event.height // 2
        self.canvas.delete("all")
        self.canvas.create_image(x, y, anchor=tk.CENTER, image=self.automata_img)

    def prev(self):
        if self.accept:
            self.accept.destroy()
            self.accept = None
        self.program_logic.current_automata.prev_state()
        self.program_logic.visualizeAutomata(self.program_logic.current_automata)  
        self.display_automata()
        self.display_input_info()

    
    def next(self):
        self.program_logic.current_automata.next_state()
        self.program_logic.visualizeAutomata(self.program_logic.current_automata)  
        self.display_automata()
        self.display_input_info()
        self.check_accept()
        
    
    def reset(self):
        if self.accept:
            self.accept.destroy()
            self.accept = None
        self.program_logic.current_automata.reset_to_beginning()
        self.program_logic.visualizeAutomata(self.program_logic.current_automata)  
        self.display_automata()
        self.display_input_info()

    def runToComplete(self):
        self.program_logic.current_automata.run_till_complete()
        self.program_logic.visualizeAutomata(self.program_logic.current_automata)  
        self.display_automata()
        self.display_input_info()
        self.check_accept()
    
    def logout(self):
        self.program_logic.logout()
        self.program_logic.current_automata = None
        self.program_logic.valid_automata = False
        self.program_logic.valid_input_string = False
        self.automata_def_label.config(text="No automaton inputted yet...")
        self.input_string_label.config(text="No input string inputted yet...")
        if hasattr(self, 'canvas'):
            self.canvas.destroy()

        self.bottom_button_frame.pack_forget()  # hide prev/next if shown
        self.controller.show_frame("HomePage")

    def update_logged_in_user(self):
        self.logged_in_label.config(text=f"Logged in as: {self.program_logic.current_user}")


class GUI(tk.Tk):
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
            "CreateAccountPage": CreateAccountPage,
            "SimulationPage": SimulationPage
        }

        # Create and pack each page
        for name, PageClass in page_classes.items():
            if name == "SimulationPage":
                frame = PageClass(parent=self, program_logic=self.program_logic, controller=self)
            else:
                frame = PageClass(parent=self, controller=self)
            self.frames[name] = frame
            frame.place(relwidth=1, relheight=1)
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]

        # If the frame has an update method, call it when shown
        if hasattr(frame, "update_logged_in_user"):
            frame.update_logged_in_user()

        frame.tkraise()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
