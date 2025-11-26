# Python Sets 

A **set** in Python is an **unordered**, **unique**, and **hash-based** collection of elements.  
Sets offer **fast membership tests** (O(1)), automatic **duplicate removal**, and useful **mathematical operations**.

---

## 1. What Is a Set?

A set is similar to real mathematical sets: it contains **unique items**, has **no duplicates**, and is optimized for **fast lookup**.

```python
s = {1, 2, 3}
```
## 2.Key properties
+ Unordered → no indexing
+ Unique elements → duplicates removed automatically
+ Mutable → you can add/remove
+ Fast membership tests due to hashing
+ Only hashable (immutable) objects allowed as elements

## 3.Creating Sets
Literal syntax 
```python
s = {1, 2, 3}
```
From iterable
```python
s = set{1,2,3,4}
# {1,2,3,4}
```
Empty set
```python 
s = set() # correct
# {} would be an empty
```
## 4. Adding and Removing Elements
1. Add
```python
s.add(10)
```
2. Remove (errors if missing)
```python
s.remove(10)
```
3. self remove(no error)
```python
s.discard(10)
```
4. Pop (removes and returns an arbitrary element)
```python
item = s.pop()
```
## 5. Set operations
#### Union - combines sets
```python
a | b
```
#### Intersection - common items
```python
a & b
```
#### Difference - items in a not b
```python
a - b
```
#### Symmetric Difference - items not shared
```python
a ^ b
```
Example:  

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # {1, 2, 3, 4, 5}
print(a & b)  # {3}
print(a - b)  # {1, 2}
print(a ^ b)  # {1, 2, 4, 5}

```
## Iterating Over a Set
```python
for item in s:
    print(item)
```
## Set Comprehensions
```python
unique_squares = {x * x for x in [1, 2, 2, 3]}
# {1, 4, 9}
```
```python
evens = {x for x in range(10) if x % 2 == 0}
```
```python
pairs = {(x, y) for x in range(3) for y in range(3) if x != y}
```
### Backend Uses
1. permission sets
2. visited URLs
3. deduplicating items
4. checking allowed methods
5. blacklists / whitelists
6. unique tags
7. fast “exists?” checks

### Choosing the Right Data Structure

| Use Case                | Recommended Structure |
| ----------------------- | --------------------- |
| Need key → value        | `dict`                |
| Need fast “exists?”     | `set`                 |
| Need duplicates + order | `list`                |
| Need to group values    | `dict` + `list`       |
| Need to count items     | `Counter`             |
| Need LRU behavior       | `OrderedDict`         |
| Need unique sequence    | `set` or `frozenset`  |
