from xml.etree.ElementTree import parse
import webbrowser
from math import cos, asin, sqrt
from get_route_22 import get_xml

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

office_latitude = 41.980262
office_longitude = -87.668452
close_range = 5

office_adress = 'https://maps.googleapis.com/maps/api/staticmap?center=' + str(office_latitude) + ',' + str(office_longitude) + '&zoom=13&size=800x800'

get_xml()
doc = parse('route22.xml')
nb_busses = []
markers_bus = '&markers=color:blue'
markers_office = '&markers=color:green'

for bus in doc.findall('bus'):
    direction = bus.findtext('d')
    lat = float(bus.findtext('lat'))
    lon = float(bus.findtext('lon'))
    if 't' in direction:
        nb_busses.append((lat, lon))
        print('direction: ', direction, ' distance: ', distance(office_latitude, office_longitude, lat, lon))
        if distance(office_latitude, office_longitude, lat, lon) < close_range:
            markers_bus = markers_bus + '|' + str(lat) + ',' + str(lon)

markers_office = markers_office + '|' + str(office_latitude) + ',' + str(office_longitude)

webbrowser.open(office_adress + markers_bus + markers_office)
