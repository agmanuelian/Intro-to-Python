import requests
import json

#### LOGIN ####

url = 'https://sandboxapicdc.cisco.com:443/api/aaaLogin.json'

payload = {
    'aaaUser': {
        'attributes': {
            'name': 'admin',
            'pwd': 'ciscopsdt'
        }
    }
}

headers= {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data= json.dumps(payload), verify= False).json()

#print(json.dumps(response, indent=2))
##### PARSE TOKEN AND SET COOKIE #####
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie={}

cookie['APIC-cookie'] = token

##### GET APPLICATION PROFILE #####

#url = 'https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet.json'

headers= {'cache-control': 'no-cache'}

# response_AP = requests.get(url, headers= headers, cookies=cookie, verify= False).json()

# print(json.dumps(response_AP, indent=2))


##### GET ENDPOINT GROUP  #####

url = 'https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-Save_The_Planet/epg-web.json'

# response_epg = requests.get(url, headers= headers, cookies=cookie, verify= False).json()

# print(json.dumps(response_epg, indent=2))

 #### UPDATE ENDPOINT GROUP DESCRIPTION #####

post_payload = {
    'fvAEPg': {
        'attributes':{
            "descr": "",
            "dn": "uni/tn-Heroes/ap-Save_The_Planet/epg-web"
        }
    }
}

post_desc_epg = requests.post(url, headers= headers, data= json.dumps(post_payload), verify= False, cookies= cookie)

# Check response 
response_epg = requests.get(url, headers= headers, cookies=cookie, verify= False).json()

print(json.dumps(response_epg, indent=2))