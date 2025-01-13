from csv import DictReader
from datetime import datetime


def read_data(path: str) -> list[dict]:
    data: list[dict] = []
    with open(path) as f:
        reader = DictReader(f)
        for item in reader:
            item["Volume"] = int(item["Volume"])
            item["Date"] = datetime.strptime(item["Date"], "%d-%m-%Y")
            item["Close"] = float(item["Close"])
            data.append(item)
    return data

def calc_highest_close_price(data: list[dict]) -> tuple[datetime, float]:
    row_with_max_price = max(data, key=lambda row: row["Close"])
    return row_with_max_price["Date"], row_with_max_price["Close"]

if __name__ == '__main__':
    data = read_data("data/AAPL.csv")
    highest_date, highest_price = calc_highest_close_price(data)
    print(f"The sdate with highest close price is {highest_date}, price: {highest_price}")

