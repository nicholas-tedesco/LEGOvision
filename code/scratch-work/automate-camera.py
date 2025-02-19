from picamera import PiCamera
from time import sleep
import requests
import json

## define variables
img_path = "../../data/captures/test-image.jpg"

## define camera, take picture
camera = PiCamera() 

camera.start_preview()
sleep(2)
camera.capture(img_path) 
camera.stop_preview()

# ## make API request
# brickognize_url = 'https://api.brickognize.com/predict/'
# res = requests.post(
#     brickognize_url,
#     files = {'query_image': ('/home/pi/Documents/lego-sorter/test-photos/test-pic.jpg''
# ) 
