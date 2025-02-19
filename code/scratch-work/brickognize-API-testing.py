# README ---------------------------------------------------------------------
# 
#   file: brickognize-API-testing.py
#   goal: connect to brickognize API, and see how ML classification works 
# 
# ----------------------------------------------------------------------------

# packages and test data -----------------------------------------------------

import pandas as pd
import requests 

path_to_image = "../../data/test-lego-piece.jpg"


# submit request to API ------------------------------------------------------

url = "https://api.brickognize.com/predict/"

files = {
    "query_image": ("test-lego-piece.jpg", open(path_to_image, "rb"), "image/jpeg")
}

headers = {
    "accept": "application/json"
}

response = requests.post(url, headers=headers, files=files)

print(response.json())