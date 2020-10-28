#Author: Alex Manuelian
#Global Systems Engineer at Ciscoimport requests 

#Getting shutdown interfaces from DNAC and posting the message on a Webex Teams room.
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime

# Credentials
user = 'devnetuser'
pwd = 'Cisco123!'

url_auth = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'

###### GET AUTH TOKEN #####
headers = {
    'Content-Type': 'application/json'
    #'Authorization': 'Basic ZGVtbzpkZW1vMTIzNCE='
}

auth_response = requests.post(url_auth, headers=headers, auth= (user, pwd)).json()

token = auth_response['Token']

#print(f'Success! Token is: {token}')

##### GET ALL INTERFACES STATE #####

url_interfaces = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/interface'

headers= {
    'x-auth-token': token
    # 'cache-control': 'no-cache',
    # 'Host': 'sanboxdnac2.cisco.com',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Connection':'keep-alive'
    }

interfaces = requests.get(url_interfaces, headers = headers).json()

#Print all the interfaces
# print(json.dumps(site_health, indent=2))
string= ""

for interface in interfaces["response"]:
    if interface["status"]=="up":
        string += "Interface " + interface["portName"] + " on " + interface["pid"] + " is up \n"

time = datetime.now()
string += f"\nLast update: {time}"
print(string)



################# POSTING OUTPUT TO WEBEX TEAMS ROOM ##################

token = "ZDQ0NTQ0MzQtNWJmYi00YjdhLWFhMDItODBkZWI0NjNlMWYxYmUzMzEzN2QtNzVj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

#roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vNWI3YzE4NTAtYTc5MC0xMWVhLWIwMjAtMmYwMjVhNDY4OTdm"
roomId_Accenture = "Y2lzY29zcGFyazovL3VzL1JPT00vMTI3NDJiNjAtMGUzOS0xMWViLTlkNjYtMTk4N2E2NTY1NmRh"

url = f'https://webexapis.com/v1/messages'

headers =  {'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}

body = {
    "roomId": roomId_Accenture,
    "text": f"{string}"
 }

requests.post(url=url, headers=headers, data=json.dumps(body))