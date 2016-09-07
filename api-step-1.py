#  Author: Paula Mendez
#  Email Address: paulipotter@ksu.edu

from json import dumps, loads
import requests #http://docs.python-requests.org/en/master/user/quickstart/
import urllib3

http = urllib3.PoolManager()

token = 'ae7949f1fc1a625459e2aed8ee66b992'
github = 'https://www.github.com/paulipotter/Code-2040'
endpoint = 'http://challenge.code2040.org/api/register'

dict = {"Token": token, "github": github}
print(dict)
#r = http.request('POST', endpoint, data)

r = requests.post(endpoint, data = dumps(dict))

#req = Request(endpoint, data=dumps(dict))
#rec = loads(urlopen(req).read())['result']
result = r.text
print(dict)
print(r.raw)
print (result)
