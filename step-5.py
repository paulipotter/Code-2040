#  Author: Paula Mendez
#  Email Address: paulipotter@ksu.edu
#  step 5 - Code 2040

import urllib3, ast, iso8601
from json import dumps, loads
from datetime import datetime, timedelta


http = urllib3.PoolManager()
r = http.request('POST', "http://challenge.code2040.org/api/dating", fields={"token": "ae7949f1fc1a625459e2aed8ee66b992"})

d = ast.literal_eval(r.data.decode("utf-8"))

#*** datestamp format ***
# yyyy-mm-ddThh:mm:ssZ

#  formatted as an ISO 8601 datestamp
datestamp = iso8601.parse_date(d.get("datestamp"), 0)
print("date:", datestamp)

#number of seconds
interval = d.get("interval")
print("interval: ", interval)
#  add the interval to the date
new_date = (datestamp + timedelta(seconds = interval)).isoformat()

# return the resulting date to the API


send = {"token": "ae7949f1fc1a625459e2aed8ee66b992", "datestamp": new_date}

print(new_date)
address = "http://challenge.code2040.org/api/dating/validate"
r = http.request('POST', address, body = dumps(send).encode('utf-8'), headers={'Content-Type':'application/json'})

print(r.data)
