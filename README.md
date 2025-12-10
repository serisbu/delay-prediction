# Bus Delay Classification

## Project Setup Instructions
  - Clone the repository
  - Make sure "make" is installed to use the Makefile
  - Open a terminal and type the following commands:
    - If make isn't installed use the following commands in the terminal to setup your environment:
      - python3 -m venv venv
      - source venv/bin/activate (if using Linux/Mac) or .\venv\Scripts\Activate.ps1 (if using Windows)
      - pip install -r requirements.txt
    - If make is installed, type "make" to setup the environment
  - Open main.ipynb file, select your python kernel from top right as the venv
  - Run the cells in the same order to download the data and reproduce the results
  - Note: Garbage collection cells are added because of the size of the dataset being used which delete used dataframes to free memory space. Make sure to run the cells in the same order.
  - Project is developed/tested on MacOS/Windows using Python 3.14 

# Final Report
## Summary of Midterm Progress
 - Trained a Random Forest model with 0.57 accuracy using 2024 data
 - Classified delay as early/ontime/late
## Data Processing/Modelling
  - Downloading Required Data
    - MBTA 2024 - 2025 Zip Files
      - mbta_2024_url = "https://www.arcgis.com/sharing/rest/content/items/96c77138c3144906bce93d0257531b6a/data"
      - mbta_2025_url = "https://www.arcgis.com/sharing/rest/content/items/924df13d845f4907bb6a6c3ed380d57a/data"
    - Weather Data
      - 2024 - https://www.ncei.noaa.gov/data/global-hourly/access/2024/72509014739.csv
      - 2025 - https://www.ncei.noaa.gov/data/global-hourly/access/2025/72509014739.csv  - 2025-01-01 to 2025-08-27

  
  - Data Cleaning
    - Removal of None values
    - Removal of incorrect measurements

  - Total data count after cleaning: 42_160_356 
  - Feature selection and calculations
    - Features directly from dataset: "route_encoded","TMP", "wind_speed_mps", "wind_dir_deg"
    - Features calculated:
      - "day_of_week": 0-6 value assigned to Monday-Sunday
      - "is_weekend": assigned 0 or 1 value whether the day is weekday/weekend
      - "is_holiday": assigned 0 or 1 using holidays library
      - "is_rainy": Using the AA1, AA2, AA3 values from database which are precipitation amounts, calculated the raindrop for the hour
      - "hour": hour value of the bus arrival time
      - "is_morning_peak": boolean value of if arrival hour is between (7, 10) am
      - "is_evening_peak": boolean value of if arrival hour is between (16, 19)
      - "month": month of the bus service/arrival
      - "season": season as an int calculated using month
      - "route_avg_delay": average delay of the route calculated using only the training data
      - "hour_avg_delay": average delay in the service hour calculated using only the training data
      - "route_hour_avg_delay": average delay of the route in that service hour calculated using only the training data
    - Labels:
      - On Time: Bus arrived within +/- 3 minutes range of scheduled time
      - Not On Time: Bus arrived outside of 3 minute range of scheduled time
## Visualizations
  - ![Labels Plot](/plots/label_dist_final.png)
  - ![Temperature Plot](/plots/temp_dist_final.png)
  - ![Wind Plot](/plots/wind_dist_final.png)
  - ![Rainy Hours Plot](/plots/is_rainy_counts_final.png)
  - ![Performance by Day](/plots/performance_by_day_final.png)
  - ![Performance by Hour](/plots/performance_by_hour_final.png)
  - ![Delay vs Rain](/plots/delay_vs_rain_final.png)
## Results
### Model Selection and Tuning
  - Train test split of approximately 75-25
  - Used whole 2024 + half of 2025 as training
  - Model Types Attempted:
    - SVM: After letting it train for 500 minutes, I needed to manually stop (failure)
    - Logistic Regression: Tried tuning the C paramater and with different train/test splits
    - Random Forest: The paramaters I mainly tuned are n_estimators, max_depth, min_samples_split with different train/test splits

  - Tried using the GridSearchCV but my system crashed, ended up manually trying various settings

### Model Performances
  - Random Forest: [class_weight="balanced_subsample", n_estimators=250, max_depth=15, min_samples_split=20,]
  - ![Random Forest Result](/plots/rf_final.png)
  - Logistic Regression: [StandardScaler(), class_weight="balanced", solver="lbfgs", C=1.0]
  - ![Logistic Regression Result](/plots/logreg_final.png)


Note: There are code blocks like the following in between cells to do garbage collection. My system wasn't able to allocate multiple dataframes with 43 million rows. So I added the blocks to free memory space.
```
var_list = ['combined', 'train_df', 'test_df', 'df_2025_train', 'df_2025_test']

for var in var_list:
    if var in globals():
        del globals()[var]
        
gc.collect()
```

