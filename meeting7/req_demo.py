import requests

response = requests.get("https://www.n12.co.il/")
print(response.status_code)
print(response.text)
print(response)