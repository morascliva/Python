#pip install requests

#import requests
#import sys

#if len(sys.argv) != 2:
#  sys.exit()

#requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" +sys.argv([1]) 
#print(response.json())

#python itunes.py weezer



#import json
#import requests
#import sys

#if len(sys.argv) != 2:
#  sys.exit()

#requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" +sys.argv([1]) 
#print(json.dumps(response.json(),indent=2))             




import json
import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

requests=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" +sys.argv([1]) 
o=response.json()
 for results in o["results"]:
     print(result["trackName"])                 
             
             
