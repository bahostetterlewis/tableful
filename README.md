tableful
========

Pretty tables for various python iterables

example:

```python
>>>d = {"First":["I'm data", "I'm other Data"], "Second":["I'm better data", "I'm the best data"]}
>>>tableful.TablefulOfDict(d)
+--------------+-----------------+
|    First     |     Second      |
+--------------+-----------------+
|   I'm data   | I'm better data |
|I'm other Data|I'm the best data|
+--------------+-----------------+

>>>a = (("First", "Second"), ("I'm data", "I'm better data"), ("I'm other Data", "I'm the best data"))
>>>tableful.Tableful(a)
+--------------+-----------------+
|    First     |     Second      |
+--------------+-----------------+
|   I'm data   | I'm better data |
|I'm other Data|I'm the best data|
+--------------+-----------------+
```

As you can see, they both have the same output.

Dicts treat keys as headers and their _iterable_ values as the column data.
To preserve order in a dict use an OrderedDict.
Non dict iterables use the first inner iterable as the headers, and each of the following as rows.


Easy interface - 2 functions

TablefulOfDict\() - Prints a dict in a tableful way.

Keyword args:
* file - an optional file like object that can be written

Tableful\() - Prints an iterable in a tableful way.

Keyword args:
* file - an optional file like object that can be written
* headers - an optional headers iterable that will be used in place of the main iterables embedded headers


Recipies
========

* Tableful CSV

```python
>>>from csv import DictReader
>>>from tableful import TablefulOfDict
>>>from collections import defaultdict
>>>table = defaultdict(list)
>>>with open('my_csv.csv', 'r') as f:
...   for dictionary in DictReader(f):
...       for key,value in dictionary.items():
...           table[key].append(value)
...
>>>with open('my_output_file.txt', 'w') as f:
...    TablefulOfDict(table, file=f)
...
>>>
```
