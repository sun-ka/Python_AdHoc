from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = " http://py4e-data.dr-chuck.net/comments_1833318.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
tags = soup('span')
sum = 0
count = 0
for tag in tags:
    count += 1
    sum += int(tag.contents[0])
    
print("Count", count)
print("Sum", sum)