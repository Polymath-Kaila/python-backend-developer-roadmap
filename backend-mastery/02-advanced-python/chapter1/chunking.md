## Chunking
Buffering is automatic.  
Chunking is decision we make as devs.  

Imagine 500MB upload to 100 concurrent users.  
so if we do:  
```python
data = f.read()
```
We just:  
 + allocate 500MB * 100
 + crashed our server
Chunking prevents this behavior.  

Buffering is OS/Python controlled its used for perfomance optimization.  
Cunking is dev controlled used for memory & flow control.  

8KB is preffered for chunk size.  
If a file is large we must chunk it.  
