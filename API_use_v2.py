import urllib.request
import urllib.parse
import json

# Find out starting and ending locations
# Obtain the directions from google API and save locally
base_url = 'https://maps.googleapis.com/maps/api/directions/json?'
origin_base = 'origin=' #Location you want to start from
origin= '1391EmpireRd'
filler1 = '&'
destination_base = 'destination='
destination= 'GatewayParkFunCenter'
key = 'key=AIzaSyCbWbe5KEMSV0UY3HJ5BEppCIUyp8Z9Brs'

url = base_url+origin_base+origin+filler1+destination_base+destination+filler1+key
print(url)
result = urllib.request.urlopen(url, data=None, )
# Result= address of data, File= Contents of url
json_file = result.read()
# print(json_file)
route_data = json.loads(json_file)

lat = 'lat'
lng = 'lng'
space = ' '
endpoints= []
startpoints= []
maneuvers= []
holder=[]
# for word in  route_data:
#    if delimiter1 in route_data:
#        z=1
# pass

routes = route_data['routes']
# print(type(routes[0]))  Is a dict
# print(type(routes[0]['legs'][0]['steps']))  Is a list
steps = routes[0]['legs'][0]['steps'] # Is a list
# print(steps)
iterations = len(steps)

# instructions_dict={latitude: , longitude: , maneuver: }

for i in range(iterations):
    holder = steps[i]['end_location']
    endpoints.append(holder)
    holder = steps[i]['start_location']
    startpoints.append(holder)
    maneuver = steps[i].get('maneuver', 0)
    maneuvers.append(maneuver)




print('startpoints= ', startpoints)
print('endpoints= ', endpoints)
print('maneuvers =' , maneuvers)
print(endpoints[1]['lat'])

new_dict=dict()
new_dict['lat']= endpoints[0]['lat']

print(new_dict)
i=0
#for i in range(iterations):
#   instructions_dict.updateendpoints[i]['lat']
#   endpoints[i]['lng']
#   maneuvers[i]


# Attempt to create data structure

class Instruction:
    def __init__(self, lat, lng, maneuver):
        self.lat = lat
        self.lng = lng
        self.maneuver = maneuver





