import facebook
import json

ACCESS_TOKEN = ''

def pp(o):
    print json.dumps(o, indent=1)

g = facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data'] 
          for friend in friends }


with open('friend_likes', 'w') as outfile:
	json.dump(likes, outfile)



