import json
from pprint import pprint

import requests

# response = requests.get("https://www.n12.co.il/")
# print(response.status_code)
# print(response.text)
# print(response)

# https://<server_address>:443/current_Weather?country=ISrael&city=Netany

# https://www.google.com/search?q=intel+stock&sca_esv=1e43933e99676cca&source=hp&ei=0naOZ-XqNKSJi-gP3tfsqQg&iflsig=AL9hbdgAAAAAZ46E4v9HCCeW_FsqsBoXq54h-DfIJkO4&oq=&gs_lp=Egdnd3Mtd2l6IgAqAggFMgoQABgDGOoCGI8BMgoQLhgDGOoCGI8BMgoQABgDGOoCGI8BMgoQABgDGOoCGI8BMgoQABgDGOoCGI8BMgoQABgDGOoCGI8BMgoQABgDGOoCGI8BMgoQABgDGOoCGI8BMgoQABgDGOoCGI8BMgoQABgDGOoCGI8BSJsmUABYAHABeACQAQCYAQCgAQCqAQC4AQHIAQCYAgGgAgmoAgqYAwnxBfdA2vbXudYIkgcBMaAHAA&sclient=gws-wiz


response = requests.get("https://api.chucknorris.io/jokes/random")
print(response.status_code)
pprint(response.text)
# json.loads()
data = response.json()
# pprint(data)
print(data['value'])