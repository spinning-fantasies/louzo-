import matplotlib.pyplot as plt
import pandas as pd

# Assuming you have a CSV file with date and medication intake data
data = pd.read_csv('intake.csv')

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Plot a time series line chart
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['hours'], marker='o', linestyle='-')
plt.title('Medication Intake Over Time')
plt.xlabel('date')
plt.ylabel('intake')
plt.grid(True)
plt.show()