# Midterm Report
Video Link: https://www.youtube.com/watch?v=z7LYP2XCOFs

[![Midterm Presentation](https://img.youtube.com/vi/z7LYP2XCOFs/0.jpg)](https://www.youtube.com/watch?v=z7LYP2XCOFs)

## Data Processing/Modelling
- Downloading Required Data
  - MBTA 2024 - 2025 Zip Files
    - mbta_2024_url = "https://www.arcgis.com/sharing/rest/content/items/96c77138c3144906bce93d0257531b6a/data"
    - mbta_2025_url = "https://www.arcgis.com/sharing/rest/content/items/924df13d845f4907bb6a6c3ed380d57a/data"
  - Weather Data
    - 2024 - https://www.ncei.noaa.gov/data/global-hourly/access/2024/72509014739.csv
    - 2025 - https://www.ncei.noaa.gov/data/global-hourly/access/2025/72509014739.csv  - 2025-01-01 to 2025-08-27
- Data Cleaning
  - Removal of None values
  - Removal of incorrect measurements
- Feature selection and calculations
  - Features directly from dataset: "route_encoded","TMP", "wind_speed_mps", "wind_dir_deg"
  - Features calculated:
    - "day_of_week": 0-6 value assigned to Monday-Sunday
    - "is_weekend": assigned 0 or 1 value whether the day is weekday/weekend
    - "is_holiday": assigned 0 or 1 using holidays library
    - "is_rainy": Using the AA1, AA2, AA3 values from database which are precipitation amounts, calculated the raindrop for the hour
  - Labels:
    - Early: Bus arrived 2 minutes earlier than the scheduled time
    - On Time: Bus arrived within +/- 2 minutes range of scheduled time
    - Late: Bus arrived more than 2 minutes late
## Data Visualization
  - ![Labels Plot](/plots/label_dist.png)
  - ![Temperature Plot](/plots/temp_dist.png)
  - ![Wind Plot](/plots/wind_dist.png)
  - ![Rainy Hours Plot](/plots/is_rainy_counts.png)
  - ![Performance by Day](/plots/performance_by_day.png)
  - ![Performance by Hour](/plots/performance_by_hour.png)
  - ![Delay vs Rain](/plots/delay_vs_rain.png)
## Preliminary Results
Used a random forest classifier with the following hyperparameters:
  - 80%-20% training/test split for 10M rows
  - n_estimators=50,
    max_depth=20,
    class_weight="balanced"
  - ![Midterm Results](/plots/midterm_results.png)

## Next Steps
 - Increase accuracy
 - Try different classification models
 - Include 2025 datasets
# Public Transportation Delay Classification (Proposal)
## Description
As a daily user of public transportation, with this project, I would like to classify the arrival of local buses as late, early and on time depending on the  weather, time, and the day of the week for each stop. To do the classification, I will test different model types that are used in classification tasks like random forest classifier.

## Goals
- Classify the bus delay time as late/early/on time according to the current weather, day of the week and time for each stop
- Detect anomalies in delay time under current conditions
- Simple local web app to test the model (if time remains)


## Data Collection
To do the classification and anomaly detection, I will need to collect weather data (temperature, wind, weather condition) and bus arrival information (the arrival time and scheduled time, the information about the stop). For bus, my current plan is to use MBTA's public data for 2024 and 2025 (until today) (https://mbta-massdot.opendata.arcgis.com/). For weather information, I am planning to use National Centers for Environmental Informations's API to pull past weather data (https://www.ncdc.noaa.gov/cdo-web/webservices/v2). According to my research, they are free to use with request rate limit constraints. My plan for the data collection is as the following:
- Retrieve bus data and weather data from two sources
- Match the data using the date and time of the data
- Do data cleaning for off hours
- Current plan for the data features are: [bus stop id, delay time (actual - scheduled arrival), temp, wind, weather condition, current time, day_of_the_week, is_holiday, weekday/weekend, late/early/ontime]


## Modeling the Data
I will do more research on this in the upcoming next weeks for the best model selection. I am planning to use a classification model like random forest classifier to do the classification. For anomaly detection, I am planning to test isolation forest's performance. My current knowledge in models is limited to ML introduction class. I will learn more about which model is a better fit for my goals until I start the training.


## Visualizing Data
I am planning to use scatter plots to visualize the data collected. Example plots can be temperature vs delay, and current time vs delay. Correlation matrices to understand the relation between features. After making the classification, I will do predicted classification and actual classification scatter plot to see the difference. Lastly, by implementing a web app, I am planning to have a test environment where the user can pick the variables and see the model's performance/results.

## Test Plan
I am planning to split the 2024 data into 70-10-20 for training/validation/test for the midterm and see the performance. During the time between midterm and final, I will combine 2024 and 2025 data to have a larger dataset and retrain the model using the whole 2024 data and use 2025 as testing data.
