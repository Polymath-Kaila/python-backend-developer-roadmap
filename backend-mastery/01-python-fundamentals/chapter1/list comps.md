# List compressions

These are a concise,fast way to build a ``` list``` from an iterable.  
They use square parenthesis.

Generally a list comp follow this structure:
```python
result = [expression for item in iterable if condition]
```
NOTE:  
1. ` Expression` - is what we want to produce `for each item`.  
Can be ``` x * 2 ```, ``` user["name"] ``` or ```item.upper()```.  

2. `Item` is the `variable` representing each element in the iterable. 
Its the current element being processed.  
```python
x in this {for x in range(10)}
user in this {for user in users}
```
3. `Iterable` this is the source we are looping over.  
Examples:
+ `range(10)`
+ `users`
+ `request.headers`
+ `log_lines`

4. `Condition` (optional) - this is filters the `items`
Only `items` where the condition is `True` gets included. 
Examples:
+ `if x > 10`
+ `if user["active"]`
+ `if item.startswith("ERROR")`

--------------------------------------------------------------------------------------

Example without using list comps:.  

```python
result = []
for x in range(10):
    result.append(x*2)

```
Example with list comps, equivalent:.  
```python
result = [x * 2 for x in range(10)]

```

-------------------------------------------------------------------------------------

List comps are faster,cleaner and more expressive.  
They are faster because they run in `C`, not Python bytecode.

--------------------------------------------------------------------------------------

## Using list comps with MULTIPLE FOR LOOPS
```python
coordinates = [(x,y) for x in range(3) for y in range(3)]
```
Backend use:
+ building combinations configs
+ generating test matrices
+ forming permission pairs


--------------------------------------------------------------------------------------
## List comps PITFALL
List comps should NOT contain:  
+ function calls in loops that are slow
+ many nested conditions
+ DB queries
+ network calls
+ try/except inside them

Good example: 
```python
[user.name for user in users]
```
Bad example:
```python
[get_user_balance(user.id) for user in users]  #  slow!
```
Better version:
```python
balances = get_balances_bulk([u.id for u in users])

```

------------------------------------------------------------------------------------

### No mutation external state inside list comps!
To `mutate` is to change a variable,list,dictionary, or object that already exists outside the current `expression`.  
Examples of mutation:
+ `list.append()`
+ modifying a dictionary:`user["name" = "chacha"]`
+ adding/removing items from a list
+ updating couters, logs,caches

Example of wrong code:
```python
log = []
[x for x in items if log.append(x)]  # WRONG

```
Why: the condition `log.append(x)`.  
- doesn't return True/False.  
- it returns `NONE`
- so the list comp logic breaks


-------------------------------------------------------------------------------------
## REAL-WORD BACKEND EXAMPLES

### 1.Transforming API payload
```python
usernames = [u["username"] for u in users_json]
```
### 2.Filtrering records
```python
active_sessions = [s for s in sessions if not s.is_expired()]
```
### 3.Generating SQL placeholders
```python
placeholders = ",".join(["%s" for _ in ids])
```
### 4.Extracting headers
```python
lower_headers = {k.lower(): v for k, v in request.headers.items()}
```
### 5.Preparing JSON responses
```python
response["items"] = [items.to_dict() for item in page.items]
```
--------------------------------------------------------------------------------------

## When to use LisComp
1. when we need a list(must index,slice,re-use)
2. Data is small/medium sized
3. We are preparing a JSON response or API output
4. We are transforming DB query results
5. We need to reuse the processed data multiple times

--------------------------------------------------------------------------------------