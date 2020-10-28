#Author: Alex Manuelian
#Global Systems Engineer at Cisco
from netmiko import ConnectHandler
import requests
import json
from datetime import datetime

####### GETTING OUTPUT FROM ROUTER VIA NETMIKO #######

#Define router parameters
host= "ios-xe-mgmt.cisco.com"
username= "developer"
password= "C1sco12345"
device_type= "cisco_xe"
ssh_port= 8181
#Make Netmiko connection

router = ConnectHandler(host=host, username=username, password=password, device_type=device_type, port= ssh_port)

#Send command to display interfaces
response = router.send_command("show ip int brief")

####### POSTING OUTPUT TO WEBEX TEAMS ROOM ########

token = "ZDQ0NTQ0MzQtNWJmYi00YjdhLWFhMDItODBkZWI0NjNlMWYxYmUzMzEzN2QtNzVj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vNWI3YzE4NTAtYTc5MC0xMWVhLWIwMjAtMmYwMjVhNDY4OTdm"
roomId_Accenture = "Y2lzY29zcGFyazovL3VzL1JPT00vMTI3NDJiNjAtMGUzOS0xMWViLTlkNjYtMTk4N2E2NTY1NmRh"
time = datetime.now()

url = f'https://webexapis.com/v1/messages'

headers =  {'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}

body = {
    "roomId": roomId,
    "text": f"""
    {response}
    """
 }

requests.post(url=url, headers=headers, data=json.dumps(body))

