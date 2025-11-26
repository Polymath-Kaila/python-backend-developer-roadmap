# Hash maps in python
A hash map or as called in python strictly as a `hash table` is a key-value data structure.  
Take objects in javascript, they store key-value objects' elements using curly brackets.  
That is the exact way hash tables in python dictionaries behave. 
Its built from:  
+ A big array object
+ A hash function which turns keys into numbers
+ A way to resolve `collisions` when two keys map same index

Now take this dictionary same as js object:  
```javascript
person = {
    "name":"kaila",
    "age":19,
    "major":"Computer science",
    "skill":"backend engineering"
    /*nb this code is exactly same in python dictionary so we use it */
}
```
Here `keys` are: name,age,major & skill.  
`Values` are: kaila,19,computer science & backend engineering.  
#### step1
python use `keys`:  
the value is a dictionary with keys of name, age etc.  
```python
value = dict["name","age","major","skill"]
```
#### step2
python runs the `keys` through the `hash function`:
```python
has("name",*"skill")
"name"= 912223344
"age" = 912223345
"major" = 912223346
"skill" = 912223347
# those are giant integers
```
#### step3
python maps it into the table:
```python
index0 = hash("name") % table_size
index1= hash("age") % table_size
index2= hash("major") % table_size
index3= hash("skill") % table_size
""" 
 Example results of backets numbers:
 index0 = 69
 index1 = 70
 index2 = 71
 index3 = 72

"""
```
#### step4
python jumps to `buckets`:
```python
table[69] - "kaila"
table[70] - 19
table[71] - "Computer Science"
table[72] - "backend engineering"
```
As seen we have no:  
+ scanning
+ searching
+ loops
Its just `direct access`
#### Important notes
1. the key itself is not stored as the number 69,70,..  
what happens:  
+ the hash number is used to choose the buckect
+ the actual key + value pairs are stored in that bucket chosen by the number
so bucket 70 holds:
```javascript
("name","kaila")
```
2. why do we store the key yet we already hased it uniquely?  
Because in rare cases, two different keys might hash to the same bucket.  
so python uses the actual key to verify the macth.  

3. In summary:
+ The hash function turns the key into a number.
+ That number picks the index in a big array.
+ That index contains the key-value pair.
+ Python jumps directly to it in constant time.
Finally in our case:  
We can run:  
 ```python
person = ["name"] # instant ouput "kaila"

```
### O(1) means `constant time`
Time does NOT grow with more data
### Rules
1. Key must be immutable, hashable: ie str,int,float,tuple Not hashable(listsdict ,set,).