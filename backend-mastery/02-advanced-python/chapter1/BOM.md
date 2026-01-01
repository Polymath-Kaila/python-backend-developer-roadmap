# Byte order marks
A BOM is a special sequence of bytes at the start of a text file used to signal encoding(mainly utf-16/32 at times utf-8).  

Example: 
+ UTF-8 BOM → `EF BB BF`
+ UTF-16 (Little-endian) → `FF FE`
+ UTF-16 (Big-endian) → `FE FF`
These bytes don’t represent visible text — they’re a signal.
Stick to utf-8 without BOM.  
Detectig and removing it in py:  
```python
text = data.decode("utf-8-sig")
```