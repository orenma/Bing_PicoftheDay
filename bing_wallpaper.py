#!/usr/bin/python3

import os
import json
import urllib.request

bingurl = "https://bing.com"
homelocation = (os.path.expanduser("~"))
savedir = homelocation + "/Pictures/bing-wallpapers/"

result = os.popen("curl -s https://www.bing.com/HPImageArchive.aspx?format=js\&idx=0\&n=1").read()
print (result)
res = json.loads(result)
name = res['images'][0]['url'].split('.')[1]

fullurl = bingurl + res['images'][0]['url']

urllib.request.urlretrieve(fullurl,savedir + name + ".jpg")
