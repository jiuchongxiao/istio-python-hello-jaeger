import urllib
import urllib2

import requests

url = "http://192.168.181.99:32693/sa/info"

req = urllib2.Request(url)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res

print "-------------------"

response = requests.get(url)
print(response.status_code)  
print(response.url)          
print(response.headers)      
print(response.cookies)      
print(response.text)
print(response.content) 
