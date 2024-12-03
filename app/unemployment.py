# this is the app/unemployment.py file...

# LOCAL DEV (ENV VARS)

from statistics import mean

import requests
from plotly.express import line


from app.alpha_service import API_KEY

def format_pct(my_number):
    """
    Formats a decimal number as a percentage, rounded to 4 decimal places, with a percent sign.

    Param my_number (float) like 0.95555555555

    Returns (str) like '95.5556%'
    """
    return f"{(my_number * 100):.2f}%"


def fetch_unemployment_data():

    request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

    response = requests.get(request_url)

    parsed_response = response.json()

    #return parsed_response["data"]

    # we probably want to clean the data before returning it
    # including converting string values to floats
    data = parsed_response["data"]

    # we could use a traditional mapping approach and collect the data into a new empty list
    # but here we are mutating / changing the data in place. choose whatever approach you like

    #clean_data = []
    #for item in data:
    #    clean_data.append({"date": item["date"], "value": float(value)})
    #return clean_data

    for item in data:
        item["value"] = float(item["value"])

    return data



if __name__ == "__main__":


    data = fetch_unemployment_data()

    # Challenge A
    #
    # What is the most recent unemployment rate? And the corresponding date?
    # Display the unemployment rate using a percent sign.

    print("-------------------------")
    print("LATEST UNEMPLOYMENT RATE:")
    #print(data[0])
    print(f"{data[0]['value']}%", "as of", data[0]["date"])




    # Challenge B
    #
    # What is the average unemployment rate for all months during this calendar year?
    # ... How many months does this cover?


    this_year = [d for d in data if "2022-" in d["date"]]

    rates_this_year = [float(d["value"]) for d in this_year]
    #print(rates_this_year)

    print("-------------------------")
    print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
    print("NO MONTHS:", len(this_year))


    # Challenge C
    #
    # Plot a line chart of unemployment rates over time.

    dates = [d["date"] for d in data]
    rates = [float(d["value"]) for d in data]

    fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
    fig.show()