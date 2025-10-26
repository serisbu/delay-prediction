import os
import requests

def retrieve_weather_data():

    ncei_2024_data_url = "https://www.ncei.noaa.gov/data/global-hourly/access/2024/72509014739.csv"

    if not os.path.exists(f"data/72509014739.csv"):

            print(f"Downloading 2024 weather data")
            response = requests.get(url = ncei_2024_data_url)

            if response.status_code == 200:
                # Save ZIP file to data folder
                with open("data/72509014739.csv", "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"Downloaded 2024 weather data")
            else:
                print(f"Failed to download file: {response.status_code}")
    else:
        print("2024 data already exists, skipping download")