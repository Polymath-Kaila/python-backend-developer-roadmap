# Unicode Normalization
The same "human-visible" text can be represented by different unicode code point sequences.  

The character `é` can be in two valid ways:  
1. single code point
```apache
   U+00E9  →  é
```
2. two code points
```apache
 U+0065 (e) + U+0301 (combining acute accent)
```
This will break backends.  
So unicode normalization converts text into canonical, consistent code point forms.  
Two main ways:  
+ `NFC` - Composed form(preferd)
+ `NFD` - Decomposed form
+ `NFKC` - Compatibility composed(recommended)
+ `NFKD` - Compatibility decomposed

Backend rule:  
Normalize text at system boundaries.  
+ user input
+ identities
+ comparisons
+ storage

```python
import unicodedata
username = unicodedata.normalize("NFKC",username)
```
### Casefolding
`.lower()`  is not enough to some extent its limited to some characters so then python gives this:  
`.casefold()` method.
works well with normalization:  

```python
def sanitize(text):
    import unicodedata
    return unicodedata.normalize("NKFC",text).casefold()
```