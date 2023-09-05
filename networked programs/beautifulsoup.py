import urllib.request, urllib.parse, urllib.error
from bs4 import beautifulsoup
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
data = urllib.request.urlopen(url, context=ctx).read()
soup = beautifulsoup(data, 'html.parser')

tags = soup('a')
for line in tags:
    print(line.get('href', None))