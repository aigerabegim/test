"""
import json
JSON - Javascript Object Notation

dump | dumps 
load | loads

Python              JSON
dict                object
list, tuple         array
str                 string
int                 integer
float               float
True/False          true/false
"""

# import json

# languages = {
#     'id: 0': {
#         'language': 'Python',
#         'weeks': 13
#     },
#     'id: 1': {
#         'language': 'JavaScript',
#         'weeks': 13
#     }
# }

# groups = {
#     'id 1':{
#         'title': 'Python19',
#         'nickname': 'Змейка PEPa',
#         'language': 0
#     } 
# }
# obj = {
#     'name': 'Umida',
#     'gender': 'Female',
#     'email': 'Umida@gmail.com',
#     'groups': [1] 
# }

# with open('obj_info.json', mode='w') as file:
#     json.dump(obj, file, indent = 4)


# json_object = json.dumps(obj)
# # print(json_object[1:12])
# # print(type(json_object))
# python_object = json.loads(json_object)
# print(python_object['name'])
# print(type(python_object))


# with open('obj_info.json', 'r') as file:
#     print(type(json.load(file))) 



import requests
import json 

URL = 'https://jsonplaceholder.typicode.com/posts'

def get_response(url: str):
    response = requests.get(url)
    return response.text #response.json()

def load_python_object(response: str):
    return json.loads(response)

response = get_response(URL)
python_obj = load_python_object(response)
# print(python_obj[1]['body']) 

for obj in python_obj:
    print(obj['title'])

class Post:

    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)
    
    def get_info(self):
        return f'{self.title} {self.body}'

obj1 = python_obj[0]
post = Post(obj1)
print(post.__dict__)
print(post.get_info())  