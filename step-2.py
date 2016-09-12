#  Author: Paula Mendez
#  Email Address: paulipotter@ksu.edu

from json import dumps, loads
import requests

token = "ae7949f1fc1a625459e2aed8ee66b992"
address = "http://challenge.code2040.org/api/reverse"

dict = {"token": token}
str = requests.post(address, data = dict)
print(str.text)

reverse = str.text[::-1]
print(reverse)
address = "http://challenge.code2040.org/api/reverse/validate"

dict['string'] = reverse

result = requests.post(address, data = dict)