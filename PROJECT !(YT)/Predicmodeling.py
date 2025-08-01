import pandas as pd
from sklearn.model_selection import train_test_split

# Load your data
data = pd.read_csv('youtube_channel_data.csv')

# Clean column names (strip spaces and standardize)
data.columns = data.columns.str.strip()

# Define features and target (edit these if your CSV uses slightly different names)
features = ['Views', 'Subscribers', 'Likes', 'Shares', 'New Comments', 'Average View Percentage (%)']
target = 'Estimated Revenue (USD)'

# Check if all columns exist
missing_features = [col for col in features if col not in data.columns]
missing_target = target not in data.columns

if missing_features or missing_target:
    print("Available columns:", list(data.columns))
    if missing_features:
        print("Missing feature columns:", missing_features)
    if missing_target:
        print(f"Missing target column: {target}")
    raise ValueError("One or more required columns are missing. Please check your CSV file and column names.")

# Select features and target
X = data[features]
y = data[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Data split successful.")