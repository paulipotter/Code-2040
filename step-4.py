#  Author: Paula Mendez
#  Email Address: paulipotter@ksu.edu
#  step 3 - Code 2040

from json import dumps, loads
import requests, ast

address = "http://challenge.code2040.org/api/prefix"

dict = {"token" : "ae7949f1fc1a625459e2aed8ee66b992"}

r = requests.post(address, data = dict)
d = r.text
d = ast.literal_eval(d)

prefix = d.get("prefix")
array = d.get("array")
arr = []

print("Prefix: ", prefix)
for word in array:
	if not word.startswith(prefix):
		arr.append(word)
		print (word, prefix)

dict["array"] = arr

address = "http://challenge.code2040.org/api/prefix/validate"
r = requests.post(address, data= dict)
print(r.text)