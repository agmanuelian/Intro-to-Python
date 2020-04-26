import requests 
from requests.auth import HTTPBasicAuth

# Credentials
user = 'demo'
pwd = 'demo1234!'

url_auth = 'https://dcloud-dna-center-inst-sjc.cisco.com/dna/system/api/v1/auth/token'

###### GET AUTH TOKEN #####
headers = {
    'Content-Type': 'application/json'
    #'Authorization': 'Basic ZGVtbzpkZW1vMTIzNCE='
}

auth_response = requests.post(url_auth, headers=headers, auth= HTTPBasicAuth(user, pwd)).json()

token = auth_response['Token']

print(f'Success! Token is: {token}')



