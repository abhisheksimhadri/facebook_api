import facebook
import json

ACCESS_TOKEN = 'CAACEdEose0cBABP4qW5jzcIZBdD688CcObQ5FhdkbSIOdmA56snZA5NB6MMQd0W72BTmezcokZAFcNZCORkvSRD6c0TzWoHbJuSpymREqFlbpxeJePVSqnWVZCuPFVzJmv040ZAPqpiXDUpVovsejwGcFUIgjTwr5TUEpxQ5WftNZBxmDpUQG68CgGjOqk2kUJm3qtn99sGXbW4E11KIIykqEcZBGaej4V8ZD'

def pp(o):
    print json.dumps(o, indent=1)

g = facebook.GraphAPI(ACCESS_TOKEN)

friends = g.get_connections("me", "friends")['data']

with open('friend_all_data', 'w') as outfile:
	json.dump(friends, outfile)
