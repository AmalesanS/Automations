import urllib.request
import json
import ctypes
import os.path

# Set the image directory where the image needs to be downloaded
image_directory = "C:/Users/ama/Desktop/temp/python/picture_of_the_day/"

# Call NASA api and retrieve the image url
url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&hd=true'
req = urllib.request.Request(url)
r = urllib.request.urlopen(req).read()
content = json.loads(r.decode('utf-8'))
imageUrl = content['hdurl']

# Download the image from NASA website to your local directory
imageFileName = image_directory+imageUrl[imageUrl.rfind('/')+1:]
urllib.request.urlretrieve(imageUrl, imageFileName)

# Call the Windows function and set the wallpaper
if os.path.isfile(imageFileName):
    print("Setting the wallpaper")
    SPI_SETDESKWALLPAPER = 20 
    SPIF_UPDATEINIFILE = 1
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(imageFileName) , SPIF_UPDATEINIFILE)
