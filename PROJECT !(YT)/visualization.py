import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('youtube_channel_data.csv')  # Replace with your actual file name
plt.figure(figsize=(12, 6))  # Set the figure size
sns.histplot(df['YouTube Ads Revenue (USD)'], bins=30, kde=True)  # Histogram with KDE curve
plt.title(' Distribution of YouTube Ads Revenue (USD)')  # Title
plt.xlabel('YouTube Ads Revenue (USD)')        # X-axis label
plt.ylabel('Frequency')                       # Y-axis label
plt.show()                                    # Display the plot