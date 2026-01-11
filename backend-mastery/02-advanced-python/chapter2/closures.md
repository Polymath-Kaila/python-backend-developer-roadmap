# Closures
A closure is a function that remembers a variable from outside itself, even after that outer code has finished running.  

```python
def outer():
    x = 10
    def inner():
        return x
    return inner
```
### A funtion is a closure if:  
1. its inside another function
2. It uses a variable from the outer function
3. the outer function returns it

### Closures exist to let us:
+ keep state without a class
+ customize functions
+ build decorators
+ write clear reusablelogic

### Use cases
 1. Rate limiters
 2. Caching(Memoization)
 3. Decorators
 4. Callbacks
 5. Encapsulation
 