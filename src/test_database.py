import pytest
import bcrypt
from database import DBMS

@pytest.fixture
def db():
    """Fixture to set up and return a fresh DBMS instance."""
    db_instance = DBMS()
    
    # Ensure fresh test setup (optional: comment out if you want persistent test data)
    conn = db_instance.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM AUTOMATA") # Clear automata table
    cursor.execute("DELETE FROM USER") # Clear user table
    conn.commit()
    conn.close()
    
    return db_instance

# 1) Fix: Test Creating a User with bcrypt Validation
def test_create_user(db):
    """Test user creation in the database."""
    db.create_user("test_user", "securepassword")

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER WHERE username = ?", ("test_user",))
    user = cursor.fetchone()
    conn.close()

    assert user is not None
    assert user[1] == "test_user" # Username column

    # Ensure the stored password hash is a bcrypt hash
    stored_hash = user[2]
    
    # Ensure it's a bcrypt hash by checking it starts with "$2b$"
    assert stored_hash.startswith(b"$2b$"), f"Expected bcrypt hash, got {stored_hash}"
    assert len(stored_hash) >= 59, f"Unexpected bcrypt hash length: {len(stored_hash)}"

# 2) Test Duplicate User Handling
def test_duplicate_user(db):
    """Test that creating a duplicate user raises a ValueError and does not insert another record."""
    db.create_user("test_user", "securepassword")
    
    # Expect ValueError when trying to create a duplicate user
    with pytest.raises(ValueError, match="Username already exists"):
        db.create_user("test_user", "securepassword") # Should fail

    # Check the database to ensure only one entry exists
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM USER WHERE username = ?", ("test_user",))
    count = cursor.fetchone()[0]
    conn.close()

    assert count == 1, f"Expected 1 user record for 'test_user', but found {count}"

# 3) Test Case Sensitivity of Usernames
def test_case_sensitive_usernames(db):
    """Test whether usernames are case-sensitive."""
    db.create_user("test_user", "password123")
    db.create_user("Test_User", "password123") # Should succeed if case-sensitive

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM USER WHERE username = 'test_user'")
    lower_case_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM USER WHERE username = 'Test_User'")
    upper_case_count = cursor.fetchone()[0]
    
    conn.close()

    assert lower_case_count == 1, "Lowercase 'test_user' was not inserted properly."
    assert upper_case_count == 1, "Uppercase 'Test_User' was not inserted properly."

# 4) Test Invalid Usernames
@pytest.mark.parametrize("username", ["", None, "  "])
def test_invalid_username(db, username):
    """Ensure that invalid usernames are not allowed."""
    with pytest.raises(Exception): # Expect failure
        db.create_user(username, "password123")

# 5) Test Adding an Automaton
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
    assert automata[1] == user_id
    assert automata[2] == "q0,q1,q2"
    assert automata[3] == "q0"
    assert automata[4] == "q2"
    assert automata[5] == "{'q0': {'a': 'q1'}, 'q1': {'b': 'q2'}}"
    assert automata[6] == "a,b"

# 6) Test Retrieving Automata
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

# 7) Test No Automata for a User
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

# 8) Test Automaton Validation (Missing Fields)
def test_add_automaton_invalid(db):
    """Test that inserting an automaton with missing fields fails."""
    db.create_user("test_user", "securepassword")

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM USER WHERE username = ?", ("test_user",))
    user_id = cursor.fetchone()[0]
    conn.close()

    # Try adding an automaton with missing fields (invalid input)
    with pytest.raises(Exception):  
        db.add_automaton(user_id, "", "q0", "q2", "", "a,b")  # Empty states and transitions

    with pytest.raises(Exception):  
        db.add_automaton(user_id, "q0,q1,q2", "", "q2", "{'q0': {'a': 'q1'}}", "a,b")  # Missing start state

# 9) Test SQL Injection Protection
def test_sql_injection_protection(db):
    """Ensure that SQL injection attempts fail."""
    malicious_username = "test_user'); DROP TABLE USER; --"
    
    db.create_user(malicious_username, "securepassword")

    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER WHERE username = ?", (malicious_username,))
    user = cursor.fetchone()
    conn.close()

    assert user is not None, "SQL injection attempt may have succeeded!"
