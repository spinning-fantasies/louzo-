import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('loxapac.db')
cursor = conn.cursor()

# Create a table to store hours
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hours (
        date TEXT,
        medication TEXT,
        hours FLOAT
    )
''')
conn.commit()

while True:
    date = input("Enter date (YYYY-MM-DD) : ")
    medication = "Loxapac"
    hours = float(input("Enter intake time : "))

    # Insert the data into the database
    cursor.execute("INSERT INTO hours VALUES (?, ?, ?)", (date, medication, hours))
    conn.commit()

    another_entry = input("Do you want to enter another hour? (yes/no): ")
    if another_entry.lower() != 'yes':
        break

# Close the database connection
conn.close()
