import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load your CSV data
csv_path = 'youtube_channel_data.csv'# <-- Replace with your actual CSV file name
try:
    data = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"Error: File '{csv_path}' not found. Please check the file path and name.")
    exit(1)

# Step 2: Print the column names to help you select the hue column
print('Revenue per 1000 Views (USD)',
    'Views',
    'Subscribers',
    'Estimated Revenue (USD)')
print(list(data.columns))
print("Subscribers")

# Step 3: Specify the columns for pairplot
columns_for_plot = [
    'Revenue per 1000 Views (USD)',
    'Views',
    'Subscribers',
    'Estimated Revenue (USD)'
]

# Print data types and check for issues
print(data[columns_for_plot].dtypes)
print(data[columns_for_plot].head())

# If everything looks good, plot:
sns.pairplot(data[columns_for_plot])
plt.show()
print("Pairplot displayed successfully.")
# Optional: Add your categorical column for hue if available
# Example: hue_column = 'Channel Type'
hue_column = 'Estimated Revenue (USD)'  # <-- Replace with your categorical column name, e.g., 'Channel Type' or 'Category'

# Step 4: Check if all columns exist
missing_cols = [col for col in columns_for_plot if col not in data.columns]
if hue_column and hue_column not in data.columns:
    missing_cols.append(hue_column)

if missing_cols:
    print(f"Error: The following columns are missing in your data: {missing_cols}")
    exit(1)

# Step 5: Create the pairplot
try:
    if hue_column:
        sns.pairplot(data[columns_for_plot + [hue_column]], hue=hue_column)
    else:
        sns.pairplot(data[columns_for_plot])
    plt.show()
    print("Pairplot displayed successfully.")
except Exception as e:
    print(f"An error occurred while plotting: {e}")