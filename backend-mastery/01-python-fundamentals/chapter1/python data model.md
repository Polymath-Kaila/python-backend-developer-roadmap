# The python Data Model

Its basically python's "contract" for how objects behave.  
Its like saying:  
"If your object implements these special methods, i python will give these abilities."  

Example mapping methods(most of dunder methods).  

In backend:  
+ Django QuerySets implements these to behave like collections.
+ custom data models,caches,ORMS,configs -all use data-model protocols instead of creating separate methods like:

```python
get_length()
iterate_items()
....
fetch_items(i)

```