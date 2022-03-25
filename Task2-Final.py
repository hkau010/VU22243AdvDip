#VU22243 AE2 Task 2
#Reading website header
#Author: John Tsun
#Date: 24/3/2022
#Version: 5

import sys
import requests
from requests.auth import HTTPBasicAuth
from pdb import set_trace as bp

print()
print(20*"*","\n")
print("This program will get the headers of a given url")
print("It will also give some attributes of the header names")
# The target url

url = 'https://www.forbes.com'
print("The target url: ",url)
print(20*"*","\n")
try:
    r = requests.get(url)
except:
    print("Error in getting header")
    print("Statius code: ",r.status_code)
    exit()
# Check the status code
print("Successfully getting the requests")
print("Statius code: ",r.status_code)
print()
print(20*"*","\n")
# Display the headers
headers=r.headers
print("Headers of the target website:",url)
#bp()

print()
print(headers)
# Prepare a list to contain the header names to find
print()
print(20*"*","\n")
find_header_names=(
    "Server","Date",
    "X-Country-Code",
    "Connection",
    "Content-Length"
    )
#bp()
no_name="Information not available"
print()
print("The following are the attributes of the interested header names:")
#bp()
for name in find_header_names:
    if name in headers:
        print(name+' -> '+headers[name])
    else:
        print(name+' -> '+no_name)
print(20*"*","\n")
#close the session
print("Session closed")
r.close()
