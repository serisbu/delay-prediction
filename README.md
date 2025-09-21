# Public Transportation Delay Prediction (Proposal)
## Description
As a daily user of public transportation, with this project, I would like to predict the delay on local bus stops (line 111) and green line metro according to the current weather and time for each stop. My current plan for the prediction is to predict exact delay time. So I will use a regression model which can be a linear regression or a random forest.

## Goals
- Predict the exact delay time according to the current weather and time for each stop
- Detect anomalies in delay time under current conditions
- Simple local web app to test the model


## Data Collection
To do the prediction and anomaly detection, I will need to collect weather data (temperature, wind, weather condition) and bus/metro arrival information (the arrival time and scheduled time, the information about the stop). For bus/metro data, my current plan is to use MBTA's V3 API (https://www.mbta.com/developers). For weather information, I am planning to use National Weather Service's API (https://www.weather.gov/documentation/services-web-api). According to my research, the API's are free to use with request rate limit constraints. My plan for the data collection is as the following:
- Retrieve metro information every 5 minutes (limit is 1000 request per minute with an API key. Without a key, it is around 20 per minute. I think it will be sufficient.)
- Retrieve weather information every hour (since it doesnt change to often) ( I couldnt find the rate limit, but the response from the request is going to be 4XX if rate limit is exceeded. I dont think it is going to be exceeded since the request is being made hourly)
- Use a cloud server (either AWS or Google) to retrieve data 24/7
- Either do data cleaning for the off hours or put a condition to not send request during off hours.
- Current plan for the data features are: [bus/metro stop id, delay time (actual - scheduled arrival), temp, wind, weather condition, current time]


## Modeling the Data
I will do more research on this in the upcoming next weeks for the best model selection. I am planning to use either linear regression or a random forest regressor to do the prediction. For anomaly detection, I am planning to test isolation forest's performance. My current knowledge in models is limited to ML introduction class. I will learn more about which model is a better fit for my goals until I start the training.


## Visualizing Data
I am planning to use scatter plots to visualize the data collected. Example plots can be temperature vs delay, and current time vs delay. Correlation matrices to understand the relation between features. After making the prediction, I will do predicted delay and actual delay scatter plot to see the difference. Lastly, by implementing a web app, I am planning to have a test environment where the user can pick the variables and see the model's performance/results.

## Test Plan
We have a month until midterm presentation and 2.5 months until the final. I am planning to collect data until december. For each time frame, I am planning to split the data into 70-10-20. So for the midterm, ~2weeks worth of data for training, ~1 week for validation and ~1 week for test. For final model, ~5 weeks for training, ~1 week for val and ~2 weeks for testing. So I will train the model twice (maybe more to test different modelling) and use the both results as the final comparison/analysis.
