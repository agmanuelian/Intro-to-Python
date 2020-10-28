# SCRIPT TO PERFORM RESTCONF OPERATIONS WITH CSR
import requests
import json
from prettytable import PrettyTable
import urllib3
from datetime import datetime
urllib3.disable_warnings()

####### GETTING OUTPUT FROM ROUTER VIA RESTCONF #######

url_csr = "https://ios-xe-mgmt.cisco.com:9443/restconf/data"

username = "developer"
password = "C1sco12345"

headers ={
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

yang_interfaces = "/ietf-interfaces:interfaces"

interfaces = requests.get(url=f"{url_csr}{yang_interfaces}", headers= headers, auth=(username, password), verify= False).json()["ietf-interfaces:interfaces"]["interface"]


interfaces_table = PrettyTable(['Interface name', 'Description', 'Enabled', 'IPAddress'])

#Printing interfaces tables
print("\nInterfaces before modification: \n")
    
for interface in interfaces:
    if "ietf-ip:ipv4" in interface:
        if "address" in interface["ietf-ip:ipv4"]: ipaddr = interface["ietf-ip:ipv4"]["address"][0]["ip"]
        else: ipaddr = "NA"
    if "description" in interface: description = interface["description"]
    else: description = "NA"

    interfaces_table.add_row([interface["name"], description, interface["enabled"],ipaddr])
        
print(interfaces_table)
####### POSTING OUTPUT TO WEBEX TEAMS ROOM ########

token = "ZDQ0NTQ0MzQtNWJmYi00YjdhLWFhMDItODBkZWI0NjNlMWYxYmUzMzEzN2QtNzVj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vNWI3YzE4NTAtYTc5MC0xMWVhLWIwMjAtMmYwMjVhNDY4OTdm"
roomId_Accenture = "Y2lzY29zcGFyazovL3VzL1JPT00vMTI3NDJiNjAtMGUzOS0xMWViLTlkNjYtMTk4N2E2NTY1NmRh"
time = datetime.now()

url = f'https://webexapis.com/v1/messages'

headers =  {'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}

body = {
    "roomId": roomId_Accenture,
    "text": f"""
    "Prueba 1234"
    {time}
    """
 }

requests.post(url=url, headers=headers, data=json.dumps(body))

