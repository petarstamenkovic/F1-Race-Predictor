# Imports
import os
import fastf1
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

# Load FastF1 2024 Chinese GP race session
session_2024 = fastf1.get_session(2024, 'China', 'R')
session_2024.load()

# Extract lap times
laps_2024 = session_2024.laps[["Driver", "LapTime"]].copy()
laps_2024.dropna(subset=["LapTime"], inplace=True)
laps_2024["LapTime (s)"] = laps_2024["LapTime"].dt.total_seconds()

print(laps_2024.head()) # Display the first 5 rows of the DataFrame