## TEXT FILES
CSV,JSON,logs,config files are:  
+ conceptually text
+ physically bytes

So backend system must:  
1. read bytes
2. decode correctly
3. then parse

### JSON
Correct backend flow:  
```python
data = open("data.json", "rb").read() # bytes
text = data.decode("utf-8")           # str
obj = json.loads(text)                # python object

```
OR
```python
with open("data.json","r",encode="utf-8") as f:
    obj = json.loads(f)
```
### CSV
Often come from excel, many uses utf-8,latin-1, wins-1252.  
so this is wrong.  
```python
open("users.csv", "r")  #  encoding guessed
```
Correct:  
```python
open("users.csv","r", encoding = "utf-8") # if we know
```
OR  safe
```python
data = open("users.csv","rb").read()
text = data.decode("utf-8",errors="strict")
obj = json.loads(data)
```

