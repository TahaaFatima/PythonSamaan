import requests
import json

r = requests.get("https://api.github.com/users/Maria-Ahmed")
lst = r.json()

print(lst['followers'])