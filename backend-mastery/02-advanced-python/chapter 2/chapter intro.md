# Into 
This chapter is titled:  
### First class functions
A function can be used anywhere as a normal value.  
That is we can store it, pass it, return it, assign it, put it in a dict, modify and inspect it.  
Example:  
1. Assigning a function to a variable.  
```python
def call_me(name):
    return f"Hello {name}"
y = call_me() # we are assigning the function to var y
print(y("kaila"))

```
2. Putting a function in a list.  
```python
def plus(x,y) return x+y
def minus(x,y) return x-y

operations = {
    "add":plus
    "minus":minus
}

print(operations["add"](3,2)) # =5
print(operations["minus"](3,2)) # = 1

````

