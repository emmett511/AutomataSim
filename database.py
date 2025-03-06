import sqlite3
import hashlib

class DBMS:
    def __init__(self, db_name="automata.db"):
        self.db_name = db_name
        self._initialize_database()  # Ensure tables exist on initialization

    def connect(self):
        """Connect to the SQLite database."""
        return sqlite3.connect(self.db_name)

    def _initialize_database(self):
        """Ensure necessary tables exist in the database."""
        conn = self.connect()
        cursor = conn.cursor()
        
        # Create USER table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS USER (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );
        """)

        # Create AUTOMATA table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS AUTOMATA (
            automaton_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            states TEXT NOT NULL,
            start_state TEXT NOT NULL,
            accept_states TEXT NOT NULL,
            state_transition_func TEXT NOT NULL,
            alphabet TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES USER (user_id) ON DELETE CASCADE
        );
        """)

        conn.commit()
        conn.close()

    def create_user(self, username, password):
        """Create a new user with a hashed password."""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        conn = self.connect()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO USER (username, password_hash) VALUES (?, ?)", (username, password_hash))
            conn.commit()
            print(f"User {username} created successfully.")
        except sqlite3.IntegrityError:
            print("Error: Username already exists.")
        finally:
            conn.close()

    def add_automaton(self, user_id, states, start_state, accept_states, state_transition_func, alphabet):
        """Insert a new automaton into the database."""
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
