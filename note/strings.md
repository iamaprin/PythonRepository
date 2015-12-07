`numbers, strings, tuples --- immutable`
`lists, dictionaries, sets ,bytearray--- changeable`

----------

**import**
`re` -- 正则表达式



----------
lists -- []
dictionaries -- {key : value}



----------
**String Conversion tools**
```python
>>> int('42'), str(42)		#convert from/to string
(42, '42')
>>> int('1101', 2)
13
```

----------
**string format**
```python
>>> 'That is %d %s bird!'%(1, 'dead')
'That is 1 dead bird!'
>>> 'That is {0} {1} bird!'.format(1, 'dead')
'That is 1 dead bird!'
```
**string methods:**
```python
>>> s = 'abbcccddddcccbba'
>>> s.replace('ccc', 'EEE')
'abbEEEddddEEEbba'
>>> s.replace('ccc', 'EEE', 1)
'abbEEEddddcccbba'

```
```python
>>> s = 'abbcccddddcccbba'
>>> list(s)
['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'c', 'c', 'c', 'b', 'b', 'a']
```
```python
>>> l = ['a', 'b', 'c', 'd']
>>> s.join(l)
'aabbcccddddcccbbababbcccddddcccbbacabbcccddddcccbbad'
>>> 'a'.join(['a', 'bb', 'c'])
'aabbac'
```
```python
>>> s = 'a, b, c, d'
>>> s.split(',')
['a', ' b', ' c', ' d']
```

----------
**functions:**
`eval`: it runs a string containing Python expression code and so can convert a string to any kind of object.
`ord` && `chr`: 's' <=> 115, convert a single character to its codepoint.
`bin`:  convert integer to binary,**bin(13) => '0b1101'**