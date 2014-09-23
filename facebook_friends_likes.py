import facebook
import json

ACCESS_TOKEN = 'CAACEdEose0cBANh04R08vtgMxFEu7Syja5rK2vxavWQJraYSFAY05OKhkv4l0j6aiXeQTsxIppmXpiKBkLrvY5JkrYuHPeZCMGpXaJxBkLgqRqlUCBpkwhYOHfkT4L6Q3JIqZAPnlU68AQF6fFUTJT0m68yQa5YFz66JGFPb24ZBFp1985xwUbWvHDZAArTYMiv6cksM1wZDZD'

def pp(o):
    print json.dumps(o, indent=1)

g = facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data'] 
          for friend in friends }


with open('friend_likes', 'w') as outfile:
	json.dump(likes, outfile)



