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

print('\n')
print ('LIST OF ORGANIZATIONS')
for org in org_req:
    print (f'Name: ' + org['name'])

print('\n')

#### GET AN ORGANIZATION'S LIST OF NETWORKS #####

orgname = 'DeLab'

print (f'LIST OF NETWORKS BELONGING TO NETWORK "{orgname}"')

for org in org_req:
    if org['name'] == orgname:
        orgid = org['id']

net_url = org_url + '/' + orgid + '/networks' 

org_networks = requests.get(net_url, headers=headers).json()

for net in org_networks:
    # Print list of networks
    print (net['name'])
    if net['name'] == 'Vegas Apartment':
        netid = net['id']

print('\n')
print (f'Network ID: {netid}')

#### GET NETWORK DEVICES #####

devices_url = url + '/networks/' + netid + '/devices'

devices = requests.get(devices_url, headers=headers).json()

# for device in devices:
#     print(f'Device: '+ device['model'])
#     print(f'IP Address: ' + device['lanIp'] + '\n')

#### GET LIST OF CLIENTS CONNECTED TO THE NETWORK #####

clients_url = url + '/networks/' + netid + '/clients'

clients = requests.get(clients_url, headers=headers).json()

for client in clients:
    print(f'Client description: ' + client['description']+ '|| IP Address: ' + client['ip'])
#print(json.dumps(clients, indent=2))