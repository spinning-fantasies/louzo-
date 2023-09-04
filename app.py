from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Define the float_to_hour function
def float_to_hour(float_number):
    hours = int(float_number)
    minutes = int((float_number - hours) * 60)
    return f"{hours:02d}:{minutes:02d}"

@app.route('/')
def calendar():
    conn = sqlite3.connect('loxapac.db')
    cursor = conn.cursor()

    cursor.execute("SELECT date, medication, hours FROM intake")
    hours_data = cursor.fetchall()

    # Convert the float hours to hour format for display
    formatted_hours_data = [(date, medication, float_to_hour(hours)) for date, medication, hours in hours_data]

    conn.close()

    return render_template('calendar.html', hours_data=formatted_hours_data)

if __name__ == '__main__':
    app.run(debug=True)
