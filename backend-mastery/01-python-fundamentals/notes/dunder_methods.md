# Data modelling
Refrence: Fluent python 3 edition

## What are dunder methods?
Dunder = "double underscore"  
They are hooks that let our custom classes integrate with python's built in features.  

## 1.__init__(self) - constructor 
Python calls it when we create an object.  

```python
class Person():
    def __init__(self,name:str,age:int): # constructs the person objects
        self.name = name
        self.age = age

        def callme(self):
            print(
                f"My name is {self.name}, i am {self.age} years old"
            )
person1 = Person("Kaila",19)
person1.callme()

```
--------------------------------------------------------------------------------------
## 2.__str__(self)
Used when printing or logging user friendly strings.  
In django models to outpu the admin panel

```python
# using the code in the constructor
def __str__(self):
 

    return f"{self.name}"
    return f"{self.age}"
  """
    return self.name { in django models}

  """
 ```

-------------------------------------------------------------------------------------
 ## 3.__len__(self)
 Useful when your object represents a collection can be a list,dictionary or set.  
 Query result, paginated data, cache entries, cart items, etc.  

 ```python 
class Table:
    def __init__(self,rows):
        self.rows = rows # a list of items
        self._data = rows

    def __len__(self):
        return len(self.rows) #returns the count of this rows

my_rows = [
    ["Evans",19],
    ["Amos",19],
    ["Godfrey"18,]
]

table = Table(my_rows)
print(len(table))  #outputs: 3

``` 
--------------------------------------------------------------------------------------

## 4.__repr__()
Used when debugging in shell or logging internal state.  
something unambiguous that helps developers understand the object.  
In backend development for logging requests, DB rows, configs


```python 
def __repr__(self):
    return f"Person(name={self.name},age={self.age})"
```

## 5.__getitem__(self,index) -indexing and slicing
its called when we run:  
   + obj[0]
   + obj[2:50]
using the list in the len method:  

```python
...
def __getitem__(self,index):
    return self._data[index] # ._data stores our rows internally

table = Table(rows)

print(table[0])    #outputs: ['kaila',19]
print(table[1][0]) # outputs: Amos

```
--------------------------------------------------------------------------------------

## 6.__iter__(self)
Similar to getitem().  
only it has inbuilt iterator for internal list as compared to getitem().  

```python
...
table = Table(rows):

for row in table:
    print(row)

    """ output
    ['kaila',19]
    ['Amos',19]
    ['Godfrey'18]
    """
```









