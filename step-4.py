#  Author: Paula Mendez
#  Email Address: paulipotter@ksu.edu
#  step 3 - Code 2040

from json import dumps, loads
import requests, ast

address = "http://challenge.code2040.org/api/prefix"
token = "ae7949f1fc1a625459e2aed8ee66b992"
r = requests.post(address, data = {"token" : token})
d = ast.literal_eval(r.text)

prefix = d.get("prefix")
array = d.get("array")
send = {"token": token, "array":[]}

print(prefix)
for word in array:
	if not word.startswith(prefix):
		send["array"].append(word)
		print(word)
	else:
		print(word, prefix)
print(" ")
		
for word in send["array"]:
	print (word)

print(send["array"])
address = "http://challenge.code2040.org/api/prefix/validate"
r = requests.post(address, data= send)
print(r.text)