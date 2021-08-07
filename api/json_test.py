
import json

a = '''{
    "name":"pepe",
    "surname":"Garcia"
    "age":30
}'''

b = json.loads(a)
print(b["name"])