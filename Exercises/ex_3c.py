import requests
import json

url = "http://jsonplaceholder.typicode.com/users"

users = requests.get(url=url).json()

#print(json.dumps(users, indent=2))
print("\nList of users: \n")
for user in users:
    print("- " + user["name"])
