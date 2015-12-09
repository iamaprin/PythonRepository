### files
#### methods:
`open(filename, mode)`:
`mode`: `r` = read, `w` = write, `a` = append
`rb/wb` = binary data(end-of-line translations and 3.X Unicode encodings are turned off)
`+` = read & write
```python
>>> file = open('note/files.md', 'r')
>>> print(file.read())
### files
#### methods:
`open(filename, mode)`:
`mode`: `r` = read, `w` = write, `a` = append
`rb/wb` = binary data(end-of-line translations and 3.X Unicode encodings are turned off)
`+` = read & write

>>> file = open('note/files.md', 'rb')
>>> print(file.read())
b'### files\r\n#### methods:\r\n`open(filename, mode)`:\r\n`mode`: `r` = read, `w` = write, `a` = append\r\n`rb/wb` = binary data(end-of-line translations and 3.X Unicode encodings are turned off)\r\n`+` = read & write
```
<br>

