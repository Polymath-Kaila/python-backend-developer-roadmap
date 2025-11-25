# Arrays,Memoryviews & Deques
Python gives us 3 high-perfomance sequence types that are faster and more efficient than normal lists when we need to handle `binary data`,`large datasets` or `fast queues`.  

These 3 tools solve different problems:
+ array.array - fast storage of numbers
+ memoryview - slices bytes WITHOUT copying
+ deque - fast queue (append/pop)

A byte is 8bits, capable of storing 256 possible values,used as the basic unit of data in computers.  
letter "A" - is ASCII code 65.  
In binary :  
```code
01000001
```
So the computer stores "A"as that single byte.  

# 1.array.array
Take list:  
```python
numbers = [1,2,3]
```
BUT lists stores `Python objects`, not raw machine numbers: this is very slow and heavy if you store `thousands or millions.`  
array('i',[....]) stores numbers in C-level raw form.

##### Inshort array.array is a list for numbers
Example:  
```python
from array import array

nums = array("i", [1, 2, 3, 4])   # "i" means integer
print(nums[0])  # 1
```
### Type codes used in array.array
1. `b` - signed char; Range:(-128 to +127); 1 byte; Example:  
```python
array('b', [10, -5, 127])
```
2. `B` - unsigned char; Range:(0 to 255); 1 byte; Example:
```python
array('B', [0, 255])
```
3. `h` - signed short
4. `H` - unsigned short
5. `i` - signed int
6. `I` - unsigned int `f`,`d`

### Backend use:
1. binary formats(network packets)
2. reading/writing numeric data to files fast
3. handling sensor data,stats,logs with huge volume

#### Real backend example
```python
payload = b"\x00\x01\x00\x02"    # bytes from a sensor
data = array("H", payload)       # "H" = unsigned short (2 bytes)
print(list(data))                # [1, 2]
```

# 2.Memoryview
Slice bytes WITHOUT copying.  
Take this scenario:  
when we slice bytes:  
```python
chunk = data[0:4]
```
Python COPIES the data - this is slow for large files / network packets.  
memoryview solves this:  
```python 
chunk = [2394,6679,8899]
mv = memoryview(data)
chunck = mv[0:4] # NO COPY
```
Inshort memoryview is a slicing technique without copying.  

### Backend use
1. parsing packets from sockets
2. handling big binary files
3. working with buffers(video,audio)
4. FAST slicing for protocols

#### Real use case: parse protocol packet
say we receive this packet:  
```python
packet = b"\xAA\x01\x02\x03\x10\x20\x30\x40"
mv = memoryview(packet)

header = mv[0]     # 0xAA
opcode = mv[1]     # 0x01
pyload = mv[2:6]   # \x02\x03\x10\x20
checksum = mv[-2:] # \x30\x40

"""
No copying.
super fast
perfect for network servers

"""
```

# Deque
list are slow in some operations like:
```python
lst = [0,3,4,5,6,7]
lst.pop(29)
lst.insert(0,y)
```
These are the O(n) operations.  
`deque` makes them O(1).  
Think of deque as:  
"The correct tool for queues,sliding windows,logs".  

#### Basic example:
```python
from collections import deque

q = deque()
q.append("req1")
q.append("req2")
print(q.popleft())  # req1
```
### Backend use
1. request queues
2. worker queues
3. sliding windows for rate limiting
4. keeping the last N logs
5. BFS/graph search
6. bounded buffers(maxlen)

#### Real use : sliding window rate limitter
```python
from collections import deque
from time import time

requests = deque(maxlen=100) # keep the last 100 timestamps

def allow_request():
    now = time()
    request.append(now)
    return len(requests) < 100
# this checks if <=100 requests happend recently.
```
### When to use array.array

+ You store NUMBERS
+ You want SPEED + low memory
+ You parse binary numeric data

### When to use memoryview

+ You slice bytes a lot
+ You parse network packets
+ You want ZERO-COPY slicing

### When to use deque

+ You need a QUEUE
+ You need fast append/pop left
+ You need sliding windows
+ You handle event streams or logs




