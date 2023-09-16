import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import pdb

conn = sqlite3.connect('data/louzou.db')
data = pd.read_sql_query("SELECT date, hours FROM intake", conn)
print(data)

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Plot a time series line chart
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['hours'], marker='o', linestyle='-')
plt.title('Medication Intake Over Time')
plt.xlabel('date')
plt.ylabel('intake')
plt.grid(True)

plt.savefig("louzou/static/intake1.png")
