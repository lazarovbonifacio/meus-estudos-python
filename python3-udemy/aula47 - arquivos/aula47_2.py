import json

with open('abc.json','r') as file:
    d1_json = file.read()

d1_json = json.loads(d1_json)
print(d1_json)