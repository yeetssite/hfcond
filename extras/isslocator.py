import json
import urllib.request
from time import strftime, localtime
urlopen = urllib.request.urlopen

issLocation_json = "http://api.open-notify.org/iss-now.json"



issLocation_request = urlopen(issLocation_json).read() 
issLocation = json.loads(issLocation_request.decode())


api_message = issLocation["message"]
if api_message == "success":
    api_message = "[32m" + api_message + "[0m"
else:
    api_message = "[31m" + api_message + "[0m"

latitude = "[1;45;37m" + issLocation['iss_position']['latitude'] + "[0m"
longitude = "[1;44;37m" + issLocation['iss_position']['longitude'] + "[0m"
timestamp = "[1;33m" + strftime('%H:%M:%S', localtime(issLocation['timestamp'])) + "[0m"

print("API Message: " + api_message)
print("[1;34mCurrent Location of the International Space Station(ISS): [0m")
print("Longitude: " + longitude)
print("Latitude:  " + latitude)
print("[1;30mLocation recorded at " + timestamp)

