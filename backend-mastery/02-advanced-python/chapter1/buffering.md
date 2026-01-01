## Buffering
This is temporarily storing data in memory so we don't do I/O one at at time/repeatedly.  
Since if we do so:    
 I/O is `slow`.  
 Memory is `fast`.  

 So if we could read a file like this:  
 ```python
 while True:
    byte = f.read(1)
    if not byte:
        break
```
So this will coause:  
+ thousands of system calls
+ terrible perfomance
+ cpu waste


Inshort making many I/O calls is a perfomance bottleneck since its slow, so we use buffering to bundle data or bytes then read or write once rather few times.  
So the preferred buffer size of bytes is 8KB = 8192.  
So now:
+ the OS reads 8kb at once.  
+ stores it in memory
+ python processes it efficiently
  
```python
while True:
    byte = f.raed(8192)
    if not byte:
        break
```

