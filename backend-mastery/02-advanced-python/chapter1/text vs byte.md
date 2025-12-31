# txt vs byte
Everything inside python is `text`(str).  
Everything outside python is `bytes`(binary).  

Bytes can exist without text but text cant. 

#### What bytes really are
In Python:  
```python
b = b"hello"
```
This is not text, internally it is:  
```accesslog
[104, 101, 108, 108, 111]
```
Bytes are:  
+ immutable
+ each element is a number (0-255)
+ slicing returns bytes
+ python does not assume meaning
  
-------------------------------

#### What str really are
In python:  
```python
s = "hello"
```
That is:  
+ a sequence of characters
+ each character maps to a `Unicode code point`
+ not tied to bytes
  
------------------------------
  