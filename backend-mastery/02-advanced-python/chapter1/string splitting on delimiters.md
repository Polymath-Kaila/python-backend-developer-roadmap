# Splitting Strings on Delimeters
When we recieve an input like: 
```python
"alice@example.com; bob@example.com,  charlie@example.com   dave@example.com"
```
Delimeters are:  
+ commas
+ semicolons
+ whitespaces
+ incosistent spacing
`.split()` cannot express this cleanly.  
So we use `regular expressions ` when the delimeter itself is a pattern.  

```python
import re
email = re.split(r'[;,\s]+',text)
```
Why this:  
+ `[]` character class (match any of them)
+ `+` one or more occurrences
+ regex engine scans once - `efficient`

Why we do not chain `.replace()`?
+ its error prone
+ multiple passes
+ harder to maintain 

## Backend rule of thumb
We use `regex` only when:  
+ delimters are variables
+ format is messy
+ input is untrusted