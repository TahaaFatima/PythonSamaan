import urllib.request, json

with urllib.request.urlopen("http://httpbin.org/json") as url:
    data = json.loads(url.read().decode())

extra_data = data['slideshow']['slides']
extra_data.append("{'items': ['itemtwo', 'itemtwo values'], 'title': 'Overview', 'type': 'all'}")
extra_data.append("{'items': ['itemthree', 'itemthree values'], 'title': 'Overview', 'type': 'all'}")
extra_data.append("{'items': ['itemfour', 'itemfour values'], 'title': 'Overview', 'type': 'all'}")

json_data = json.dumps(data)
print(json_data)