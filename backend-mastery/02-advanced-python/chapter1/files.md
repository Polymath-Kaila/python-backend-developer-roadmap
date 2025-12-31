## Files
A file is just a stream of bytes on disk.  
No text, No characters, No encoding.  
So python has two choices when opening a file:  
1. Give us the raw bytes
2. Decode the bytes into text 

That is why file modes exust:    
### 1. Binary mode("rb")
```python
file = open("data.txt", "rb")
data = file.read()
```
What we get:  
+ type: `bytes`
+ values:`0-255`
+ exactly whats on disk
No decoding happened.  
No encoding assumed.  

#### "rb" use cases
1. reading uploads (imgs,videos,pdfs,zips,encr dta)
2. handling unknown files
3. dealing with large files
4. working with binary formats
5. caring about correctness

--------------------------------------

### 2. Text mode ("r")
```python
f = open("data.txt", "r", encoding="utf-8")
text = f.read()
```
What python secretely does:
1. reads bytes from disk
2. applies `.decode("utf-8")`
3. returns a `str`

N/B we must specify which encoding to use ie utf-8.  
#### Explicit
```python
data = open("file.txt", "rb").read()
text = data.decode("utf-8")
```
#### Implicit
```python
text = open("file.txt", "r", encoding="utf-8").read()
```
#### "r" use cases
1. config files
2. JSON
3. CSV
4. logs
5. source code

-------------------------------

### Writing files
#### 1. Writing text
```python
open("out.txt", "w", encoding="utf-8").write("hello")
```
#### 2. Writing binary
```python
open("out.bin", "wb").write(b"\x00\xff")
```
---------------------------

#### Generally

+ Disk always stores → bytes
+ "rb"  → bytes → YOU decide
+ "r"   → bytes → decode → str
+ "w"   → str → encode → bytes
+ "wb"  → bytes → disk
