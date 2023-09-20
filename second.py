import pandas as pd
import matplotlib.pyplot as plt

# Read the filtered data from the CSV file
filtered_data = pd.read_csv('filtered_data.csv')

# Create a line graph to visualize the data
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Jaren'], filtered_data['Aantal gedetineerden'], marker='o', linestyle='-')
plt.xlabel('Jaren')
plt.ylabel('Aantal gedetineerden')
plt.title('Jaren')
plt.xticks(rotation=45)
plt.grid(True)

# Show the graph
plt.tight_layout()
plt.show()