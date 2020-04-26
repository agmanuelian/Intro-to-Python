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

#print(json.dumps(org_req, indent=2))

# Print list of organizations

for org in org_req:
    print (f'Name: ' + org['name'])

#### GET AN ORGANIZATION'S LIST OF NETWORKS #####

for org in org_req:
    if org['name'] == 'DevNet San Jose':
        orgid = org['id']

net_url = org_url + '/' + orgid + '/networks' 

org_networks = requests.get(net_url, headers=headers).json()

for net in org_networks:
    if net['name'] == 'Cisco Live Network':
        netid = net['id']

print (f'Network ID: {netid}')
#### GET NETWORK DEVICES #####

devices_url = url + '/networks/' + netid + '/devices'

devices = requests.get(devices_url, headers=headers).json()

for device in devices:
    if (device['model'] in device) and (device['lanIp'] in device):
        print(f'Device: '+ device['model'])
        print(f'IP Address: ' + device['lanIp'])
#print(json.dumps(devices, indent=2))
