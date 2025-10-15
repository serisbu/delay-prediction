import requests
import zipfile
import os

def download_mbta_bus_data():
    # URLs of the ZIP files
    mbta_2024_url = "https://www.arcgis.com/sharing/rest/content/items/96c77138c3144906bce93d0257531b6a/data"
    mbta_2025_url = "https://www.arcgis.com/sharing/rest/content/items/924df13d845f4907bb6a6c3ed380d57a/data"


    mbta_2024_name = "data/MBTA_Bus_Arrival_Departure_Times_2024"
    mbta_2025_name = "data/MBTA_Bus_Arrival_Departure_Times_2025"

    data = {mbta_2024_name: mbta_2024_url, mbta_2025_name: mbta_2025_url}

    for name,url in data.items():

        if not os.path.exists(f"{name}.zip"):

            print(f"Downloading {name}")
            response = requests.get(url)
            print("Download complete.")

            if response.status_code == 200:
                # Save ZIP file to data folder
                with open(f"{name}.zip", "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {name}")

                # Extract ZIP
                with zipfile.ZipFile(f"{name}.zip", "r") as zip_ref:
                    zip_ref.extractall("./data/")
                print(f"Unzipped: {name}.zip")
            else:
                print(f"Failed to download file: {response.status_code}")

        elif not os.path.exists(name) and os.path.exists(f"{name}.zip"):
            print(f"{name}.zip already exists, skipping downloading, but unzipping")
            # Extract ZIP without downloading
            with zipfile.ZipFile(f"{name}.zip", "r") as zip_ref:
                zip_ref.extractall("./data/")
            print(f"Unzipped: {name}.zip")
        else:
            print(f"{name} folder already exists, skipping download and unzip")