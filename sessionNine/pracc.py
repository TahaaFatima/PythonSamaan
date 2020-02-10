import urllib.request
import json

req = urllib.request.urlopen("http://httpbin.org/json")
data = req.read().decode('utf-8')
print(data)

obj = json.loads(data)
print(obj['slideshow']['author'])

for slide in obj['slideshow']['slides']:
    print(slide['title'])

print(obj['slideshow']['slides'][1]['items'][1])