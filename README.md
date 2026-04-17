# Python-programming-language Learning notes

# 📘 Week 01 – Basics & Operators

## 🔹 Input and Type Conversion

```python
benefits = float(input("Enter the amount of the study benefits: "))
```

⚠️ `input()` always returns a **string**, so conversion is required.

## 🔹 String Concatenation

```python
print("after a raise, would be " + str(benefits_after_raise) + " euros")
```

👉 Better:

```python
print(f"After a raise, it would be {benefits_after_raise} euros")
```

## 🔹 Checking Numeric Strings

```python
if not feeling.isdigit():
```

👉 Checks if a string contains only digits (no negatives or decimals!)

## 🔹 Important Operators

### Floor Division

```python
change // 10
```

👉 Returns the largest integer ≤ result (floor division)

### Power Operator

```python
2 ** 3  # 8
```

# 📘 Week 02 – Conditionals & Loops

## 🔹 Boolean Expressions

```python
read_words = word != "quit"
```

👉 Equivalent to:

```python
if word == "quit":
    read_words = False
```

## 🔹 for-loop with range

```python
for ind in range(0, height - 1):
```

## 🔹 `break` vs `continue`

```c
while True:
    x = input("Enter number: ")

    if x == "":
        break

    if int(x) < 0:
        continue

    print(x)
```

- `break` → exits the **while** loop completely.
- `continue` → skips the rest of the current **while** loop iteration and starts the next one.

## 🔹 range() Examples

**range(start, end, step)**

```python
print(*range(1, 10, 2))      # 1 3 5 7 9
print(*range(100, 200, 10))  # 100 110 ... 190
print(*range(10, 0, -1))     # 10 9 ... 1
```

👉 `*` = **unpacking operator**

- It **unpacks** the elements of an iterable (like `range`, list, tuple)
- So each element is passed as a **separate argument** to `print()`

### Key rules

- Interval: **[start, end)**
  👉 end is **NOT included**
- Default values: **start = 0, step = 1**

## 🔹 print formatting

### Same line printing

```python
print("Hello", end="")
print("World")
```

### Separator

👉 By default, `print()` uses a **space (" ") as separator**

#### 🔹 Custom separator

```python
print("apple", "banana", "cherry", sep=", ") # apple, banana, cherry
print("2026", "04", "16", sep="-")           # 2026-04-16
```

## 🔹 f-string formatting

```python
print(f"result: {3.14159265358979 * 9 ** 2:.3f}")
```

👉 `.3f` = 3 decimal places

## 🔹 Width and alignment

```python
value = 123
# default is right align
# > right align, < left align, ^ center align, width = 10
print(f"{value:10d}")  # '       123'
print(f"{value:>10}")  # '       123'  (right aligned)
print(f"{value:<10}")  # '123       '  (left aligned)
print(f"{value:^10}")  # '   123    '  (center aligned)

print(f"{value:010d}") # '0000000123'  (fill with 0)
```

# 📘 Week 03 – Functions

## 🔹 Swapping / Tuple Assignment

```python
a, b = b, a + b
a, b = b, a             → Python swaps without temp (tuple unpacking)
```

## 🔹 String repetition

```python
print("a" * 5)  # aaaaa
```

## 🔹 Multiple return values

```python
def convert_time(days):
    return hours, minutes

hh, mm = convert_time(days)
```

# 📘 Week 04 – Functions (Advanced)

## 🔹 Default Parameters

```python
def print_line(char="*", length=10):
    print(char * length)
```

👉 If no argument is given → uses default value

## 🔹 Important Pitfall ⭐

⚠️ Default values are evaluated **once**, not every call

```c
def add_item(lst=None):  # ✅ safer
    if lst is None:
        lst = []
    lst.append(1)
    return lst

def add_item(lst=[]):   # ❌ dangerous
    lst.append(1)
    return lst
```

❗Parameters with defaults must come last

```c
def func(a=1, b):   # SyntaxError
def func(a, b=1):   # ✅ Correct
```

# 📘 Week 05 – Lists

## 🔹 Common Methods

```python
nums_list.count(7)                    # count how many times 7 appears in the list

sorted(lottery_numbers, reverse=True) # return a NEW list sorted in descending order (original unchanged)

results.index(6)                      # return index of first occurrence of 6 (ValueError if not found)
```

⚠️ Error:

```python
ValueError: 6 is not in list
```

## 🔹 Insert

```python
mylist = [0, 1, 2]
mylist.insert(0, 9)   # [9, 0, 1, 2]
```

## 🔹 Remove vs Pop

```python
mylist.remove(value)   # removes first occurrence
mylist.pop()           # removes last element
mylist.pop(index)      # removes at index
```

## 🔹 Delete

```python
del mylist[index]
```

## 🔹 Swap elements

```python
elements[-1], elements[0] = elements[0], elements[-1]
```

## 🔹 index() advanced

