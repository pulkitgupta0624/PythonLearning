'''
Write a program to pronounce list of names using win32 api.
if yout are given a list l as follows:

```python
l = ["name1", "name2", "name3"]
```
Your program should pronounce each name in the list.
Shoutout to name1
, Shoutout to name2, Shoutout to name3...
'''

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

l = ["Pulkit", "Palak", "Rohit", "Saksham"]

for name in l:
    text = f" how are you :  {name}"
    print(text)
    speaker.Speak(text)

