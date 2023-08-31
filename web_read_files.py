from urllib import request
import random

file_url = "https://www.google.com"

def online_data(new_data):
    getting = request.urlopen(new_data)
    downloading = getting.read()
    download_str = str(downloading)
    lines = download_str.split("\\n")
    print(lines)

online_data(file_url)