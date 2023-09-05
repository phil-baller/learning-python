import urllib.request

information = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for lines in information:
    data = lines.decode().strip()
    print(data)