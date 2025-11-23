# Generator Expressions (genexp)
Same syntax as listComps, but uses parentesis() instead of square parenthesis []:  

They produce one item at a time (`lazy`) --> doeas not store full data in memory.

Generally: 
```python
result = (expression for item in iterable if condition)

```
## When to use generators:
+ processing big logs(large data)
+ reading files line-by-line
+ handling streaming data
+ streaming responses, chunck by chunk
+ memory is important ie avoid loading everything 
+ you only iterate once
+ feeding functions like sum(),any(),max()

### 1.streaming lines of a file:
```python
lines = (line.strip() for line in open("access.log"))
errors = (l for l in lines if "ERROR" in l)
```
### 2.find if any user is admin
```python
user_isAdmin = any(u.role == "admin" for u in users)

```
### 3.calculate total order amount
```python
total = sum(o.amount for o in orders)
```


--------------------------------------------------------------------------------------
## genexp with `sum`,`max`,`any`
Backend patter:
```python
total = sum(order.amount for order in orders)
has_admin = any(u.role == "admin" for u in users)
max_age = max(u.age for u in users)
```

------------------------------------------------------------------------------------

## choosing between ListComp vs GenExp guide:

|        Need            |  use   |
|------------------------|--------|
|must sore data for reuse|ListComp|
|only iterating once     |GenExp  |
|Memory efficiency needed|GenExp  |
|small to medium dataset |ListComp|
|large files/stream/log  |GenExp  |
|need indexing/slicing   |ListComp|
|feeding a function sum  |GenExp  |
|building API response   |ListComp|
|building SQL parameter  |ListComp|
|filtering huge sequences|GenExp  |


### NOTE:
1. We use `ListComp` when we need a list.
2. We use GenExp when we need a stream