import sqlite3

# Define the float_to_hour function
def float_to_hour(float_number):
    hours = int(float_number)
    minutes = int((float_number - hours) * 60)
    return f"{hours:02d}:{minutes:02d}"


# Connect to the SQLite database
conn = sqlite3.connect('data/loxapac.db')
cursor = conn.cursor()

# Create a table to store hours
cursor.execute('''
    CREATE TABLE IF NOT EXISTS intake (
        date TEXT,
        medication TEXT,
        hours FLOAT
    )
''')
conn.commit()

while True:
    date = input("Enter date (YYYY-MM-DD): ")
    medication = "Loxapac"
    hours = float(input("Enter intake time : "))

    # Convert the float hours to hour format
    hours_format = float_to_hour(hours)

    # Insert the data into the database
    cursor.execute("INSERT INTO intake VALUES (?, ?, ?)", (date, medication, hours_format))
    conn.commit()


    another_entry = input("Do you want to enter another hour? (yes/no): ")
    if another_entry.lower() != 'yes':
        break

# Close the database connection
conn.close()
