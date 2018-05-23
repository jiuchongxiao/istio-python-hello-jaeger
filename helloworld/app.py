from flask import Flask,request, render_template, redirect, url_for
# import simplejson as json
import requests
import os
import socket

import urllib
import urllib2

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1


# Connect to Redis
# redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
app = Flask(__name__)

from flask_bootstrap import Bootstrap
Bootstrap(app)



@app.route("/")
def hello():
   # try:
   #     visits = redis.incr("counter")
   # except RedisError:
   #    visits = "<i>cannot connect to Redis, counter disabled</i>"
    visits = "hahahahahhahahahahahhahahahahhaahhaha..."
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> ${visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
	
@app.route('/python-sa-noheader/info')
def portalRouteNoheader():
    # url = "http://192.168.181.99:32693/sa/info"
    url = "http://service-a:8081/sa/info"
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res
	

@app.route('/python-sa/info')
def portalRoute():
    headers = getForwardHeaders(request)
    portal = getProductReviews(headers)
    return portal
	
	
	
def getProductReviews(headers):
    ## Do not remove. Bug introduced explicitly for illustration in fault injection task
    ## TODO: Figure out how to achieve the same effect using Envoy retries/timeouts
    #url = "http://192.168.181.99:32693/sa/info"
    url = "http://service-a:8081/sa/info"
    res = requests.get(url, headers=headers, timeout=10.0)
    return res.text
    
	
	

def getForwardHeaders(request):
    headers = {}

    user_cookie = request.cookies.get("user")
    if user_cookie:
        headers['Cookie'] = 'user=' + user_cookie

    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            #print "incoming: "+ihdr+":"+val

    return headers
	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

