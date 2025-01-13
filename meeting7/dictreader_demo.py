import datetime
from csv import DictReader
from pprint import pprint

with open("data/AAPL.csv") as f:
    reader = DictReader(f)
    for item in reader:
        item["Volume"] = int(item["Volume"])
        item["Date"] = datetime.datetime.strptime(item["Date"], "%d-%m-%Y")
        pprint(item)
        break