import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
data = pd.read_csv('youtube_channel_data.csv')
target_column = 'Estimated Revenue (USD)'

# 1. Prepare features and target
features = data.drop(['ID', 'Video Publish Time', target_column], axis=1).columns.tolist()
X = data[features]
y = data[target_column]

# 2. Encode categorical columns
X_encoded = pd.get_dummies(X)
features = X_encoded.columns.tolist()  # Update feature list

# 3. Split, train, feature importances
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

importances = model.feature_importances_
feature_importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})

# Sort and select top N features
N = 15  # Show top 15 most important features (change as needed)
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False).head(N)

# Plot
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette="viridis")
plt.title(f"Top {N} Feature Importances")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()