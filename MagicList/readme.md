# MagicList
This Python class implements a simplified list by skipping boundary checks when possible.

## How to Install
Import the class:
```
from MagicList import MagicList
```

## How to Use

- The class supports prividing *cls_type* parameter in the constructor, which represents the list elements dataclass.
- Usage examples:
```
a = MagicList()  
a[0] = 5  
b = MagicList(cls_type=Person)  
b[0].age = 100  
print(a) 
### [5] 
print(b)
### [Person(age=5)]
```
