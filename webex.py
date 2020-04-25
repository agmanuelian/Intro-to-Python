#Script to automate different tasks on Webex teams
import requests
import json
import pprint

token = 'NDBiYmZiYzgtY2JkMC00MWU2LWE3NTUtYTE2MDcxMDg3NzYzZDhjYzJlMDctMzI2_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

#### CREATE A TEAM ######

url = 'https://api.ciscospark.com/v1/teams'
headers =  {'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}

body = {
    "name": "TEAM test"
}

# post_response = requests.post(
#     url, headers= headers, data= json.dumps(body)).json()
# print(post_response)


#### GET LIST OF TEAMS ######

get_response = requests.get(url, headers= headers).json()

# Pretty print
parsed = json.dumps(get_response, indent=2, sort_keys=True)
print (parsed)

# Get team ID
teams = get_response['items']

for team in teams:
    if team['name'] == "TEAM test":
        teamID = team['id']

#### CREATE A ROOM ###

room_url = 'https://api.ciscospark.com/v1/rooms'
room_body = {
    "title": "ROOM test",
    "teamId": teamID
}

# post_room = requests.post(
#     room_url, headers= headers, data= json.dumps(room_body)).json()

get_rooms =  requests.get(room_url, headers= headers).json()

rooms = get_rooms['items']

for room in rooms:
    if room['title'] == "ROOM test":
        roomid = room['id']
        #print (json.dumps(room, indent=2))

#### POST A MESSAGE INTO THE ROOM #####

msg_url = 'https://api.ciscospark.com/v1/messages'
msg_body= {
    "roomId": roomid,
    "text": "This is the seconde test message"
}

msg_post = requests.post(
     msg_url, headers= headers, data= json.dumps(msg_body)).json()

print (json.dumps(msg_post, indent=2))

