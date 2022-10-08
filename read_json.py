import json

with open('json_example.json', 'rb') as file:
    print(json.loads(file.read()))
