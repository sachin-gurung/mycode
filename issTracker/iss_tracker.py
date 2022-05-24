#!/usr/bin/env python3
"""ISS Tracker location"""
import datetime
import requests
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    response= requests.get(URL).json()

    epoch_time = response["timestamp"]
    ts=datetime.datetime.fromtimestamp(epoch_time)

    print(f"""
CURRENT LOCATION OF THE ISS:
{ts}
Lon: {response["iss_position"]["longitude"]}
Lat: {response["iss_position"]["latitude"]}"""
    )

if __name__ == "__main__":
    main()

