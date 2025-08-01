import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_csv("youtube_channel_data.csv")
print("Dataset Info:")
print(data.info())
print("\nNull Values in Each Column:")
print(data.isnull().sum())
print("\nFirst 10 Rows of the Dataset:")
print(data.head(10))