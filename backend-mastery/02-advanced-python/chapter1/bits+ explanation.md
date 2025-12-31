# CS founds
Facts:  
+ Everything in a computer is `bits`
+ Bits are grouped into `bytes`
+ We represent bytes using:  
    + binary(base-2)
    + octal(base-8)
    + hexadecimal(base-16)
These are just representations, not different data.  
Example:  
```apache
Binary:       01000001
Decimal:      65
Hexadecimal:  0x41
```
#### Characters before Unicode
Originally computers used ASCII (American Standard for Information Interchange):  
+ It was 8 bits thats 2^8 = 256 
+ 1byte was repr by 7bits so max bytes = 2^7 = 127.  
Take a look of ASCII table:  

|Numbers  | character |
|---------|-----------|
|65       |  A        |
|66       |  B        |
|67       |  C        |
|97       |  a        |

So when we say:  
"AFC converts to binary/hex".  
Whats happening is:  
```dns
"A" → 65 → 0x41 → 01000001
"F" → 70 → 0x46 → 01000110
"C" → 67 → 0x43 → 01000011
```
its character - number - bits.  
ASCII broke because it only supports 128 characters.  
That is: 
+ no Arabic
+ no chinese
+ no emojis
+ no accents
+ no math symbols
So the world needed needed one universal character set.  
This is where `Unicode` comes in.

-------------------------------

#### Unicode
Unicode is not encoding.  
Unicode is:  
A universal list that assigns a `unique number` to every charcter.  
These numbers are callled code `points`.
Example:  

| Character | Code point |
| --------- | ---------- |
| A         | U+0041     |
| é         | U+00E9     |
| 火        | U+706B     |
| 🔥        | U+1F525    |

Key facts:  
A unicode code point is just a number.  
So:  
  + Unicode defines `meaning`
  + It does NOT define `storage`
  
-------------------------------------

#### From code points to memory(UTF-8)
Computers stores `bytes` not `code points`.  
So we need a rule to convert:  
```excel
Unicode code points - bytes
```
That rule is called an `encoding`.  
Examples:  
+ UTF-8
+ UTF-16
+ UTF-32

#### UTF-8
This is a variable-length encoding.  
Its says:  
  + ASCII characters equal 1 byte
  + other characters equal 2-4 bytes

Example:  
Character `A`.  
  + code point: U+0041(65)
  + UTF-8 bytes: `0x41`
  + Binary: 01000001  
Character: `🔥`
  + code point: U+1F525
  + utf-8 bytes: `0xF0 0x9F 0x94 0xA5`

So when we coonvert characters to hex/binary we are usually:  
  + either using ASCII
  + or using UTF-8 bytes

------------------------------

### N/B IN PY & MEMORY
Rule of thumb.  
Both `str` abd `bytes` are stored as bytes in memory.  
The difference is how python interprets those bytes.  

#### 1. How bytes are stored in memory
```python
byte = b"A"
```
in memory:  
```code
41
```
Thats it.  
  + One byte
  + Value = 65
  + No interpretation

#### 1. How str are stored in memory
```python
string = "A"
```
Internally:  
  + Python stores `Unicode code points`
  + Not UTF-8 bytes (usually)
  + storage format is implementation-dependent

Cpython uses different internal representations:  
  + 1 byte per character (Latin-1)
  + 2 bytes
  + or 4 bytes
But the key idea:  
`str` stores `characters`, not encoded `bytes`

Encoding happens only when we cross the boundary:  
+ writing to file
+ sending over networks
+ calling `.encode()`

#### Generally
+ Bits/bytes are physical reality
+ Hex / binary / octal are just representations
+ Characters are numbers (code points)
+ Unicode defines meaning, not storage
+ UTF-8 defines how code points become bytes
+ `bytes` = encoded representation
+ `str` = characters / code points
+ Both live in memory as bytes, but at different abstraction layers