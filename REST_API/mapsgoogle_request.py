import requests

url = 'http://maps.googleapis.com/maps/api/geocode/json?address=yahotyn'
response = requests.get(url)
print(response.json())
