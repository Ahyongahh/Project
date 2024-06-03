import requests
from datetime import datetime

api_key = '2UZTD17EATULS029'

symbol = input("What stocks would you like to see? Write in Symbol")


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'

r = requests.get(url)
data = r.json()



time_series = data.get('Time Series (Daily)', {})


if time_series:

    latest_date = max(datetime.strptime(date, '%Y-%m-%d') for date in time_series.keys())
    latest_date_str = latest_date.strftime('%Y-%m-%d')
    latest_data = time_series[latest_date_str]

    print(f"Latest date: {latest_date_str}")
    print("Latest data:", latest_data)

else:

    print("No Data")