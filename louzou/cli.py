import sys
from datetime import datetime

from louzou.db import create_db, db_conn


class InvalidTimeError(Exception):
    pass


# Define the float_to_hour function
def float_to_hour(float_number):
    hours = int(float_number)
    minutes = int((float_number - hours) * 60)
    return f"{hours:02d}:{minutes:02d}"


def validate_time(time_str: str) -> None:
    split_time = time_str.split(":")
    if len(split_time) != 2:
        raise InvalidTimeError(f"{time_str} is not a valid time")

    try:
        hour = int(split_time[0])
    except ValueError:
        raise InvalidTimeError(f"{split_time[0]} is not a valid hour")

    try:
        minute = int(split_time[1])
    except ValueError:
        raise InvalidTimeError(f"{split_time[1]} is not a valid minute")

    if hour > 23 or hour < 0:
        raise InvalidTimeError(f"{time_str} is not a valid time")

    if minute > 59 or minute < 0:
        raise InvalidTimeError(f"{time_str} is not a valid time")

create_db()
conn = db_conn()
cursor = conn.cursor() 

while True:
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"{date_str} is not a valid date")
        sys.exit(1)

    medication = "Loxapac"
    hours = input("Enter intake time : ")
    try:
        validate_time(hours)
    except InvalidTimeError:
        print(f"{hours} is not a valid time")
        sys.exit(1)

    # Convert the float hours to hour format
    # hours_format = float_to_hour(hours)

    # Insert the data into the database
    cursor.execute(
        "INSERT INTO intake(date, medication, hour) VALUES (?, ?, ?)",
        (date, medication, hours)
    )
    conn.commit()


    another_entry = input("Do you want to enter another hour? (yes/no): ")
    if another_entry.lower() != 'yes':
        break

# Close the database connection
conn.close()
