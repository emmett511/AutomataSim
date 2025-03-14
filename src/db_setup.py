import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect("automata.db")
cursor = conn.cursor()

# Read and execute schema
try:
    with open("schema.sql", "r") as schema_file:
        schema_sql = schema_file.read()
        cursor.executescript(schema_sql)
    print("Database and tables created successfully.")
except Exception as e:
    print("Error creating tables:", e)

# Commit and close connection
conn.commit()
conn.close()

print("Database and tables created successfully.")
