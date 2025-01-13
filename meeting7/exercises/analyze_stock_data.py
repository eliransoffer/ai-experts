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
