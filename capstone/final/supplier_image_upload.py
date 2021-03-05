#!/usr/bin/env python3
import requests, os

URL = "http://35.226.179.194/upload/"
SOURCE = "/home/student-01-7207a75628ea/supplier-data/images"
files = os.listdir(SOURCE)

file_names = [fname for fname in files if ".jpeg" in fname]

for fname in file_names:
    with open(os.path.join(SOURCE, fname), 'rb') as f:
        r = requests.post(URL, files={'file': f})