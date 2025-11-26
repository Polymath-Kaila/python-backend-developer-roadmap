# Protocols in python

A protocol is not a class or inheritance.  
Its to say:  
"If your object implements these specific methods...i python will treat it as this 'type.'"  



### 1. sequence protocols
   If our class implements:
   ```python
   __len__
   __getitem__
   ```
   Then our class is automatically:
   1. slicable
   2. indexable
   3. iterable
   4. works with ```len()```
   5. works with ```for item in obj:```
   6. works with ```in``` operator
   7. works with list utilities

   This is without inheriting from ```list or collections.abc.Sequence```

   -----------------------------------------------------------------------------------

### 2. Protocols are BEHAVIOUR contracts
They say:  
" If it walks like a duck and quacks like a duck...its a duck."  
Python doesn't care what class you inherit from,  
Python cares whether you implement the right behavior.

lets say we create:
```python
    class Numbers:
        def __len__(self):
            return 10
        def __getitem__(self,index):
            return index * 2
```
EVEN THOUGH this is not a list...  

Python treats it exactly like one:
```python
    nums = Number()
    len(nums)      # 10
    nums(3)        # 6 since we index of then multiply by 2
    nums(1:5)      # slicing works automatically
    for n in nums:
        print(n) # iteration works
```
We did not write any array class.  
we didn't inherit from list.  
We didn't inherit from sequence.  

But python says: 
"you implement the sequence protocol.  
So I'll behave accordingly."

------------------------------------------------------------------------------------
## How Django QuerySet Uses Protocols
 
### 1.QuerySet implements __len__
This allows:
```python
len(User.objects.all())
  ```
To return the number of rows.
Internally Django does something like: 
```python
  def __len__(self):
    return self.count()
    # count() triggers a SELECT COUNT(*) FROM...
```
So when we do:
```python 
    if qs:
```
Django actually uses the length:


```python
    __bool__ = __len__
```
    

--------------------------------------------------------------------------------------
### 2.QuerySet implements __getitem__
This is why we can do:
```python
qs:[0]
qs:[5:10]
qs:[:3]
```
Django overrides __getitem__ to behave like this:
+ if the argument is an integer, QS fetches one object
+ if the argument is a slice, it returns another QS.
```python
def __getitem__(self, k):
    if isinstance(k, slice):
        return self._clone()._filter_slice(k)
    else:
        return self._clone()._fetch_one(k)
```
Django is literally doing:
+ index access → limit 1 offset N.  
+ slicing → SQL LIMIT/OFFSET.  

This is protocol power.

QuerySets didn’t inherit from list or tuple —.  
they just implemented the sequence protocol properly.  

------------------------------------------------------------------------------------
### 3.QuerySet implements  __iter__
Django defines __iter__so we can loop over query results.
```python
for user in User.objects.all():
    print(user)


```
internally: 
```python
def __iter__(self):
    self._fetch_all()       # actually hits the database
    return iter(self._result_cache)
```
So a QS: 
1. is lazy
2. only fetches results when iterated
3. caches results internally

----------------------------------------------------------------------------------
### 4. QuerySet implements __repr__




    