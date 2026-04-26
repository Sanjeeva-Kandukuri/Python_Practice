import json
data = {"name":"Sanjeeva", "age":21}
json_str = json.dumps(data)

parsed = json.loads(json_str)
print(parsed)