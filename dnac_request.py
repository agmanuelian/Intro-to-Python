import requests 
from requests.auth import HTTPBasicAuth
import json

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

##### GET SITE HEALTH #####

# url_sh = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/site-health'

# headers= {
#     'x-auth-token': token,
#     # 'cache-control': 'no-cache',
#     # 'Host': 'sanboxdnac2.cisco.com',
#     # 'Accept-Encoding': 'gzip, deflate',
#     # 'Connection':'keep-alive'
#     }

# site_health = requests.get(url_sh, headers = headers).json()

# print(json.dumps(site_health, indent=2))

