import os
import requests

def retrieve_weather_data():

    ncei_2024_data_url = "https://www.ncei.noaa.gov/data/global-hourly/access/2024/72509014739.csv"
    ncei_2025_data_url = "https://www.ncei.noaa.gov/data/global-hourly/access/2025/72509014739.csv"

    if not os.path.exists(f"data/2024_72509014739.csv"):

            print(f"Downloading 2024 weather data")
            response = requests.get(url = ncei_2024_data_url)

            if response.status_code == 200:
                # Save ZIP file to data folder
                with open("data/2024_72509014739.csv", "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"Downloaded 2024 weather data")
            else:
                print(f"Failed to download file: {response.status_code}")
    else:
        print("2024 data already exists, skipping download")


    if not os.path.exists(f"data/2025_72509014739.csv"):

            print(f"Downloading 2025 weather data")
            response = requests.get(url = ncei_2025_data_url)

            if response.status_code == 200:
                # Save ZIP file to data folder
                with open("data/2025_72509014739.csv", "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"Downloaded 2025 weather data")
            else:
                print(f"Failed to download file: {response.status_code}")
    else:
        print("2025 data already exists, skipping download")
