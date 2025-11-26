# Slicing
Slicing lets us extract parts of a sequence.  

It works on:  
+ strings
+ lists
+ tuples
+ ranges
+ objects

#### The syntax:
```english
sequence[start:stop:step]
```
+ `start` - where to begin (its included).
+ `stop`  - where to end(excluded) ie `stop-1`.
+ `step`  - how much to move each time.

### 1.Basic Slicing: `[start:stop]`
```python
numbers = [10,20,30,40,50]
"""
10 - index [0]
20 - index [1]
30 - index [2]
40 - index [3]
50 - index [4]
"""
numbers[1:3] # outputs [20,30]
```
### 2.Omitting `start`
```python
numbers = [10,20,30,40,50]

numbers[:3] # mean from index 0 upto index 2 since we did not specify any start point
# output : [10,20,30]
```
### 3.Omitting `stop`
```python 
numbers = [10,20,30,40,50]

numbers[3:] #starts from index 3 to the end
# output : [40,50]
```
### 4.Stride Slicing
```python
numbers = [10,20,30,40,50,60,70,80]

numbers[0:6:2] # start at 0 go to 6 but dont include 6, move 2 steps at a time
"""
so what happens
 start at 0
 Add 2 - 2
 Add 2 - 4
 Add 2 -6 but stop index is not included 
 """
 """
 so for this:
 index 0 = 10
 index 2 = 30
 index 4 = 50

 """
# so output : [10,30,50]

```

### 5.Copying entire sequence
```python
# we just use empty values in start,stop
numbers = [10,20,30,40]
numbers[:]
#output : [10,20,30,40]
```
### 6.Using Negative Indexes
Negative indexes count from the end:  
+ -1 - `last` element
+ -2 - `second last` element
+ -3 - `third last` element
```python
numbers = [10,20,30,40,50]
nums[-3:-1]
"""
index [-1] = 50(last but excluded)
index [-2] = 40(so we pick this)
index [-3] = 30(start)
index [-4] = 20
index [-5] = 10

"""
# output [30,40]
```
### 7.Reverse slicing
Here we omit start and stop and only include step but negative
```python
nums = [10,20,30,40,50,60,70,80]
# idx      0  1  2  3  4  5  6  7
numbers[::-1]
"""
start at last index(7 - 80)
move backwards one step at a time ( step = -1)
stop when you pass index0 since stop is omitted

"""
# output : [80,70,60,50,40,30,20,10]

name = "kaila"
name[::-1] # output : "aliak"

```
### 8.Assigning slices 
```python
numbers = [0,1,2,3,4,5,6,7,8,9]
#index      0 1 2 3 4 5 6 7 8 9

numbers[2:5] = [20,30]
"""
slice of start 2:stop5 is 2,3,4
so then we assign them to 20 and 30
python shrinks the list to fit them thus we have no 4

new list = [0,1,20,30,5,6,7,8,9]
"""
new list = [0,1,20,30,5,6,7,8,9]
del numbers[5:7]
""" 

we delete at index start 5 which is 6 and stop at 7 which is 7
so we remove 5 and 6
0 - 0
1 - 1
20 -2
30 -3
5 - 4
6 - 5(at this index) = 6
7 - 6(at this index) = 7
8 - 7
9 - 8

new list2 = [0, 1, 20, 30, 5, 8, 9]
       # idx   0  1   2   3  4  5  6

"""
new list2 = [0, 1, 20, 30, 5, 8, 9]

new list2[3::2] = [11,22] # means start at 3 till end skipping by 2;
""" 
start at index 3 which is 30;
so index 0 same as 3+2 = new index = index 5
value at index 5 = 8
if we do newindex + 2 we will get to index 7 which is past the end 
so we assign them to 11 and 22

so output : lastlist = [0,1,20,11,5,11,9]
"""
```
## Backend applications
### Parsing fixed-width log line
```python
IP    = slice(0, 15)
METHOD = slice(16, 20)
PATH  = slice(21, 50)

ip = line[IP]
method = line[METHOD].strip()
path = line[PATH].strip()

```
### Extracting bytes from a protocol message
```python
msg_type = packet[:2]
payload = packet[2:-4]
checksum = packet[-4:]

```

### Reversing data
```python
reversed_body = body[::-1]

```

### Sampling logs
```python
sampled = logs[::100]

```
### Modifying part of a mutable sequence
```python
buffer[10:20] = b"\x00" * 10
```

## Backend use of slicing
- parsing logs
- parsing fixed-width files
- binary protocol slicing
- trimming paths/urls
- reversing sequences
- sampling data