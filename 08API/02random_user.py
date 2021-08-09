import requests
import json

URL="https://randomuser.me/api/"

res=requests.get(URL)
print(res.status_code)
data=json.loads(res.text)
print(data['results'][0]['name']['first'])