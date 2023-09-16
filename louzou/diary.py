import sys
from datetime import datetime

from db import create_db, db_conn

create_db()
conn = db_conn()
cursor = conn.cursor() 


moods = ["Rad 👍👍👍👍", "Good 👍", "Meh 😕", "Bad 👎", "Awful 💩" ]
activities = ["Family", 
              "Friends", 
              "Date", 
              "Exercise", 
              "Sport", 
              "Relax", 
              "Coding", 
              "Cinema", 
              "Reading", 
              "Cleaning", 
              "Cooking", 
              "Sleeping early",
              "Wake up early", 
              "Eat healthy", 
              "Shopping"
            ]

while True:
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"{date_str} is not a valid date")
        sys.exit(1)


     # Prompt the user to select an activity from the list
    print("Available moods:")
    for index, activity in enumerate(activities, 1):
        print(f"{index}. {activity}")
    
    activity_choice = input("Select a mood (enter the corresponding number): ")
    try:
        activity_index= int(activity_choice)
        if 1 <= activity_index <= len(activities):
            activity = activities[activity_index - 1]
        else:
            print("Invalid activity selection. Please enter a valid number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    
    # Prompt the user to select a mood from the list
    print("Available moods:")
    for index, mood in enumerate(moods, 1):
        print(f"{index}. {mood}")
    
    mood_choice = input("Select a mood (enter the corresponding number): ")
    try:
        mood_index= int(mood_choice)
        if 1 <= mood_index <= len(moods):
            mood = moods[mood_index - 1]
        else:
            print("Invalid mood selection. Please enter a valid number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Insert the data into the database
    cursor.execute(
        "INSERT INTO activities_mood(date, activity, mood) VALUES (?, ?, ?)",
        (date, activity, mood)
    )
    conn.commit()

    another_entry = input("Do you want to enter another hour? (yes/no): ")
    if another_entry.lower() != 'yes':
        break

# Close the database connection
conn.close()
