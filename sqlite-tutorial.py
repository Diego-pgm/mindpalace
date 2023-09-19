import sqlite3

# Connect to the database
con = sqlite3.connect("tutorial.db")
print("Connection created!")

# Create the cursor object
cur = con.cursor()

try:
    # Create a table
    cur.execute("CREATE table movie(title, year, score)")
except Exception:
    print('Table already created!')

# Select the tables from sqlite_master
cur.execute("SELECT name FROM sqlite_master")
# Fetch the results
print(cur.fetchall())

# Insert values to database
cur.execute("""
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit() # DONT FORGET TO COMMIT

# Get the results 
cur.execute("SELECT * FROM movie")
cur.fetchall()

# Insert many values with executemany()
data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?,?,?)", data)
con.commit() 

# Select the year and title from the database
for row in cur.execute("Select year, title FROM movie ORDER BY year"):
    print(row)

# Close the connection
con.close()
