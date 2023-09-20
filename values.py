import cbsodata
import pandas as pd

# Fetch the data and create the DataFrame
huizenprijzen = pd.DataFrame(cbsodata.get_data('82321NED'))

# Get the unique values for each column
for column in huizenprijzen.columns:
    unique_values = huizenprijzen[column].unique()
    print(f"Unique values in '{column}' column:", unique_values)