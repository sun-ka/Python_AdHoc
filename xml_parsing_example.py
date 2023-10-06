import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
data.decode()
tree = ET.fromstring(data)

results = tree.findall('.//count')
sum = 0
count = 0
for res in results:
    count += 1
    sum += int(res.text)
    
print("Count", count)
print("Sum", sum)