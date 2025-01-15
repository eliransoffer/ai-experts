# Exercise: Analyze Stock Data
# Write a function analyze_stock_data that reads a CSV file containing
# stock data for Apple and performs the following tasks:
#
# 1. Read the Data:
# The function should read the CSV file and parse the stock data
# (with columns like Date, Low, Open, Volume, High, Close, Adjusted Close).
#
# 2. Find the Highest Closing Price:
# It should find the date with the highest closing price (Close column)
# and return the date and the closing price.
#
# 3. Calculate Average Volume:
# The function should calculate and return the average trading volume (Volume column) over the period.
#
# 4. Create a Dictionary of Dates and Prices:
# It should return a dictionary where the keys are the dates (from the Date column)
# and the values are the closing prices (Close column).
#
# 5. Identify Price Increase Days:
# The function should also find the number of days when the closing price increased compared to the previous day.

# Example output:
# {
#     'highest_close': ('29-12-1980', 0.160714),
#     'average_volume': 46935422.0,
#     'price_increase_days': 5,
#     'dates_and_prices': {
#         '12-12-1980': 0.1283479928970337,
#         '15-12-1980': 0.12165199965238571,
#         '16-12-1980': 0.11272300034761429,
#         # more entries...
#     }
# }


# Requirements:
# Use the csv module to read and parse the file.
# Use dictionaries to store and return results.
# Use loops to iterate through the data and calculate values.
# Use conditions to find the highest closing price and count the price increase days.

import csv


def analyze_stock_data(file_name):
    highest_close = None
    highest_close_date = None
    total_volume = 0
    num_days = 0
    price_increase_days = 0
    dates_and_prices = {}

    # Read the CSV file
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)

        previous_close = None

        for row in reader:
            date = row['Date']
            close_price = float(row['Close'])
            volume = int(row['Volume'])

            # Task 1: Find the highest closing price and the corresponding date
            if highest_close is None or close_price > highest_close:
                highest_close = close_price
                highest_close_date = date

            # Task 2: Calculate the average volume
            total_volume += volume
            num_days += 1

            # Task 3: Create a dictionary with date and closing price
            dates_and_prices[date] = close_price

            # Task 4: Count the days with price increase
            if previous_close is not None and close_price > previous_close:
                price_increase_days += 1

            # Update previous close for next comparison
            previous_close = close_price

    # Calculate the average volume
    average_volume = total_volume / num_days if num_days > 0 else 0

    # Return the results
    return {
        'highest_close': (highest_close_date, highest_close),
        'average_volume': average_volume,
        'price_increase_days': price_increase_days,
        'dates_and_prices': dates_and_prices
    }


# Example usage:
result = analyze_stock_data("intel_stock.csv")
print(result)
