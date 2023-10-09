import urllib.request, urllib.parse, urllib.error
import json
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

info = json.loads(data)
sum = 0
count = 0

for item in info["comments"]:
    count += 1
    sum += int(item["count"])
    
print("Count", count)
print("Sum", sum)