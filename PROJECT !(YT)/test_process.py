import pandas as pd
import isodate 
import matplotlib.pyplot as plt
import seaborn as sns 
data = pd.read_csv("youtube_channel_data.csv")
print(data.head()) 
data = data.dropna(subset=['Video Duration'])
print("Rows after dropping missing durations:", len(data))
def parse_duration_safe(x):
    try:
        if isinstance(x, str):
            return isodate.parse_duration(x).total_seconds()
        else:
            return None
    except Exception as e:
        print(f"Error parsing: {x} - {e}")
        return None
data['Video Duration'] = data['Video Duration'].apply(parse_duration_safe)
data = data.dropna(subset=['Video Duration'])
print("Rows after converting durations:", len(data))
print(data[['Video Duration']].head())