```python
ints.index(1)        # first occurrence
ints.index(1, 2)     # start from index 2
ints.index(1, 1, 3)  # search in range [1,3)
```

## 🔹 sorted vs sort ⭐

```python
new_list = sorted(lst)   # returns a new list
lst.sort()               # modifies original list
```

## 🔹 List operators

```python
[1, 2] + [3, 4]   # new list
[0] * 5           # repetition
```

## 🔹 Slicing ⭐

```python
lst[a:b]   # elements from index a to b-1 (end NOT included)

lst[:b]    # from beginning (index 0) to b-1

lst[a:]    # from index a to the end of the list

lst[:]     # copy of the whole list (shallow copy)
```

👉 End index is **not included**

## 🔹 Copying a list ⭐

```python
list2 = list1      # same object (alias)
list2 = list1[:]   # real copy
```

👉 Very important difference

## 🔹 Slice assignment

```python
lst[2:4] = [99, 100]   # replace
lst[2:4] = []          # delete slice
```

## ⚠️ Important Errors

- `ValueError`
- Index out of range

## ⚠️ Critical Pitfall ⭐

👉 **Do NOT modify a list while iterating over it**

❌ Wrong:

```python
for x in lst:
    if x == 1:
        lst.remove(x)
```

✅ Safer:

```python
result = []
for x in lst:
    if x != 1:
        result.append(x)
```

# 📘 Week 06 – Strings

## 🔹 split()

```python
text.split()
```

👉 Splits by whitespace (default)

## 🔹 join()

```python
text = " ".join(wordlist)
```

## 🔹 substring check

```python
"Ann" in text
"Ann" not in text
```

## 🔹 replace()

```python
line = "kokko"
line.replace("ko", "ka")      # kakka
line.replace("ko", "ku", 1)   # kukko
```

## 🔹 strip ⭐

```python
text.strip()    # remove whitespace from BOTH ends (very common when reading input/file lines)

text.lstrip()   # remove whitespace from LEFT (start) only

text.rstrip()   # remove whitespace from RIGHT (end), often used to remove '\n'
```

👉 Very useful when reading files

## 🔹 case conversion ⭐

```python
text.lower()
text.upper()
text.casefold()  # convert string to a normalized lowercase form
```

👉 `casefold()` is best for comparisons

👉 `casefold()` handles special characters better

```c
"ß".lower()     # "ß"
"ß".casefold()  # "ss"
```

## 🔹 find ⭐

```python
text.find("abc")
```

👉 Returns index or `-1` if not found

## 🔹 Type checking

```python
type(x)
isinstance(numerator, int)
```

## 🔹 Object comparison

```python
if self is not another:
```

👉 `is` checks **identity**, not value

## 🔹 String properties ⭐

👉 **Strings are immutable**

```python
text = "abc"
text.upper()   # returns new string
```

## 🔹 Useful checks

```python
text.isalpha()
text.isdigit()
text.islower()
text.isupper()
text.isspace()
```

⚠️ Important:

```python
"123".isdigit()   # True
"-123".isdigit()  # False
"12.3".isdigit() # False
```

## 🔹 Method chaining ⭐

```python
line.lower().count("koko")
```

## 🔹 Common Exceptions

- `ValueError` → wrong value
- `TypeError`→ wrong type
- `OSError`→ file/system error
- `IndexError` → list index out of range
- `NameError` → variable not defined
- `KeyError` → dictionary key not found

# 📘 Week 07 – Dictionary & Set

## 🔹 Dictionary Basics

```python
d = {"Alice": 25, "Bob": 30}
```

👉 Key–value pairs

👉 Keys must be **unique** and **immutable**

## 🔹 Access & Modify

```python
d["Alice"]        # 25
d["Charlie"] = 40 # add new key
```

## 🔹 Iteration

```python
for key in d:
    print(key)

for key, value in d.items():
    print(key, value)
```

👉 `.items()` is the most useful in practice

## 🔹 Safe Access

```python
if "Alice" in d:
    print(d["Alice"])
```

👉 Avoids `KeyError`

### ⭐ Better way: `get()`

```python
d.get("Alice", 0)   # return value for key "Alice", or 0 if key not found (no error)
```

👉 Returns default value if key not found

## 🔹 Removing elements

```python
del d["Alice"]        # remove key "Alice" (no return value)

value = d.pop("Bob")  # remove key "Bob" and RETURN its value
```

## 🔹 Sorting dictionary

```python
for key in sorted(d):
    print(key, d[key])
```

## 🔹 Set (important for duplicates)

```python
s = set([1, 2, 2, 3])   # {1,2,3}
```

## 🔹 Set operations

```python
a | b   # union
a & b   # intersection
a - b   # difference
```

## ⚠️ Common mistakes

- ❌ `d["missing"]` → KeyError
- ❌ assuming order (dict/set are conceptually unordered)

# 📘 Week 08 – File Processing

