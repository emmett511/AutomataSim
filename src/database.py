import sqlite3
import bcrypt

class DBMS:
    def __init__(self, db_name="automata.db"):
        self.db_name = db_name  # Just store the name, don't reinitialize DB

    def connect(self):
        """Connect to the SQLite database."""
        return sqlite3.connect(self.db_name)

    def create_user(self, username, password):
        """Create a new user with a hashed password, ensuring username is valid."""
        if not username or username.strip() == "":
            raise ValueError("Username cannot be empty or only spaces.")

        conn = self.connect()
        cursor = conn.cursor()

        # Check if username already exists
        cursor.execute("SELECT user_id FROM USER WHERE username = ?", (username,))
        if cursor.fetchone():
            conn.close()
            raise ValueError("Username already exists.")

        # Hash the password using bcrypt
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        try:
            cursor.execute("INSERT INTO USER (username, password_hash) VALUES (?, ?)", 
                           (username, password_hash))
            conn.commit()
            print(f"User '{username}' created successfully.")
        finally:
            conn.close()

    def verify_user(self, username, password):
        """Verify a user's login credentials."""
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT password_hash FROM USER WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            stored_hash = result[0]
            if bcrypt.checkpw(password.encode(), stored_hash):
                return True
        return False

    def add_automaton(self, user_id, states, start_state, accept_states, state_transition_func, alphabet):
        """Insert a new automaton into the database, ensuring all fields are valid."""
        if not all([states, start_state, accept_states, state_transition_func, alphabet]):
            raise ValueError("Automaton fields cannot be empty.")

        conn = self.connect()
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO AUTOMATA (user_id, states, start_state, accept_states, state_transition_func, alphabet) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, states, start_state, accept_states, state_transition_func, alphabet)
        )
        
        conn.commit()
        conn.close()
        print("Automaton added successfully.")

    def get_automata_by_user(self, user_id):
        """Retrieve all automata associated with a user."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM AUTOMATA WHERE user_id = ?", (user_id,))
        automata = cursor.fetchall()
        conn.close()
        return automata
