from pprint import pprint

prices: list[dict] = []
with open("data/AAPL.csv") as f:
    header = f.readline().strip()
    fields = header.split(",")
    print(fields)
    for line in f:
        obj = {}
        for field, cell in zip(fields, line.strip().split(",")):
            obj[field] = cell
        prices.append(obj)
        # prices.append({field: cell for field, cell in zip(fields, line.split(","))})
pprint(prices[:5])

