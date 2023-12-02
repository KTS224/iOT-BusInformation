import requests
import json
import pprint
from datetime import datetime

url = 'http://apis.data.go.kr/1613000/ArvlInfoInqireService/getSttnAcctoArvlPrearngeInfoList'
params ={'serviceKey' : '/qm3lFkgNoJJ/L3AlgXkutx7GfXq/olUy6tZOxLq3RGSUpXobOfNbeWw3lnlE9rKYa86FKFBBAN9JcDjWyHXYw==', '_type' : 'json', 'cityCode' : '34010', 'nodeId' : 'CAB285001052' }

response = requests.get(url, params=params)
# print(response.content)
data = json.loads(response.content)
# pprint.pprint(data)
items = data['response']['body']['items']['item']

print("현재시간: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("상명대학교")

for item in items:
    arrprevstationcnt = item['arrprevstationcnt']
    arrtime = item['arrtime']
    nodeid = item['nodeid']
    nodenm = item['nodenm']
    routeid = item['routeid']
    routeno = item['routeno']
    routetp = item['routetp']
    vehicletp = item['vehicletp']
    
    arrtimeDevidedBySec = int(int(arrtime)/60)

    # Print or use the extracted values as needed
    print(f"{arrprevstationcnt:>4} 정류장 {arrtimeDevidedBySec:>4}분 "
          f"{routeno:>4}번 {vehicletp:<4} 입니다.")