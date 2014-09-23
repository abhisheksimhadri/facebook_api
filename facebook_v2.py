import facebook
import json
                
ACCESS_TOKEN = 'CAACEdEose0cBALQ4Mo7ZAHiVIH48pfZBEB6ZCAKQKdnZApnpQK5RYNn4qzv2dZCZBFvFWipEPHqkPZArCDGcralZBxz0qZCIkmEIIjSq4rZBDl4ZA1ZBZCVcNdZCZCnF8l3W1SqrMXlwHwWmmVbjlSGJFyoRHALrqP2zTeZASYLuow0AaDdfDRnGyVCYeLSvYzIz41EpDFRT9tQs6sUiZAQZDZD'

# A helper function to pretty-print Python objects as JSON

def pp(o): 
    print json.dumps(o, indent=1)

# Create a connection to the Graph API with your access token

g = facebook.GraphAPI(ACCESS_TOKEN)

# Execute a few sample queries

print '---------------'
print 'Me'
print '---------------'
pp(g.get_object('me'))
print
print '---------------'
print 'My Friends'
print '---------------'
pp(g.get_connections('me', 'friends'))
print
print '---------------'
print 'Social Web'
print '---------------'
pp(g.request("search", {'q' : 'social web', 'type' : 'page'}))
