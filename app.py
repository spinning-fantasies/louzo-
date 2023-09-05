from flask import Flask, render_template
import sqlite3
import pdb

app = Flask(__name__)

@app.route('/')
def calendar():
    conn = sqlite3.connect('data/loxapac.db')
    cursor = conn.cursor()

    cursor.execute("SELECT date, medication, hours FROM intake")
    hours_data = cursor.fetchall()

    conn.close()

    return render_template('calendar.html', hours_data=hours_data)

if __name__ == '__main__':
    app.run(debug=True)
