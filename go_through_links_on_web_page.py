from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


href = "http://py4e-data.dr-chuck.net/known_by_Valentino.html"
name = ""
count = 7
while count > 0:
    url = href
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    href = tags[17].get('href', None)
    name = tags[17].contents[0]
    count -= 1
print(name)