import random
from urllib.request import urlretrieve

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://skaleway.com/_next/image?url=https%3A%2F%2Fres.cloudinary.com%2Fdixnt59y8%2Fimage%2Fupload%2Fv1691081476%2Fskaleway%2Fbfuoyuz7br3v1re24dnb.png&w=1080&q=75")

fw = open('sample.txt', 'w')
fw.write('Testing my python skills to see how far i have come over the past days \n')
fw.write("Rice and beans are my favorite")
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)