```c
# "r" → file must exist ❗ → otherwise OSError
# "w" → creates file if not exist, but erases content
# "a" → creates file if not exist, keeps old content

open("file.txt", "r")   # read file
open("file.txt", "w")   # overwrite file
open("file.txt", "a")   # append to file
```

## 🔹 1. Read file line by line ⭐ (most common)

```python
with open("file.txt") as f:
    for line in f:
        print(line.strip())
```

👉 **Use when:**

- Processing file line by line
- Reading structured data (e.g. `split(";")`)
- Building lists or dictionaries

## 🔹 2. Read entire file

```python
with open("file.txt", "r") as f:
    data = f.read()
```

👉 **Use when:**

- You need the whole file as one string
- Searching or analyzing full text

## 🔹 3. Error handling with file

```python
try:
    with open("file.txt") as f:
        data = f.read()
except OSError:
    print("Error")
```

👉 **Use when:**

- File may not exist
- You want to handle errors safely

### 🔹 Why `with`?

👉 Automatically closes the file

👉 Prevents resource leaks

## 🔹 4. Manual open (NOT recommended)

```python
f = open("file.txt")

try:
    data = f.read()
finally:
    f.close()
```

👉 Works, but:

- More code
- Easy to forget `close()`
- Less safe than `with`

## 🔹 Splitting file lines

```python
parts = line.strip().split(";")
```

## 🔹 Building data structures

```python
data = {}

for line in file:
    name, score = line.strip().split(";")
    data[name] = int(score)
```

## ⚠️ Common errors

- `FileNotFoundError`
- forgetting `strip()`
- wrong split delimiter

# 📘 Week 09 – Nested Data Structures

## 🔹 Typical structure

```python
{
    "Alice": [10, 20, 30],
    "Bob": [5, 15]
}
```

## 🔹 Access pattern

```python
for name in data:
    for value in data[name]:
        print(name, value)
```

## 🔹 Adding values

```python
if name not in data:
    data[name] = []

data[name].append(score)
```

## 🔹 Real pattern (VERY IMPORTANT)

👉 “grouping data”

```python
groups = {}

for item in items:
    key = ...
    value = ...

    if key not in groups:
        groups[key] = []

    groups[key].append(value)
```

## 🔹 Nested dict

```python
{
  "Alice": {"math": 90, "eng": 85}
}
```

## ⚠️ Common mistakes

- forgetting to initialize list
- wrong indexing level

# 📘 Week 10 – Classes & Objects

## 🔹 Class structure

```python
class Car:
    def __init__(self, tank):
        self.__tank = tank
```

## 🔹 Object creation

```python
car = Car(50)
```

## 🔹 Methods

```python
def get_tank(self):
    return self.__tank
```

## 🔹 Using methods

```python
car.get_tank()
```

## 🔹 Private attributes

```python
self.__tank
```

## 🔹 Setter & Getter

```python
def set_tank(self, value):
    if value < 0:
        raise ValueError
    self.__tank = value
```

## 🔹 Modifying state

```python
self.__gas += amount
```

## 🔹 Comparing objects

```python
if self is not another:
```

👉 `is` = identity

👉 `==` = value comparison (if defined)

## 🔹 Common exceptions

- `ValueError`
- `TypeError`

## ⚠️ Critical mistakes (VERY COMMON)

### ❌ Missing `self`

```python
def func():   # wrong
```

### ❌ Accessing private incorrectly

```python
car.__tank   # wrong ❌ AttributeError
print(car._Car__tank)   # ✔ works,not recommended
```

### ❌ Formatting mistake

```python
f"{x:1f}"   # wrong
f"{x:.1f}"  # correct
```

### ❌ Logic error in methods

(e.g. forgetting to update attributes)

# 📘 Name Mangling

## 🔹 What is Name Mangling?

```python
class Car:
    def __init__(self):
        self.__speed = 100
```

👉 Python automatically changes the name:

```python
self._Car__speed
```

👉 This process is called **name mangling**

## 🔹 Why is it used?

```
To avoid accidental access or overriding of attributes
```

- Especially useful in inheritance
- Prevents name conflicts between classes

## 🔹 Not truly private ❗

```python
car = Car()
print(car._Car__speed)   # still accessible
```

👉 So:

```
Not truly private → still accessible if you know the name
```

## 🔹 More like “protected”

```
Means: "You can access it, but you should not"
```

👉 It is a **convention**, not strict enforcement

## 🔹 Comparison

```python
self.x     # public (accessible anywhere)

self._x    # protected (by convention, do not use outside class)

self.__x   # name mangling (stronger protection)
```

## 🔹 Why use `__x`?

👉 Prevent conflicts in subclasses

```python
class A:
    def __init__(self):
        self.__x = 1

class B(A):
    def __init__(self):
        self.__x = 2
```

👉 Becomes:

```
A → _A__x
B → _B__x
```

✔ No conflict between parent and child class
