import json


with open("json_example.json", "rb") as fin:
    j_loads = json.loads(fin.read())
    j_dumps= json.dumps(obj=j_loads, ensure_ascii=False, indent=4)
    print(j_dumps)
