#! /usr/bin/env python3

import os
import requests
# {"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}

SOURCE = "supplier-data/descriptions/"
URL = "http://35.226.179.194/fruits/"
files = os.listdir(SOURCE)

def file_to_dict(path):
    with open(path, "r") as f:
        content = f.read().strip().split("\n")
        data = {
            "name" : content[0],
            "weight" : int(content[1].replace("lbs", "").strip()),
            "description" : "".join(content[2:]).strip(),
            "image_name" : os.path.splitext(os.path.basename(path))[0] + ".jpeg"
        }
    return data

def main():
    for fname in files:
        data = file_to_dict(os.path.join(SOURCE, fname))
        try:
            r = requests.post(URL, json=data)
            if r.status_code != 201:
                raise requests.ConnectionError
        except requests.ConnectionError:
            print("Failed to send request on: ", fname)

if __name__ == "__main__":
    main()

