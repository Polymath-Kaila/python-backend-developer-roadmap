# Into 
This chapter is titled:  
## First class functions

## Python treats functions as first-class objects:
- assign them to variables
- store them in lists/dicts
- pass them as arguments
- return them from functions
- introspect them

## Higher-order functions:
- accept functions as arguments or return them
- used for custom sorting, callbacks, decorators

## Anonymous functions (lambda):
- short inline functions for simple expressions

## Closures:
- inner function remembers variables from outer scope
- foundation for decorators, middleware, caching, DI

## Callable objects:
- classes implementing __call__ act like functions

## Function introspection:
- __name__, __doc__, __annotations__, __defaults__, __closure__

## Backend applications:
- decorators (routing, auth, caching)
- middleware layers
- strategy pattern implementations
- dependency injection systems
- dynamic dispatch tables
- asynchronous callbacks

----------------------------------

A function can be used anywhere as a normal value.  
That is we can store it, pass it, return it, assign it, put it in a dict, modify and inspect it.  
Example:  
1. Assigning a function to a variable.  
```python
def call_me(name):
    return f"Hello {name}"
y = call_me # we are assigning the function to var y
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

