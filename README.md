# F1 Race Predictor
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Formula%201-E10600?style=for-the-badge&logo=formula-1&logoColor=white"/>
</p>

<p align="left">
  <img src="https://github.com/user-attachments/assets/d1ef130d-338d-4351-a4ae-30635483c68c" width="800">
</p>

## Authors

- Petar Stamenković [@petarstamenkovic](https://www.github.com/petarstamenkovic )
- Aleksa Mitrovčan [@alex64a](https://www.github.com/alex64a)

## Overview
This project leverages machine learning to predict Formula 1 race outcomes, including final driver positions and fastest lap times. Developed by Petar Stamenkovic and Aleksa Mitrovcan, the project combines F1 data analysis with predictive modeling to forecast race results based on historical performance, weather conditions, and other key features.

## Key Features

* Dual Prediction Models:
  - XGBoost (Gradient Boosting): Predicts final driver positions.
  - Random Forest: Predicts fastest lap times via a derived metric called "Time Ratio."
* Data Pipeline:
  - Fetches and processes F1 data using the fastf1 Python package.
  - Handles missing values, encodes categorical features, and scales numerical data.
* Feature Engineering:
  - Includes driver skill (abbreviation), team performance, grid position, weather data (temperature, humidity, rain), and driver experience (number of races).
  - Introduces "Time Ratio" to normalize lap times across seasons, accounting for technological advancements.

## Methodology
  1. Data Collection: Uses fastf1 to retrieve race, qualifying, and weather data.
  2. Preprocessing: 
        - Encodes strings (e.g., driver names, teams) into numerical values.
        - Resolves missing data (NaN) by imputing mean values.
        - Scales features using StandardScaler and MinMaxScaler.
  3. Model Training:
        - Splits data into training/validation sets.
        - Trains XGBoost for position prediction and Random Forest for Time Ratio.
  4. Evaluation: Uses Mean Absolute Error (MAE) for performance metrics (MAE ≈ 2.96 for positions, ≈0.1 for Time Ratio).

## Results
  * Predicts race outcomes with reasonable accuracy, accounting for variables like weather and driver experience.
  * Visualizations (e.g., position rankings, lap time trends) are provided for specific races (e.g., Japanese GP 2025).

## Requirements
  * Python (Jupyter Notebook environment)
  * Libraries: fastf1, pandas, scikit-learn, XGBoost, matplotlib/seaborn for visualization.
  * Basic understanding of F1 and machine learning concepts.

## How to Use
  1. Clone the repository and install dependencies.
  2. Run the Jupyter Notebook (*.ipynb) to fetch data, train models, and generate predictions.
  3. Modify the prediction sample (e.g., race year, drivers) for custom analyses.

