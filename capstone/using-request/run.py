#!/usr/bin/env python3

import os
import requests
from multiprocessing import Pool

URL = "http://35.192.93.59/feedback/"
DIR_PATH = "/data/feedback"
files = os.listdir(DIR_PATH)

for fname in files:
    with open(os.path.join(DIR_PATH, fname), "r") as f:
        content = f.read().strip().split("\n")
        data = {
            "title" : content[0],
            "name" : content[1],
            "date" : content[2],
            "feedback": "".join(content[3:])
        }
        print(data)
        try:
            r = requests.post(URL, json=data)
            if r.status_code != 201:
                raise requests.ConnectionError
        except requests.ConnectionError:
            print("Error while processing the request on file: ", fname)
            