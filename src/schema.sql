CREATE TABLE USER (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE AUTOMATA (
    automata_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    states TEXT NOT NULL,
    start_state TEXT NOT NULL,
    accept_states TEXT NOT NULL,
    state_transition_func TEXT NOT NULL,
    alphabet TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES USER(user_id) ON DELETE CASCADE
);
