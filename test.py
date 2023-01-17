import json
from collections import deque

file = open('data.json', "r+")
queue = deque(json.load(file))
print(queue)