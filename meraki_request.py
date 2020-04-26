import requests 
import json

api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

url = 'https://api.meraki.com/api/v0'

headers = {
    'X-Cisco-Meraki-API-Key' : api_key
} 

#### GET ORGANIZATIONS #####

org_url = url + '/organizations'

org_req = requests.get(org_url, headers=headers).json()

print(json.dumps(org_req, indent=2))