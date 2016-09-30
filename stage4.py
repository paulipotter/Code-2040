import urllib3, ast
from json import dumps, loads

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
