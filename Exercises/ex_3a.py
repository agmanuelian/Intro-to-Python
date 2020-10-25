import json

user_data = '''
{ "user": { "name": "john", "location": { "city": "Austin", "state": "TX" }, "roles": [ "admin", "user" ] } }
'''

user_dict = json.loads(user_data)

print(json.dumps(user_dict, indent=2))

name= user_dict["user"]["name"]
city= user_dict["user"]["location"]["city"]

print(f"His name is {name} and lives in {city}")