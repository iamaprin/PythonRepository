### dictonaries - mutable mapping
```python
d = {'name': 'Bob', 'age', 40}
```

#### methods
`dict.keys() & dict.values() & dict.items()`：
```python
>>> l = {'name': 'Bob', 'age': 40}
>>> print(l.keys())
dict_keys(['age', 'name'])
>>> list(l.keys())
['age', 'name']
>>> list(l.items())
[('age', 40), ('name', 'Bob')]
```
`dict.pop()`：
```python
>>> l
{'age': 40, 'name': 'Bob'}
>>> l.pop('age')
40
>>> l
{'name': 'Bob'}
```
#### make dict from tuple
```python
>>> ll = dict([('name', 'Bob'), ('age', 40)])
>>> ll
{'age': 40, 'name': 'Bob'}

>>> lll = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
>>> lll
{'b': 2, 'a': 1, 'c': 3}
```
