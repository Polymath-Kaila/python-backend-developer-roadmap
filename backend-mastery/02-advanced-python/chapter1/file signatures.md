# File signatures
File extensions mean nothing.  
`.png`,`.pdf`,`.mp4` are labels, not guarantees.  
Backend systems never trust labels.  
Why?  
+ users rename files
+ attackers fake extensions
+ operating systems lie
+ browsers guess
So we need a `byte-level truth.`.  

--------------------------------

So a `file signature` (magic numbers) is a fixed sequence of bytes at the start of a file that uniquely identifies the file format.  

This is just `bytes`.  

| File | Signature (hex)           | Bytes                    |
| ---- | ------------------------- | ------------------------ |
| PNG  | `89 50 4E 47 0D 0A 1A 0A` | `b"\x89PNG\r\n\x1a\n"`   |
| PDF  | `25 50 44 46`             | `b"%PDF"`                |
| ZIP  | `50 4B 03 04`             | `b"PK\x03\x04"`          |
| JPG  | `FF D8 FF`                | `b"\xff\xd8\xff"`        |
| MP4  | `66 74 79 70`             | `b"ftyp"` (offset-based) |

so these bytes exist before any content.  
Signatures work beacuse:  
+ file formats must be self-identifying
+ parsers need to know how to read the rest
+ operating systems rely on them
  
So say for a PNG decoder it expects those first 8bytes.  
No signature means no PNG.  

------------------------------------

## N/B for backend
`Validate file types using bytes, not filenames, not MIME headers`.  

### Streaming safe detection
We never do:  
```python
data = f.read()
```
Instead:  
```python
header = f.read(16)
```
Why 16:  
+ enough fro most signatures
+ minimal memory
+ safe for large files
  
#### Correct implementation of signatures
```python
SIGNATURES = {
    "png": b"\x89PNG\r\n\x1a\n",
    "pdf": b"%PDF",
    "zip": b"PK\x03\x04",
    "jpg": b"\xff\xd8\xff",
}

def detect_file_type(stream):
    header = stream.read(16)

    for filetype, sig in SIGNATURES.items():
        if header.startswith(sig):
            return filetype

    return "unknown"
```
This:  
+ reads minimal bytes
+ works with streaming
+ avoids decoding
+ avoids memory blowups

Decoding is wrong here because we are not dealing with text.  

--------------------------------

### Offset-based signatures
Some formats like (MP4) dont start immediately.  
I.e:  
+ MP4 signature `ftyp`
+ Appears at byte offset 4
  
so detection becomes:  
```python
if header[4:8] == b"ftyp":
    return "mp4"
```
--------------------------------

### Security
File signatures checks prevent:  
+ disguised executables
+ script uploads
+ polyglot files
+ content-type confusion attacks

#### polyglot file
This is a file that is valid as more than one file type at the same time.  
The same bytes can be correctly interpreted in two ways or more depending on which program reads.  

Example:  
1. `Image + Script`:  
+ valid PNG
+ also valit html/js
+ browser renders image
+ server excutes script
  
2. `ZIP + APK`
+ Android app package is just a ZIP.  
+ Same file works as both.  
  
3. `PDF + JavaScript`
+ PDF viewer shows document
+ JS engine runs code

#### steganography
Means hiding information inside something ordinary so no one even knows its there.  
This is secrecy of existence.  
Ie. `LSB` `Least Significant Bit` steganography.  
Where say a photo of a cat is sent inside it with a secret message,zip,malware,another image.  

| Polyglot                              | Steganography              |
| ------------------------------------- | -------------------------- |
| File is **valid as multiple formats** | File is **one format**     |
| Data is *interpretable*               | Data is *hidden*           |
| Obvious if opened differently         | Invisible unless extracted |
| Parser-based                          | Data-based                 |

They can be combined:  
+ valid PNG image
+ valid zip archive
+ inside image pixels is hidded encrypted payload.  