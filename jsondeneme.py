import json

person_string = '{"name":"Ali","languages":["python","C#"]}'
result = json.loads(person_string)
print(result)
