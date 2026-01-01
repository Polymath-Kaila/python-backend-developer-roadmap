# Encode/Decode
## Encoding
Encoding is converting characters (`code points`) into bytes using a rule.  
Example:  
```python
string = "A"
```
Internally:  
+ Character: "A"
+ Code point: `U+0041`(65)
Now:  
```python
byte = string.encode("utf-8")
```
What happens:  
```apache
U+0041  →  UTF-8 rule  →  0x41
```
So:  
```python
byte == b"\x41"
```
Important:  
+ UTF-8 is not `text`
+ It is a mapping algorithm
+ same characters - same bytes (deterministic)

------------------------------------------

# Decoding
Decoding is converting bytes into characters using a rule.  
Example:  
```python
byte = b"\x41"
string = byte.decode("utf-8")
```
What happens:  
```apache
0x41  →  UTF-8 rule  →  U+0041  →  "A"
```
So:  
```python
string =="A"
```
-----------------------------------------
### N/B
+ Encoding and decoding are inverse operations
+ If they dont match - corruption
+ Example we cannot encode using utf-r then decode back using latin-1
+ One character doesnt mean one byte, ie an emaoji has 4bytes

----------------------------------------

### Common mistakes
#### 1. Decoding binary data (silent disaster)

```python
data = open("image.png","rb").read()
text = data.decode("utf-8") # silent corruption
```
This is bad:  
  + binary data hsa no text meaning
  + utf-8 decoder expects structured byte patterns
  + random bytes violate those patters
Rule: `if you didn't create it as text, dont decode it`.  
Rule: once encoded, we are in byte-world.  
Rule: business logic belongs in str-world.  
+ Encode only when crossing out of Python
+ Decode only when entering into Python logic
+ Decode as late as possible
+ Encode as early as necessary
+ Never guess encoding
+ Never decode binary files
