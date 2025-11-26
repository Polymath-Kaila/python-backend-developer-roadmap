# Python dict data structure
A python dict(dictionary) is a Pythons's built in `hash table` implementation.  
It stored key-value pairs.  
#### Syntax:  

```python
person = {
    "name": "Kaila",
    "age": 19
}
```
retrieving/accessing instantly:
```python
print(person["name"])   # Kaila
```
They are fast, constant time O(1).  
```python
user ={
    "id":1,
    "username": "kaila"
}
```
#### Accessing:
```python
user["id"]
```
#### Add or modify a value:  
```python
user["email"] = "kaila@gmail.com"
```
#### Delete value: 
```python
del user["id"]
```
#### check if key exists
```python
if "age" in user:
    print(exists)
```
### Common Dict operations
#### Get with fallback
```python
age = user.get("age",0)
```
#### Iterate keys
```python
for key in user:
    print(key)
```
#### Iterate value
```python 
for value in user.values():
    print(value)
```
#### Iterate key-value pairs
```python
for key,value in user.items():
    print(key,value)
```
## Advanced 
### 1.Dictionary Comprehensions
just like we do in lists:  
```python
names = ["kaila","alex","james","amos"]
names_uper[names.upper() name for name in names]
```
we can do:
```python
names = {
    "first":"kaila",
    "second":"alex",
    "third":"james",
    "forth":"amos"
}
names = {names:name.upper() for name in names}
```
#### Backend use of dict comps:
1. clean JSON transformation
2. index rows by ID
3. build lookup tables
4. build routing maps

### 2.Using dicts as simple objects just like in javascript
```python
person = dict(name = "kaila",age=19)
```
### 3.Merging dicts
```python
a = {"x":1}
b = {"y":2}

c = {**a, **b} # c has the key value pairs of dict a and dict b
```
### 4.Nested dicts(common in JSON)
```python
user ={
    "id": 43,
    "profile":{
        "name":"kaila"
        "email":"kaila@gmail.com"

    }
}
print(user["profile"]["email"])
```
### 5.Dict preserve insertion order(python 3.7+)
The order we insert keys is the order python remembers them.  
```python
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3

print(d)
# output : {'a':1, 'b':2, 'c':3}
```
### 6.defaultdict
`from collections import defaultdict`.  
A `defaultdict` is a dict that automatically creates a default value when a missing key is accessed.  

Why it exists.  
In a normal dict,THIS fasils:
```python
d = {}
d["users"].append("kaila")  # key error
```
Because "users" doesnt exist yet.  
With `defautdict` we give it a function that creates a default value.  

Example:
```python
from collections import defaultdict

users = defaultdict(list)

users["admins"].append("kaila")
users["editors"].append("amos")

print(users)
# output:
defaultdict(<class 'list'>, {'admins': ['kaila'], 'editors': ['john']})
```
#### Backend use cases:
1. counting occurrences
2. grouping rows in db
3. accumulating logs/messages
4. storing list of things
5. API aggregation 
6. grouping items

### Counter
`from collections import Counter`
A counter automatically counts how many times each item appears.  
```python 

from collections import Counter

c = Counter(["apple", "banana", "apple", "orange"])
print(c)
c["apple"]   # 2
c.most_common(1)
# [('apple', 2)]
c["banana"] += 1  # increamenting

# output1
Counter({'apple': 2, 'banana': 1, 'orange': 1})
```
#### Backend use-cases:
1. Counting API calls per user
2. Counting errors in logs
3. Counting how many times a route is hit
4. Frequency analysis in text processing
5. Detecting brute-force attempts (count ip hits)

### ChainMap
`from collections import ChainMap`.  
A chainMap combines multiple dicts and allows us to lookup keys across all of them as if they were one dict.  

Example: `Multiple dicts stacked together`  
```python
defaults = {
    "debug":False,
    "port":8000
}
env = {
    "debug" : True
}
config = ChainMap(env,defaults)
print(config["debug"]) # True (comes from env)
print(config["port"])
```
#### Backend use-cases
1. Config layering (dev → prod → default)
2. Merging environment variables and config files
3. Simple template scopes
4. Handling nested variable scopes in interpreters
 
 ```python
 cmdline = {"port": 9090}
env = {"debug": True}
defaults = {"port": 8000, "debug": False, "host": "localhost"}

settings = ChainMap(cmdline, env, defaults)
print(settings["port"])   # 9090
print(settings["debug"])  # True
print(settings["host"])   # 'localhost'
```

