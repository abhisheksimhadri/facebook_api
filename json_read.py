import json
from pprint import pprint

file = open("friend_likes", "r")

d = json.load(file)

pprint(d)

file.close()


