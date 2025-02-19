# README -------------------------------------------------------------
# 
#   file: full-workflow.py
#   goal: incorporate process to automatically capture pictures from 
#         camera, then query API for piece ID
# 
# --------------------------------------------------------------------

# packages -----------------------------------------------------------

from picamera import PiCamera 
from time import sleep
import requests 
import json 


# script parameters --------------------------------------------------

api_url = "https://api.brickognize.com/predict/"


# core algorithm -----------------------------------------------------

camera = PiCamera() 
camera.resolution = (1024, 768)

camera.start_preview() 
sleep(2) 

for i in range(3): 

    ## take picture 
    image_path = "../../data/captures/test-image_" + str(i) + ".jpg"
    camera.capture(image_path)

    ## query API 
    files = {"query_image": ("posted-brick.jpg", open(image_path, "rb"), "image/jpeg")}
    headers = {"accept": "application/json"}
    response = requests.post(api_url, headers=headers, files=files)

    ## determine most probable piece ID 
    returned_json = response.json()
    all_items = returned_json["items"]
    
    if len(all_items) > 0: 
        highest_prob_item = all_items[0]
        brick_id = highest_prob_item["id"]
    
    else: 
        brick_id = -1

    print(brick_id)

    ## wait to start next iteration 
    sleep(5) 

camera.stop_preview()