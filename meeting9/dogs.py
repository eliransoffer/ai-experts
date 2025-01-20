from pprint import pprint

import requests

URL = "https://random.dog/woof.json"

response = requests.get(URL)
response.raise_for_status()

data = response.json()
pprint(data)

media_url: str = data['url']

response = requests.get(media_url)
media_bytes = response.content

with open(media_url.split("/")[-1], 'wb') as f:
    f.write(media_bytes)

