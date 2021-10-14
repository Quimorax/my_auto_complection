## _**Auto-conplete => Auto-complete**_

### Description

---
This project is small auto-complete with command line support. The user enters a word, 
either on the command line with the parameter or enters directly, 
and the program identifies the word with which the greatest similarity is found.

### Technical information

---

Dictionary is small, because size of dictionary with most common words is only 3000 words. 
Dictionary saved and extracted using pickle. Initially, after extraction dictionary 
has "0" as default value, looks something like this:

```python
{
    'a': 0,
    'abandon': 0,
    'ability': 0,
    'able': 0,
    'abortion': 0,
    'about': 0,
    'above': 0,
    'abroad': 0, 
    'absence': 0, 
    'absolute': 0,
    # and so on...
    'young': 0, 
    'your': 0,
    'yours': 0, 
    'yourself': 0, 
    'youth': 0, 
    'zone': 0
}
```
But minus of avoiding all dictionary for greater accuracy is a little drop in productivity. 
### Need libraries
This program needs only one and then, only for tests, is `pytest`.
