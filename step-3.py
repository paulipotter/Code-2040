#  Author: Paula Mendez
#  Email Address: paulipotter@ksu.edu

from json import dumps, loads
import requests, ast

address = "http://challenge.code2040.org/api/haystack"

dict = {"token" : "ae7949f1fc1a625459e2aed8ee66b992"}

r = requests.post(address, data = dict)
d = r.text
d = ast.literal_eval(d)

needle = d.get("needle")
haystack = d.get("haystack")

for index in range(0, len(haystack)):
	if needle == haystack[index]:
		print("Found it! at index = ", index)
		dict["needle"] = index  #  Add index to the dictionary
		address = "http://challenge.code2040.org/api/haystack/validate"
		r = requests.post(address, data = dict)
		print(r.text)
		break