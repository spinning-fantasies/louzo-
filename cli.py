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

medications = ["Clozapine 25mg", "Clozapine 100mg", "Olanzapine 5mg", "Olanzapine 10mg" "Paroxétine 2mg", "Loxapac 150mg"]  # Add more medications as needed


while True:
    date = input("Enter date (YYYY-MM-DD): ")
    medication = "Loxapac"
    hours = float(input("Enter intake time : "))

    # Prompt the user to select a medication from the list
    print("Available medications:")
    for index, med in enumerate(medications, 1):
        print(f"{index}. {med}")
    
    medication_choice = input("Select a medication (enter the corresponding number): ")
    try:
        medication_index = int(medication_choice)
        if 1 <= medication_index <= len(medications):
            medication = medications[medication_index - 1]
        else:
            print("Invalid medication selection. Please enter a valid number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Insert the data into the database
    cursor.execute("INSERT INTO intake VALUES (?, ?, ?)", (date, medication, hours))
    conn.commit()


    another_entry = input("Do you want to enter another hour? (yes/no): ")
    if another_entry.lower() != 'yes':
        break

# Close the database connection
conn.close()
