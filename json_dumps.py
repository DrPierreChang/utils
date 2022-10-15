import json


python_object = [{"a": [1, 2, 3]}, {"a": [1, 2, 3]},]

json_string = json.dumps(python_object)

print(type(json_string)) # <class 'str'>