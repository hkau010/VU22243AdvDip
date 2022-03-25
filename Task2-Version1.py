#VU22243 AE2 Task 2
#Reading website header
#Author: John Tsun
#Date: 23/3/2022
#Version 2


import sys
import requests
from requests.auth import HTTPBasicAuth
from pdb import set_trace as bp

print("This program will get the headers of a given url")
print("It will also give some attributes of the header names")
# The target url
url = 'https://www.google.com'
print("The target url: "+url)
bp()
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
# Display the headers
headers=r.headers

print(type(headers))
print()
print(headers)
# Prepare a list to contain the header names to find
bp()
find_header_names=("Server","Date","X-Country-Code","Connection,"Content-Length")
no_name="Information not available"
print()
print("The following are the attributes of the header names \n")
for name in find_header_names:
    if name in headers:
        bp()
        print(name+': '+headers(name))
    else:
        print(name+': '+no_name)

