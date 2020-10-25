# SCRIPT TO PERFORM RESTCONF OPERATIONS WITH CSR
import requests
import json
from prettytable import PrettyTable
import urllib3
urllib3.disable_warnings()

url_csr = "https://ios-xe-mgmt.cisco.com:9443/restconf/data"

username = "developer"
password = "C1sco12345"

headers ={
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

yang_interfaces = "/ietf-interfaces:interfaces"

interfaces = requests.get(url=f"{url_csr}{yang_interfaces}", headers= headers, auth=(username, password), verify= False).json()["ietf-interfaces:interfaces"]["interface"]

print("Interfaces configured:")
for interface in interfaces:
    print("- "+ interface["name"])