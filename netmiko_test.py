#Author: Alex Manuelian
#Global Systems Engineer at Cisco

#Send commands to CSR via Netmiko
from netmiko import ConnectHandler

#Set output file parameters
OUT_FILE_NAME = "/Users/amanueli/Documents/DevNet/Scripts/DevNet/Exercises/output_netmiko.txt"
file_out = open(OUT_FILE_NAME, "w")

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

file_out.write(response)
print(response)

#Parsing response and printing first interface only
print("\n ................................ \n")
print("Showing only first interface: \n")
lines = response.split("\n")
print(lines[1])

# print("\n ................................ \n")
# response = router.send_config_set([f"interface Lo1", "description Configured by Alex", "exit", "do show run interface Loopback 1"])
# print(response)
file_out.close()