import urllib.request
import urllib.parse
import json

# Find out starting and ending locations
# Obtain the directions from google API and save locally
base_url = 'https://maps.googleapis.com/maps/api/directions/json?'
origin_base = 'origin='                     #Location you want to start from
origin= '1391EmpireRd'                      #Starting location (for now)
filler1 = '&'                               #Filler for google API syntax
destination_base = 'destination='
destination= 'GatewayParkFunCenter'         #Destination
key = 'key=AIzaSyCbWbe5KEMSV0UY3HJ5BEppCIUyp8Z9Brs'

url = base_url+origin_base+origin+filler1+destination_base+destination+filler1+key
print(url)
result = urllib.request.urlopen(url, data=None, )
# Result= address of data, File= Contents of url
json_file = result.read()                   #Read JSON into Python
route_data = json.loads(json_file)          #Take out excess JSON crap that clogs up the screen (makes it easier for user to read)


endpoints= []                               #Array for storing lat and lng of startpoints
startpoints= []                             #Array for storing lat and lng for endpoints
maneuvers= []                               #Array for storing maneuvers
holder=[]                                   #Array used to fill the startpoint and endpoint arrays


routes = route_data['routes']               #Cuts out unnecessary JSON data
steps = routes[0]['legs'][0]['steps']
iterations = len(steps)



for i in range(iterations):                 #This loop fills in the arrays above with the relevant data that is parsed from the JSON file
    holder = steps[i]['end_location']
    endpoints.append(holder)
    holder = steps[i]['start_location']
    startpoints.append(holder)
    maneuver = steps[i].get('maneuver', 0)
    maneuvers.append(maneuver)




print('startpoints= ', startpoints)
print('endpoints= ', endpoints)
print('maneuvers =' , maneuvers)






class Instruction:                          # Data structure to organize the lat, lng, and maneuver data into one instruction
    def __init__(self, lat, lng, maneuver):
        self.lat = lat
        self.lng = lng
        self.maneuver = maneuver



directions=[]                               # Array of organized directions
for i in range(iterations):                 # This loop fills in the directions array
    directions.append(Instruction(endpoints[i]['lat'], endpoints[i]['lng'], maneuvers[i]))
    print(directions[i].lat)
    print(directions[i].lng)
    print(directions[i].maneuver)

