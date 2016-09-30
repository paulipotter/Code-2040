#  Author: Paula Mendez
#  Email Address: paulipotter@ksu.edu

from json import dumps, loads
import requests #http://docs.python-requests.org/en/master/user/quickstart/
# import urllib.request as url

token = 'ae7949f1fc1a625459e2aed8ee66b992'
github = 'https://www.github.com/paulipotter/Code-2040'
endpoint = 'http://challenge.code2040.org/api/register'
method = "POST"
dict = {'token': token, "github": github}
d = dumps(dict)


# r = urllib.urlopen(endpoint, data)
r = requests.post(endpoint, d)


#req = Request(endpoint, data=dumps(dict))
#rec = loads(urlopen(req).read())['result']
result = r.text
print(d)
print(result)
