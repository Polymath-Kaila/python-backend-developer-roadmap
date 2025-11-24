# Pattern matching with sequence

Its lets us match the `structure` of lists,tuples,and sequence like objects.  
It uses two keywards `match` and `case`.  

When we use it python checks:  
+ How many elements in the structure?
+ What is the order?
+ Do certain values match?
+ Do variables binding fit the pattern?

Its like `destructuring`, but more powerful.

## 1.Basic sequence pattern matching:
```python
data = [10,20]
match data:
  case [x,y]:
     print("A list of two items:", x,y) #  outputs a list of two items : 10 20
```

-----------------------------------------------------------------------------------
## 2.Using Wildcards (_)
Simply means "I dont care what it is"

```python
command = ["ping","git init"]
match command:
  case ["ping", _]:
     print("ping command received")
```
--------------------------------------------------------------------------------------

## 3.Star Patterns (*rest)
Python allow us to use `*` inside our patterns matching like in unpacking

```python
data = ["sum",3,5,6,7]
match data:
  case ["sum", *nums]
    print(sum(nums))
```
### Backend usage:
+ variable-length commands
+ parsing multi-part URIs
+ extracting args from payloads

-------------------------------------------------------------------------------------

## 4.Nested Patterns

Patterns digging deaper into sequences.  

Example:  
```python
record = ["kaila",["Computer science",19]]
match record:
    case [name,["major",age]]:
       print("Name:",name)
       print("major:",major)
       print("age:",age)
""" 
output:
Name: kaila
major: Computer science
age : 19

"""
```
### Backend use:
+ parsing structured request bodies
+ matching nested DSL commands
+ structured log entries
-----------------------------------------------------------------------------------


## 5.Combining Patters with OR `(|)`
```python
shape = ["circle"]
shape = ["rectangle"]

match shape:
   case ["circle"] | ["rectangle"]:
     calculate()
```
We can compare even lists and tuples.  

--------------------------------------------------------------------------------------

## Practical Backend Scenarios

### 1.URL Routing
```python
segments = path.split("/")

match segments:
   case ["","api","users", user_id]:
      handle_user(user_id)
    case ["","api","products", product_id]
      handle_product(product_id)
```

### 2.Command Parsing
```python
match cmd.split():
    case ["GET", resource]:
        ...
    case ["POST", resource, *data]:
        ...
```

### 3.Webhook Parsing
```python
match event:
    case ["user.created", {"id": id, "email": email}]:
        ...
```
### 4.Log Parsing
```python
match log_line.split():
    case [ip, "-", method, path, status, *rest]:
        ...
```

## When to use Pattern Matching

#### We use matching when:
1. input has a shape
2. you want readable destructuring
3. conditions depend on structure
4. you’re matching nested lists/dicts
5. alternatives depend on specific layouts

#### Avoid when:

1. input structure is extremely dynamic
2. heavy logic inside a case (move to function)
3. data is huge (use streaming or slicing)