import urllib.request
from xml.etree.ElementTree import parse
import webbrowser
from math import cos, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))

# u = urllib.request.urlopen('http://www.meteoromania.ro/anm/prognoza-orase-xml.php')
# data = u.read()
# f = open('prognoza_5_zile.xml', 'wb')
# f.write(data)
# f.close()

doc = parse('prognoza_5_zile.xml')
root = doc.getroot()

print(root.tag, root.attrib)
for country in root:
    orase = [city.attrib['nume'] for city in country]

print(orase)

for p in root.iter('temp_min'):
    print(p.attrib, p.tag, p.text)
