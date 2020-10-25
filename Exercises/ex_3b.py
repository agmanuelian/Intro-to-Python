import requests
import json

url = "https://sv443.net/jokeapi/v2/joke/Pun?type=twopart"

joke = requests.get(url=url).json()

#print(json.dumps(joke,indent=2))
setup = joke["setup"]
delivery= joke["delivery"]

print(f"\nSetup: {setup}")
print(f"Delivery: {delivery}")