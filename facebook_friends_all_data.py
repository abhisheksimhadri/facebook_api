import facebook
import json

ACCESS_TOKEN = ''

def pp(o):
    print json.dumps(o, indent=1)

g = facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

with open('friend_all_data', 'w') as outfile:
	json.dump(friends, outfile)
