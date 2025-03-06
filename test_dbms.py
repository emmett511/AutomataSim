from database import DBMS

db = DBMS()

# Create a test user
db.create_user("test_user", "securepassword")

# Add an automaton for the user (assuming user_id is 1)
db.add_automaton(1, "q0,q1,q2", "q0", "q2", "{'q0': {'a': 'q1'}, 'q1': {'b': 'q2'}}", "a,b")

# Retrieve automata for the user
print("Retrieving automata...")
automata = db.get_automata_by_user(1)
print("Retrieved Automata:", automata)
