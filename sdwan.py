#### GET LIST OF DEVICES CONNECTED TO VMANAGE #####
import requests 
import json
import urllib3 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url= 'https://10.10.20.90/j_security_check'

login_body= {
    'j_username': 'admin',
    'j_password': 'admin'
    }

# Session initiation
session = requests.session()
response = session.post(url, data= login_body, verify= False)

print(response)

# Get list of network devices

vm_url= 'https://10.10.20.90/dataservice/device'

devices = session.get(vm_url, verify= False).json()['data']

for device in devices:
    host_name = device['host-name']
    system_ip = device['system-ip']
    print(f'{host_name}: {system_ip}\n')
