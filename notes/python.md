# Python

## Agenda

* Intro to Python
* Importance of indentation
* Variables and types
* Control statements
* Functions
* Packages & Classes
* Common data structures (list, dist)
* Using built in packages - File I/O

## Performance Measure

* Comfortable doing Python programming
* Python exercise

## Installation Reminder

Please install [Python](https://www.python.org/) prior to start following.

> For Mac user, use `brew install python` to install Python 2 and
> `brew install python3` to install Python 3

### Why Python

Python, one of the most common languages choice for Artificial Intelligence. Why?

Many Machine Learning libraries are written in Python. This includes 
Machine Learning libraries like [Sci-kit](http://scikit-learn.org/stable/),
[NumPy](http://www.numpy.org/),
[Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html) or
[OpenCV](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)

Moreover, there are several additional reasons why Python is popular language:

* Easy to learn
* Easy to get it up and running
* Syntax is very close to pseudocode
* Interpreted languages (have interpreter built in)

All in all, Python allows developers/scientists to develop quickly as its nature
of the dynamic type language.

In following lecture, we will go over some of the basic tutorial of Python
language and practice them in the TDD manner.

---

Plus, you can always import antigravity!

![import antigravity from XKCD comic](https://imgs.xkcd.com/comics/python.png)

### Importance of Indentation

Before we dive into the Python specific syntax, we need to talk about one very
important aspect of Python -- indentation.

Python, unlike Java, does not have bracket or semi-colon. Python uses 
**indentation** to detect code block.

What do I mean by indentation? Consider the following:

```python
x = 1

if x > 0:
    print("x is positive")

    print("and more print statement just to prove the indentation block works")
```

When the print statement is not indented properly. It will not be executed
when x is greater than zero.

Therefore, it is highly recommended for you to display all the invisible characters
(space or tab) in your favorite text editor or IDE.

> Don't ask why your code doesn't work later because your code contains both
> hard tab and soft tab (1 hard tab and 4 spaces)

![5 Stages of Debugging](https://i.redd.it/7593yrkzhgiz.jpg)

> Please! Showing invisible characters will help you to avoid the 5 stages of debugging

### Variables and types

From this section and onward, I'll assume you are already familiar with Java and
build various knowledge based on what you've already known in Java to Python.

To define a variable, you don't need to specify types not like Java.
e.g. `int a = 3;` in Java vs `a =3` in Python

```python
# Numbers
x = 1 + 1
floatingNumber = 2 / 3
dividedInt = 2 // 3
modularInt = 2 % 3

# Boolean (keep it in mind that first character is capitalized)
t = True

# String
y = "Hello, world"
z = "Hello\nworld!"
multiline_string = """
this is multi-line string
if you need to print out multi-line
you may use three "
"""

concat_str = "Hello" + "," + "world!"

# You can treat word like list and get character(s) out this way
y[1]   # e
y[0:2] # He

# List
li = [1, 2, 3]
li[0] # 1
li[:] # return shallow copy of the list
li[1] = 4 # list is now [1, 4, 3]
li.append(5) # list is now [1, 4, 3, 5]
li[2:3] = [] # list is now [1, 4, 5]
len(li) # 3

# nested list
li = [[1, 2], [2, 3], [3, 4]]
```

### Control flow

Control flows includes if, for, while and function.

```python
x = 1

# if statement doesn't need to be surrounded by parentheses
if x > 0:
  print "x is positive"

# for 
li = [1, 2, 3]
# like enhance for loop in Java
for i in li:
  print i
# range
for i in range(10):
  print i # 0 ... 9
# range can also be specific range with lower-bound(inclusive) to upper-bound(exclusive)
for i in range(5, 10):
  print i # 5, 6, 7, 8, 9
# break and continue
for i in range(100):
  if i > 10:
    break
  elif i % 2 == 0:
    continue
  else:
    print i
```

```python
# def is the keyword to define a function
def f(x, y):
  return x + y

# to call a function, same way as Java
f(1, 2) # 3

# Python unlike Java can have default parameter value
def g(x, y=1):
  return x + y

g(1) # returns 2

def h(x, y, z):
  print x
  print y
  print z
  return x + y - z

# when calling function, it can provide keyword as argument
# order can be any way you want to put
h(y=2,x=6,z=10)

# lambda
def l(x):
  return lambda n: n + x

f = l(42)
f(8) # 50

# documentation for function
def messy(z):
  """
  this is a documentation example with multi-line string
  """
  return z + 42

print(messy.__doc__)
```

### Data structure

**List**

* list.append(x)
  * Add an item to the end of list
* list.extend(anotherList)
  * Extend list from another list
* list.insert(i, x)
  * Insert item x into position i e.g. insert to front of list `list.insert(0, item)`
* list.remove(x)
  * remove the **first** item of value x
* list.pop([i])
  * pop certain item from the list of index i. If no argument is given, pop the last item
* list.index(x)
  * return index of item x
* list.sort()
* list.reverse()

**List as stack**

```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack # [3, 4, 5, 6, 7]
stack.pop() # 7
stack # [3, 4, 5, 6]
stack.pop() # 6
stack.pop() # 5
stack # [3, 4]
```

**List as queue**

```python
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
# 'Eric'
queue.popleft()                 # The second to arrive now leaves
# 'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

**Functional programming with list** like filter, map and reduce

* filter  
```python
def f(x): return x % 3 == 0 or x % 5 == 0

filter(f, range(2, 25))
# [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]
```
* map  
```python
def cube(x): return x*x*x

map(cube, range(1, 11))
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```
* reduce  
```python
seq = range(8)
def add(x, y): return x+y

map(add, seq, seq)
# [0, 2, 4, 6, 8, 10, 12, 14]

# Python 2 and 3:
from functools import reduce

assert reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) == 1+2+3+4+5
```

Quite note on the methods above, they work in Python 2 only. To make the code
works with Python 2 and 3:

```python
# Python 2 only:
mynewlist = map(f, myoldlist)
assert mynewlist == [f(x) for x in myoldlist]
# Python 2 and 3: option 1
# Idiomatic Py3, but inefficient on Py2
mynewlist = list(map(f, myoldlist))
assert mynewlist == [f(x) for x in myoldlist]
# Python 2 and 3: option 2
from builtins import map

mynewlist = list(map(f, myoldlist))
assert mynewlist == [f(x) for x in myoldlist]
# Python 2 and 3: option 3
try:
    import itertools.imap as map
except ImportError:
    pass

mynewlist = list(map(f, myoldlist))    # inefficient on Py2
assert mynewlist == [f(x) for x in myoldlist]
# Python 2 and 3: option 4
from future.utils import lmap

mynewlist = lmap(f, myoldlist)
assert mynewlist == [f(x) for x in myoldlist]
# Python 2 and 3: option 5
from past.builtins import map

mynewlist = map(f, myoldlist)
assert mynewlist == [f(x) for x in myoldlist]
```

**Tuples**

We saw that lists and strings have many common properties, such as indexing and slicing operations. They are two examples of sequence data types (see Sequence Types — str, unicode, list, tuple, bytearray, buffer, xrange). Since Python is an evolving language, other sequence data types may be added. There is also another standard sequence data type: the tuple.

A tuple consists of a number of values separated by commas, for instance:

```python
t = 12345, 54321, 'hello!'
t[0]
# 12345
t
# (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
t[0] = 88888
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
# ([1, 2, 3], [3, 2, 1])
```

**Set**

Similar to list but with keyword `set`

```python
li = [1, 2, 3, 1]
se = set(li) # set([1, 2, 3])
1 in se # True
4 in se # False

# operation on sets
li2 = set([2, 3, 4])
# in se but not in li2
se - li2 # 1

# union
se | li2 # 1234

# interception
se & li2

# in a or b but not both
se ^ li2
```

**Dictionary**

Dictionary is like map in Java.

```python
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

tel.keys()

'guido' in tel

# to loop through
for i, v in enumerate(['tic', 'tac', 'toe']):
  print i, v
```

### Modules

Each python file is essentially a module.

For instance,

```python
# my_math.py

def add(x, y):
  return x + y
```

```python
import my_math

my_math.add(1, 2)
```

**Python main method**

If you have a if statement like below, that block of code will not be executed when you import to other module.

```python
if __name__ == "__main__":
  import sys
  print sys.argv[1]
```

**Packages**

When your code base grows larger, you will need to think about how to organize your code. 

Packages allows you to create folder containing modules. However, in order to 
create a package, you will need to create a file called `__init__.py` for Python
runtime to know this folder is a package like below:

```
main.py
acquisition/
  __init__.py
  collector.py
  source.py
storage/
  __init__.py
  mongo.py
```

Then in your `main.py` you can start import like below:

```python
# main.py
import acquisition.collector
import aqcuisition.source

while source.hasNext():
  collector.save(collector.munge(source.next()))
```

### File read/write

```python
# Python 2 only
f = open('myfile.txt')
data = f.read()              # as a byte string
text = data.decode('utf-8')

# Python 2 and 3: alternative 1
from io import open
f = open('myfile.txt', 'rb')
data = f.read()              # as bytes
text = data.decode('utf-8')  # unicode, not bytes

# Python 2 and 3: alternative 2
from io import open
f = open('myfile.txt', encoding='utf-8')
text = f.read()    # unicode, not bytes
```

### json

JSON is built-in with Python!

```python
# write json string
json.dumps([1, 'simple', 'list'])

# dump json to a file
json.dumps([1, 'simple', 'list'], f)

# read json string from file
json.load(f)
```

### Exceptions

```python
while True:
  try:
    x = int(raw_input("Please enter a number: "))
    break
  except ValueError:
    print "Oops!  That was no valid number.  Try again..."
```

### Classes

```python
class MyClass: # can defined inheritance MyClass(ParentClass, ParentClass2)
    """A simple example class"""
    # Static variable
    static_int = 12345

    def __init__(self):
      self.instance_int = 54321
      print 'no arg constructor is called'

    def f(self): # first argument is always self
        return 'hello world'
```

### Package manager -- pip

https://pip.pypa.io/en/stable/installing/

### Recommended reading

http://python-future.org/compatible_idioms.html
