import pytest
from database import DBMS

@pytest.fixture
def db():
    """Fixture to set up and return a fresh DBMS instance."""
    db_instance = DBMS()
    
    # Ensure fresh test setup (optional: comment out if you want persistent test data)
    conn = db_instance.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM AUTOMATA")  # Clear automata table
    cursor.execute("DELETE FROM USER")  # Clear user table
    conn.commit()
    conn.close()
    
    return db_instance

def test_create_user(db):
    """Test user creation in the database."""
    db.create_user("test_user", "securepassword")

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER WHERE username = ?", ("test_user",))
    user = cursor.fetchone()
    conn.close()

    assert user is not None
    assert user[1] == "test_user"  # Username column
    assert len(user[2]) == 64  # Hashed password should be a SHA-256 hash (64 characters)

def test_duplicate_user(db):
    """Test that creating a duplicate user is not allowed."""
    db.create_user("test_user", "securepassword")
    db.create_user("test_user", "securepassword")  # Should fail

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM USER WHERE username = ?", ("test_user",))
    count = cursor.fetchone()[0]
    conn.close()

    assert count == 1  # Should only be one entry for "test_user"

def test_add_automaton(db):
    """Test adding an automaton to the database."""
    db.create_user("test_user", "securepassword")

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM USER WHERE username = ?", ("test_user",))
    user_id = cursor.fetchone()[0]
    conn.close()

    db.add_automaton(user_id, "q0,q1,q2", "q0", "q2", "{'q0': {'a': 'q1'}, 'q1': {'b': 'q2'}}", "a,b")

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AUTOMATA WHERE user_id = ?", (user_id,))
    automata = cursor.fetchone()
    conn.close()

    assert automata is not None
    assert automata[1] == user_id  # Foreign key reference
    assert automata[2] == "q0,q1,q2"
    assert automata[3] == "q0"
    assert automata[4] == "q2"
    assert automata[5] == "{'q0': {'a': 'q1'}, 'q1': {'b': 'q2'}}"
    assert automata[6] == "a,b"

def test_get_automata_by_user(db):
    """Test retrieving automata associated with a user."""
    db.create_user("test_user", "securepassword")

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM USER WHERE username = ?", ("test_user",))
    user_id = cursor.fetchone()[0]
    conn.close()

    db.add_automaton(user_id, "q0,q1,q2", "q0", "q2", "{'q0': {'a': 'q1'}, 'q1': {'b': 'q2'}}", "a,b")

    automata = db.get_automata_by_user(user_id)
    
    assert len(automata) == 1
    assert automata[0][1] == user_id  # Ensure automaton belongs to correct user
    assert automata[0][2] == "q0,q1,q2"

def test_no_automata_for_user(db):
    """Test that retrieving automata for a user with no automata returns an empty list."""
    db.create_user("empty_user", "password")
    
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM USER WHERE username = ?", ("empty_user",))
    user_id = cursor.fetchone()[0]
    conn.close()

    automata = db.get_automata_by_user(user_id)

    assert automata == []  # Should be an empty list

