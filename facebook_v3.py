import facebook
import json

ACCESS_TOKEN = 'CAACEdEose0cBALQ4Mo7ZAHiVIH48pfZBEB6ZCAKQKdnZApnpQK5RYNn4qzv2dZCZBFvFWipEPHqkPZArCDGcralZBxz0qZCIkmEIIjSq4rZBDl4ZA1ZBZCVcNdZCZCnF8l3W1SqrMXlwHwWmmVbjlSGJFyoRHALrqP2zTeZASYLuow0AaDdfDRnGyVCYeLSvYzIz41EpDFRT9tQs6sUiZAQZDZD'

def pp(o): 
    print json.dumps(o, indent=1)

g = facebook.GraphAPI(ACCESS_TOKEN)

pp(g.request('search', {'q' : 'pepsi', 'type' : 'page', 'limit' : 5}))
pp(g.request('search', {'q' : 'coke', 'type' : 'page', 'limit' : 5}))

# Use the ids to query for likes

pepsi_id = '56381779049' # Could also use 'PepsiUS'
coke_id = '40796308305'  # Could also use 'CocaCola'

# A quick way to format integers with commas every 3 digits
def int_format(n): return "{:,}".format(n)

print "Pepsi likes:", int_format(g.get_object(pepsi_id)['likes'])
print "Coke likes:", int_format(g.get_object(coke_id)['likes'])
