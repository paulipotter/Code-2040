#  Author: Paula Mendez
#  Email Address: paulipotter@ksu.edu
#  step 3 - Code 2040

from json import dumps, loads
import requests, ast

address = "http://challenge.code2040.org/api/prefix"
token = "ae7949f1fc1a625459e2aed8ee66b992"

# Post request should return a dictionary
r = requests.post(address, data = {"token" : token})

# The following line makes sure the variable is of type Dictionary 
d = ast.literal_eval(r.text)


prefix = d.get("prefix") 
array = d.get("array")

# Creates the dictionary that will be sent in the second POST request
send = {"token": token, "array":[]} 


for word in array:
	# If word in array does not start with prefix
	if not word.startswith(prefix):
		send["array"].append(word)  #  append word to a new array (keep order)
		

print(prefix)
print()
print(array)
print()
print(send)

# POST request sending a Dictionary with the resulting array and my unique API token
address = "http://challenge.code2040.org/api/prefix/validate"
r = requests.post(address, data=send)
print(r.text)