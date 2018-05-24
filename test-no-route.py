import urllib3

import requests

url = "http://192.168.181.99:32693/sa/info"

req = urllib3.PoolManager()
res_data = req.request('Get', url)
print(res_data.data)
print(res_data.status)