# Tuples
A `tuple` is a ligthweight,ordered collection of items.  
It is very similar to a `list` but with one crucial property:  

A tuple is `Immutable`.  
This is to mean once we create it, we cannot add,remove,or change its `elements`

Take a look at this two cases:  

1. tuple
```python

scores = (89,77,87,90)
# scores[0] = 65  this will cause an error

```
2. list
```python
scores = [89,77,87,90]
scores[0] = 65 # works
```
A tuple relates to list compressions and genexps.  
THey are all not data types.They are ways to build `sequence`

--------------------------------------------------------------------------------------

## Roles of Tuples

### 1. Tuples as Records
In databases a `record` is a row in a table.  
`fields` are the columns in the table.    
A tuple can group together `different kinds of information` that belongs to one logical object like a row in a database.  
* An `object` is just a bundle of data and behaviour.  

Example:  
```python
student = ("Kaila", 19, "Computer Science")
```
This tuple is a record:
+ index 0 --> name
+ index1 --> age
+ index 2 -->major

Acessing `fields`:
```python
name = student[0]
age = student[1]
major = student[2]

print(name,age,major)

```
### Backend Use-Cases for Tuples

#### Database rows (quick unpacking)
```python
user_id, username, email = row
```
#### Parsed config values
```python
host, port = config["DB"]
```
#### Small,fixed structures used frequently
```python
status = (200, "OK")
```


--------------------------------------------------------------------------------------
#### Unpackaging in tuples
Tuple unpackaging means:  
Python lets us assign each `element` of a tuple to a `variable` in a single step.  

Example:  
```python
point = (10, 20)
x, y = point
```
Now:  
+ x gets 10 
+ y gets 20

To ignore values during unpackaging we use `_` as a throwaway variable:  
```python
x, _ = point
# now y will not be assigned to 20
```
#### Backend use:
1. unpack DB results
2. unpack split() results
3. unpack JSON fields
4. unpack API responses


--------------------------------------------------------------------------------------
#### Extended unpackaging(*)
This allows `one variable` to collect multiple remaining items using the `*` operator

Example:  
```python
numbers = (1,2,3,4,5,6)
first,*middle,last = numbers
""" output
first - 1
middle - [2,3,4,5]
last - 6
"""
```
#### Backend use:
1. processing route segments
2. parsing commands
3. matching patterns

-------------------------------------------------------------------------------------
### 2.Tuples as IMMUTABLE LISTS
A tuple can also behave like a list that must never change.  

Think:
+ Tuple - locked list
+ List  - editable list

Example: A set of allowed roles in a system.   
```python
ALLOWED_ROLES = ("admin", "editor", "viewer")
```
we can also do it like a list:  
```python
for role in ALLOWED_ROLES:
    print(role)

print(ALLOWED_ROLES[1])  # "editor"
```

But we cannot mutate it:
```python
ALLOWED_ROLES.append("guest")   #  error
ALLOWED_ROLES[0] = "superuser"  #  error

```
--------------------------------------------------------------------------------------
#### When to use tuples instedd of lists:
-  When the data should not change
-  When using as dictionary keys
-  When the structure is fixed
-  When defining constants
-  When indexing or slicing is needed but no mutation

### N/Bs:
1. tuples are faster than lists for: creation,iteration,comparison,hashing and function return values.  
Because tuples:
+ store fixed-size metadata
+ require no resizing
+ are immutable

2. We should avoid use of tuples when dealing with mutable data.(never put mutable items inside tuples we plan to hash or treat as consts).
3. tuples are comparable: `(1,3) < (1,4)` compared `lexicographically`
Backend use:
+ sort by (status_code, time)
+ priority queues
+ version checking
+ tuple-based routing rules

----------------------------------------------------------------------------------

# Tuples — Summary (Fluent Python Ch.2.2)

Tuples serve two roles:
1. Records (fixed structures): (lat, lon), DB rows, config pairs
2. Immutable lists: fixed collections like ALLOWED_METHODS

Key features:
- Fast, immutable, lightweight
- Support unpacking, extended unpacking, nesting
- Hashable → can be dict keys or set items
- Compare lexicographically → useful for sorting/priorities
- Don’t store mutable items if tuple is used as a key

Backend Use Cases:
- Config values
- Returning multiple values
- Routing/HTTP rule definitions
- Safe constant sequences
- Cache keys
- Parsing request path segments
