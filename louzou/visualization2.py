import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load data
conn = sqlite3.connect('data/louzou.db')
data = pd.read_sql_query("SELECT date, hours FROM intake", conn)
print(data)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['hours'], data['date'], alpha=0.5)
plt.xlabel('hours')
plt.ylabel('date')
plt.title('Hour of Taking vs. Date')
plt.grid(True)

# Set custom x-axis tick labels for better readability
plt.xticks(range(24), ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM'], rotation=45)

plt.savefig("louzou/static/intake2.png")
