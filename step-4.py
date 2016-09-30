import urllib3, ast
from json import dumps, loads

<<<<<<< HEAD
http = urllib3.PoolManager()
r = http.request('POST', "http://challenge.code2040.org/api/prefix", fields={"token": "ae7949f1fc1a625459e2aed8ee66b992"})
print(r.data)

# The following line makes sure the variable is of type Dictionary
d = ast.literal_eval(r.data.decode("utf-8"))


prefix = d.get("prefix")

# Creates the dictionary that will be sent in the second POST request
send = {"token": "ae7949f1fc1a625459e2aed8ee66b992", "array":[]}

print(prefix)

for word in d.get("array"):
    #  if word does not start with the given prefix
    if not word.startswith(prefix):
        print(word)
        send["array"].append(word) #  append word to a new array (keep order)
    else:
        print(prefix, word)

# POST request sending a Dictionary with the resulting array and my unique API token
address = "http://challenge.code2040.org/api/prefix/validate"
r = http.request('POST', address, body = dumps(send).encode('utf-8'), headers={'Content-Type':'application/json'})

#  Result from validation
print(r.data)
=======
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
>>>>>>> 973691e1b27cae316fa2f8df1e84efe5a7b58928
