import requests
import json

url="https://www.boredapi.com/api/activity"

try:
    res=requests.get(url)
    # print(res.status_code)
    # print(res.text)
    data=json.loads(res.text)
    print(type(data))
    print(data['activity'])
except BaseException as err:
    print("Incorrecct URL")


print("More lines of code")