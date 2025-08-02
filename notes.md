
# 🐍Python
## Preset
- Created by Guido van Rossum in 1990, Python 3 released in 2008
- Emphasizes readability and simplicity
- Official docs: [docs.python.org/3](https://docs.python.org/3)

## Table of Contents

- [Input and Output ](#input-and-output)
- [Variables](#variables)
- [Keywords](#kaywords)
- [Data Types](#data-types)
- [Conditional Statements](#conditional-statements)
- [Loops](#loops)
- [Functions](#functions)
- [Different types of Data Structure](#different-types-of-data-structure)
- [Strings](#strings)
- [List](#list)
- [Tuples](#tuples)
- [Dictionary](#dictionary)
- [Sets](#sets)
- [Arrays](arrays)
- [List Comprehension](#list-comprehension)


## Input and Output 

This document summarizes all major types of input and output declarations in Python for quick reference.

#### 📥 Input Methods

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| String Input              | `name = input("Enter your name: ")`                                              |
| Integer Input             | `age = int(input("Enter your age: "))`                                           |
| Float Input               | `price = float(input("Enter price: "))`                                          |
| Multiple Int Inputs       | `a, b = map(int, input().split())`                                               |
| List of Ints              | `nums = list(map(int, input().split()))`                                         |
| List of Strings           | `words = input().split()`                                                        |
| Characters List           | `chars = list(input())`                                                          |
| 2D Matrix Input           | `matrix = [list(map(int, input().split())) for _ in range(rows)]`                |
| Command-line Args         | `import sys\\nargs = sys.argv[1:]`                                               |

#### 📤 Output Methods

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| Basic Print               | `print("Hello")`                                                                 |
| Print Variables           | `print("Name:", name)`                                                           |
| f-string Output           | `print(f"My name is {name}")`                                                    |
| Custom Separator          | `print("A", "B", sep="-")`                                                       |
| No Newline                | `print("Hello", end="")`                                                         |
| Format               | `print("{0} and Portal".format("Geeks"))`                                                         |


#### 📂 File Input/Output

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| Read File                 | `with open("input.txt") as f: data = f.read()`                                   |
| Write to File             | `with open("file.txt", "w") as f: f.write("text")`                               |
| Append to File            | `with open("file.txt", "a") as f: f.write("more")`                               |
| Read Line by Line         | `for line in open("file.txt"):`                                                  |

#### 🔄 Loop Input

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| Loop Input List           | `nums = []\\nfor _ in range(n): nums.append(int(input()))`                       |
| Loop 2D Matrix Input      | `for i in range(rows):\\n row = list(map(int, input().split()))\\n matrix.append(row)` |

#### ⚡ List Comprehension

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| List of Ints              | `[int(x) for x in input().split()]`                                              |
| 2D Matrix Input           | `[list(map(int, input().split())) for _ in range(rows)]`                         |
| List of Squares           | `[x**2 for x in nums]`                                                           |
| Conditional List          | `[x for x in nums if x % 2 == 0]`                                                |

#### 🛡️ Error Handling

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| Try/Except Input          | `try: val = int(input())\\nexcept ValueError: print("Invalid input")


# Variables

| Type of Variable Declaration       | Description                                        | Example                                           |
|-----------------------------------|--------------------------------------------------|--------------------------------------------------|
| Basic Variable Declaration         | Assign value directly; dynamic typing             | `x = 10`<br>`name = "Rajashree"`                 |
| Multiple Variable Assignment       | Assign multiple variables in one line             | `a, b, c = 1, 2, 3`<br>`x = y = z = "same"`     |
| Type Hinting (Python 3.5+)         | Declare variable types for readability            | `age: int = 25`<br>`name: str = "Rajashree"`    |
| Constants (By Convention)           | Uppercase names for values that should not change | `PI = 3.14159`<br>`MAX_LIMIT = 100`              |
| Global and Local Variables          | Variables inside/outside functions                  | `x = 100  # Global`<br>`def f(): y=200  # Local` |
| Using `global` and `nonlocal`       | Keywords to modify variable scope                   | `global count`<br>`nonlocal x`                    |
| Class and Instance Variables        | Variables shared by class or per instance           | `class_var = 10`<br>`self.instance_var = 5`      |
| Data Structures as Variables        | Lists, tuples, sets, dictionaries                    | `my_list = [1,2,3]`<br>`my_dict = {"a": 1}`     |
| NoneType Variable                   | Variable assigned None                              | `result = None`                                   |
| Environment Variables (`os.environ`)| Variables from OS environment                         | `import os`<br>`os.environ['API_KEY'] = 'key'`   |
| Assign Function to Variable         | Functions can be assigned to variables              | `def greet(): `<br>` print("Hello") `<br>`say_hello = greet `<br>`say_hello()`                               |
| Passing Function as an Argument         | Functions can be assigned as an Argument               | `def greet(): `<br>` return "Hi! `<br>`def call_function(func): `<br>`message =func() `<br>`print(meassge)`<br>`call_function(greet)` 
| Returning Functions from Another Function         | Functions can be assigned from Another Function               | `def outer(): `<br>` def inner(): `<br>` return "I’m the inner function!" `<br>` return inner `<br>`my_func = outer() `<br>` print(my_func())` |
| Insert Variable into a String      | Combine variables and text in a string             | `f"My name is {name}"`<br>`"My age is {}".format(age)`<br>`"Age: " + str(age)` |
| Type Casting – Implicit            | Python auto-converts type                          | `z = 5 + 3.2` → `z` becomes `float` (8.2)                               |
| Type Casting – Explicit            | Manually convert between types                     | `int("10")`<br>`float(5)`<br>`str(123)`<br>`bool(0)`                    |


# Operators
| **Operator Type** | **Operator** | **Example**      | **Description**    |
| ----------------- | ------------ | ---------------- | ------------------ |
| **Arithmetic**    | `+`          | `2 + 3` → `5`    | Addition           |
|                   | `-`          | `5 - 2` → `3`    | Subtraction        |
|                   | `*`          | `3 * 4` → `12`   | Multiplication     |
|                   | `/`          | `10 / 2` → `5.0` | Division (float)   |
|                   | `//`         | `10 // 3` → `3`  | Floor division     |
|                   | `%`          | `10 % 3` → `1`   | Modulo (remainder) |
|                   | `**`         | `2 ** 3` → `8`   | Exponentiation     |
| Comparison | == | 5 == 5 → True | Equal to |
| | != | 5 != 3 → True | Not equal to |
| | > | 5 > 3 → True | Greater than |
| | < | 2 < 3 → True | Less than |
| | >= | 5 >= 5 → True | Greater than or equal to |
| | <= | 3 <= 4 → True | Less than or equal to |
| Logical | and | True and False → False | Logical AND |
| | or | True or False → True | Logical OR |
| | not | not True → False | Logical NOT |
| Bitwise | & | 5 & 3 → 1 | AND |
| | | | 5 | 3 → 7 | OR |
| | ^ | 5 ^ 3 → 6 | XOR |
| | ~ | ~5 → -6 | NOT |
| | << | 2 << 1 → 4 | Left Shift |
| | >> | 4 >> 1 → 2 | Right Shift |
| Assignment | = | a = 5 | Assign value |
| | += | a += 2 → a = a + 2 | Add and assign |
| | -= | a -= 3 → a = a - 3 | Subtract and assign |
| | *= | a *= 2 → a = a * 2 | Multiply and assign |
| | /= | a /= 2 | Divide and assign |
| | //=, %= | a %= 2 | Floor/Modulo assign |
| | **=, &=, |=, ^=, <<=, >>= | Compound assignment |
| Identity | is | a is b | True if same object |
| | is not | a is not b | True if not same object |
| Membership | in | 'a' in 'apple' → True | Is member |
| | not in | 'x' not in 'apple' → True | Not member |
| Modulo | % | 10 % 3 → 1 | Remainder of division |
| Division | / | 10 / 4 → 2.5 | True division |
| | // | 10 // 4 → 2 | Floor division |
| Ternary Operator | x if condition else y | a = 10 if b > 5 else 20 | Conditional expression |
| Operator Overloading | +, -, etc. | class A: def __add__(self, other): ... | Custom behavior for operators in classes |
| OR (Logical) | or | True or False → True | Used to combine conditions |

# Keywords
| Keyword        | Description                               | Example                                  |
|----------------|-------------------------------------------|------------------------------------------|
| `False`        | Boolean value                             | `x = False`                              |
| `None`         | Represents null value                     | `x = None`                               |
| `True`         | Boolean value                             | `x = True`                               |
| `and`          | Logical AND                               | `if a > 0 and b > 0:`                    |
| `as`           | Alias or context manager                  | `import numpy as np`                     |
| `assert`       | Debugging check                           | `assert x > 0`                           |
| `async`        | Declare asynchronous function             | `async def fetch():`                    |
| `await`        | Wait for async result                     | `await fetch()`                          |
| `break`        | Exit loop                                 | `if x == 5: break`                       |
| `class`        | Define a class                            | `class Person:`                          |
| `continue`     | Skip iteration in loop                    | `if x % 2 == 0: continue`                |
| `def`          | Define function                           | `def greet():`                           |
| `del`          | Delete object                             | `del my_list[0]`                         |
| `elif`         | Else if condition                         | `elif x == 2:`                           |
| `else`         | Else condition                            | `else:`                                  |
| `except`       | Handle exception                          | `except ValueError:`                     |
| `finally`      | Run no matter what                        | `finally:`                               |
| `for`          | Looping                                   | `for i in range(5):`                     |
| `from`         | Import specific part                      | `from math import sqrt`                  |
| `global`       | Declare global variable                   | `global counter`                         |
| `if`           | Conditional branching                     | `if x > 0:`                              |
| `import`       | Import module                             | `import os`                              |
| `in`           | Check membership                          | `if 3 in [1,2,3]:`                        |
| `is`           | Identity comparison                       | `if a is b:`                             |
| `lambda`       | Anonymous function                        | `f = lambda x: x + 1`                    |
| `nonlocal`     | Declare outer function variable           | `nonlocal count`                         |
| `not`          | Logical NOT                               | `if not valid:`                          |
| `or`           | Logical OR                                | `if a > 5 or b < 3:`                     |
| `pass`         | Do nothing                                | `if x > 0: pass`                         |
| `raise`        | Raise exception                           | `raise ValueError("Invalid")`           |
| `return`       | Exit function and return value            | `return x + y`                           |
| `try`          | Try block for exception                   | `try:`                                   |
| `while`        | While loop                                | `while x < 5:`                           |
| `with`         | Context manager                           | `with open("file.txt") as f:`           |
| `yield`        | Yield value in generator                  | `yield x`                                |

# Data Types
| Type      | Category      | Description                      | Example                |
| --------- | ------------- | -------------------------------- | ---------------------- |
| `int`     | Primitive     | Integer values                   | `x = 10`               |
| `float`   | Primitive     | Decimal/real numbers             | `x = 10.5`             |
| `complex` | Primitive     | Complex numbers                  | `x = 3 + 4j`           |
| `bool`    | Primitive     | Boolean values: True or False    | `x = True`             |
| `str`     | Primitive     | Sequence of characters (strings) | `x = "Hello"`          |
| `list`    | Non-Primitive | Ordered, mutable collection      | `x = [1, 2, 3]`        |
| `tuple`   | Non-Primitive | Ordered, immutable collection    | `x = (1, 2, 3)`        |
| `set`     | Non-Primitive | Unordered, no duplicates         | `x = {1, 2, 3}`        |
| `dict`    | Non-Primitive | Key-value pairs                  | `x = {"a": 1, "b": 2}` |
| Function       | Purpose                         | Example Input        | Output            |
| -------------- | ------------------------------- | -------------------- | ----------------- |
| `int()`        | Convert to integer              | `int("10")`          | `10`              |
| `float()`      | Convert to float                | `float("3.14")`      | `3.14`            |
| `complex()`    | Convert to complex number       | `complex(2, 3)`      | `(2+3j)`          |
| `bool()`       | Convert to boolean              | `bool(0)`            | `False`           |
| `str()`        | Convert to string               | `str(100)`           | `'100'`           |
| `list()`       | Convert to list                 | `list("abc")`        | `['a', 'b', 'c']` |
| `tuple()`      | Convert to tuple                | `tuple([1, 2])`      | `(1, 2)`          |
| `set()`        | Convert to set                  | `set([1, 2, 2])`     | `{1, 2}`          |
| `dict()`       | Create dictionary from pairs    | `dict([('a',1)])`    | `{'a': 1}`        |
| `type()`       | Get type of variable            | `type(3.14)`         | `<class 'float'>` |
| `isinstance()` | Check data type                 | `isinstance(5, int)` | `True`            |
| `len()`        | Get length of sequence or dict  | `len("hello")`       | `5`               |
| `round()`      | Round a float                   | `round(3.56)`        | `4`               |
| `format()`     | Format string or numbers        | `"{}".format(5)`     | `'5'`             |
| `repr()`       | String representation of object | `repr("abc")`        | `"'abc'"`         |
| `eval()`       | Evaluate expression from string | `eval("3 + 5")`      | `8`               |

# Conditional Statements
| **Type**                           | **Syntax**                                                                              | **Example**                                                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Simple `if`**                 | `if condition:`<br>    `# code`                                                         | `x = 10`<br>`if x > 5:`<br>    `print("x is greater than 5")`                                                                         |
| **2. `if-else`**                   | `if condition:`<br>    `# code`<br>`else:`<br>    `# code`                              | `x = 3`<br>`if x > 5:`<br>    `print("Big")`<br>`else:`<br>    `print("Small")`                                                       |
| **3. `if-elif-else`**              | `if cond1:`<br>    `# code`<br>`elif cond2:`<br>    `# code`<br>`else:`<br>    `# code` | `x = 0`<br>`if x > 0:`<br>    `print("Positive")`<br>`elif x == 0:`<br>    `print("Zero")`<br>`else:`<br>    `print("Negative")`      |
| **4. Nested `if`**                 | `if cond1:`<br>    `if cond2:`<br>        `# code`                                      | `x = 15`<br>`if x > 10:`<br>    `if x < 20:`<br>        `print("Between 10 and 20")`                                                  |
| **5. One-line if**                 | `if condition: statement`                                                               | `x = 7`<br>`if x > 5: print("x is greater than 5")`                                                                                   |
| **6. One-line if-else**            | `val = a if condition else b`                                                           | `x = 8`<br>`result = "Even" if x % 2 == 0 else "Odd"`<br>`print(result)`                                                              |
| **7. Multiple conditions**         | `if cond1 and cond2:`<br>    `# code`                                                   | `x = 10; y = 5`<br>`if x > 5 and y < 10:`<br>    `print("Valid")`                                                                     |
| **8. `if` with `and`**             | `if a and b:`<br>    `# code`                                                           | `is_logged_in = True`<br>`is_admin = True`<br>`if is_logged_in and is_admin:`<br>    `print("Access granted")`                        |
| **9. `match-case`** (Python 3.10+) | `match variable:`<br>`case value1:`<br>    `# code`<br>`case value2:`<br>    `# code`   | `fruit = "apple"`<br>`match fruit:`<br>`case "apple":`<br>    `print("Red fruit")`<br>`case "banana":`<br>    `print("Yellow fruit")` |
| **10. Ternary Operator**           | `value_if_true if condition else value_if_false`                                        | `a, b = 5, 10`<br>`min_val = a if a < b else b`<br>`print(min_val)`                                                                   |

# Loops
| **Topic**                           | **Explanation**                               | **Example**                                                                                |
| ----------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **1. `for` Loop**                   | Iterates over a sequence (list, string, etc.) | `for i in [1, 2, 3]: print(i)`<br>**Output:** 1 2 3                                        |
| **2. For Loop with String**         | Loops through each character                  | `for ch in "Hi": print(ch)`<br>**Output:** H i                                             |
| **3. `range()` with For Loop**      | Iterates over a range of numbers              | `for i in range(3): print(i)`<br>**Output:** 0 1 2                                         |
| **4. `range(start, stop, step)`**   | Custom range control                          | `for i in range(2, 10, 3): print(i)`<br>**Output:** 2 5 8                                  |
| **5. `continue` Statement**         | Skips current iteration                       | `for i in range(5): if i==2: continue; print(i)`<br>**Output:** 0 1 3 4                    |
| **6. `break` Statement**            | Exits loop early                              | `for i in range(5): if i==3: break; print(i)`<br>**Output:** 0 1 2                         |
| **7. `pass` Statement**             | Does nothing (placeholder)                    | `for i in range(2): pass` (No output)                                                      |
| **8. For-Else**                     | Runs `else` if loop **doesn't break**         | `for i in range(2): print(i); else: print("Done")`<br>**Output:** 0 1 Done                 |
| **9. For-Else with Break**          | Skips `else` if loop **breaks**               | `for i in range(3): if i==1: break; print(i); else: print("Done")`<br>**Output:** 0        |
| **10. `enumerate()` with For Loop** | Index and item from sequence                  | `for i, v in enumerate(['a','b']): print(i, v)`<br>**Output:** 0 a <br>1 b                 |
| **11. Nested For Loop**             | Loop inside a loop                            | `for i in range(2): for j in range(2): print(i,j)`<br>**Output:** 0 0<br>0 1<br>1 0<br>1 1 |
| **12. `while` Loop**              | Repeats **as long as** a condition is True         | `i = 0\nwhile i < 3:\n    print(i)\n    i += 1`<br>**Output:** 0 1 2                               |
| **13. Infinite `while` Loop**     | Condition is always True (use `break` to stop)     | `while True:\n    print("Run")\n    break`<br>**Output:** Run                                      |
| **14. `while` with `continue`**   | Skips current iteration                            | `i = 0\nwhile i < 3:\n    i += 1\n    if i == 2: continue\n    print(i)`<br>**Output:** 1 3        |
| **15. `while` with `break`**      | Exits when condition met                           | `i = 0\nwhile i < 5:\n    if i == 3: break\n    print(i)\n    i += 1`<br>**Output:** 0 1 2         |
| **16. `while`-`else`**            | `else` executes if no break                        | `i = 0\nwhile i < 2:\n    print(i)\n    i += 1\nelse:\n    print("Done")`<br>**Output:** 0 1 Done  |
| **17. Simulated `do-while` Loop** | Loop runs **at least once**, then checks condition | `i = 0\nwhile True:\n    print(i)\n    i += 1\n    if i >= 3:\n        break`<br>**Output:** 0 1 2 |

# Functions

| **Concept**                       | **Explanation**                                             | **Example Code**                                                                                                                                                                                                                   |
| --------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Basic Python Function**      | Defines reusable blocks of code using `def`.                | `def greet():`<br>`    print("Hello!")`<br>`greet()`                                                                                                                                                                               |
| **2. Pass Statement in Function** | `pass` is used when the function has no implementation yet. | `def future_function():`<br>`    pass`                                                                                                                                                                                             |
| **3. Global and Local Variables** | Local vars exist inside a function; global vars outside.    | `x = 10`<br>`def show():`<br>`    x = 5`<br>`    print("Local x:", x)`<br>`show()`<br>`print("Global x:", x)`                                                                                                                      |
| **4. Recursion in Python**        | A function calling itself to solve smaller subproblems.     | `def factorial(n):`<br>`    if n == 1:`<br>`        return 1`<br>`    return n * factorial(n - 1)`<br>`print(factorial(5))`                                                                                                        |
| **5. \*args in Function**         | Used to pass variable number of non-keyworded arguments.    | `def add(*numbers):`<br>`    total = 0`<br>`    for num in numbers:`<br>`        total += num`<br>`    return total`<br>`print(add(1, 2, 3))`                                                                                      |
| **6. \*\*kwargs in Function**     | Used to pass variable number of keyworded arguments.        | `def print_info(**kwargs):`<br>`    for key, value in kwargs.items():`<br>`        print(key, ":", value)`<br>`print_info(name="Raj", age=25)`                                                                                     |
| **7. 'self' as Default Argument** | Refers to the instance of the class in object methods.      | `class Person:`<br>`    def greet(self):`<br>`        print("Hello from instance")`<br>`p = Person()`<br>`p.greet()`                                                                                                               |
| **8. First-Class Function**       | Functions can be passed as arguments, returned, assigned.   | `def shout(text):`<br>`    return text.upper()`<br>`def greet(func):`<br>`    print(func("hello"))`<br>`greet(shout)`                                                                                                              |
| **9. Lambda Function**            | Small anonymous function using `lambda`.                    | `square = lambda x: x * x`<br>`print(square(5))`                                                                                                                                                                                   |
| **10. Map Function**              | Applies a function to every item of an iterable.            | `nums = [1, 2, 3, 4]`<br>`squared = list(map(lambda x: x*x, nums))`<br>`print(squared)`                                                                                                                                            |
| **11. Reduce Function**           | Applies rolling computation to items (from functools).      | `from functools import reduce`<br>`nums = [1, 2, 3, 4]`<br>`product = reduce(lambda x, y: x * y, nums)`<br>`print(product)`                                                                                                        |
| **12. Filter Function**           | Filters elements based on a condition.                      | `nums = [1, 2, 3, 4, 5]`<br>`even = list(filter(lambda x: x % 2 == 0, nums))`<br>`print(even)`                                                                                                                                     |
| **13. Inner Function**            | Function defined inside another function.                   | `def outer():`<br>`    def inner():`<br>`        print("Inner function")`<br>`    inner()`<br>`outer()`                                                                                                                            |
| **14. Decorators**                | Wraps a function to extend its behavior.                    | `def decorator(func):`<br>`    def wrapper():`<br>`        print("Before")`<br>`        func()`<br>`        print("After")`<br>`    return wrapper`<br>`@decorator`<br>`def say_hello():`<br>`    print("Hello")`<br>`say_hello()` |

# Different types of Data Structure
🧱 Built-in Data Structures
| **Data Structure**            | **Type** | **Description**                       | **Example (code line by line)**                                                               |
| ----------------------------- | -------- | ------------------------------------- | --------------------------------------------------------------------------------------------- |
| **List**                      | Built-in | Ordered, mutable, allows duplicates   | my\_list = \[1, 2, 3, 4]<br>my\_list.append(5)<br>print(my\_list)  # Output: \[1, 2, 3, 4, 5] |
| **Tuple**                     | Built-in | Ordered, immutable, allows duplicates | my\_tuple = (1, 2, 3)<br>print(my\_tuple\[0])  # Output: 1                                    |
| **Set**                       | Built-in | Unordered, mutable, no duplicates     | my\_set = {1, 2, 2, 3}<br>print(my\_set)  # Output: {1, 2, 3}                                 |
| **FrozenSet**                 | Built-in | Immutable version of set              | frozen = frozenset(\[1, 2, 3])<br>print(frozen)  # Output: frozenset({1, 2, 3})               |
| **Dictionary (dict)**         | Built-in | Key-value pairs, mutable              | my\_dict = {'a': 1, 'b': 2}<br>print(my\_dict\['a'])  # Output: 1                             |
| **String**                    | Built-in | Immutable sequence of characters      | text = "hello"<br>print(text\[1])  # Output: e                                                |
| **Array (from array module)** | Module   | Efficient list for numeric data       | from array import array<br>arr = array('i', \[1, 2, 3])<br>print(arr\[0])  # Output: 1        |

📚 User-defined Data Structures

| **Data Structure**     | **Description**             | **Example (line by line)**                                                                                                                         |
| ---------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stack (LIFO)**       | Last In First Out           | stack = \[]<br>stack.append(1)<br>stack.append(2)<br>stack.pop()  # Output: 2                                                                                        |
| **Queue (FIFO)**       | First In First Out          | from collections import deque<br>queue = deque()<br>queue.append(1)<br>queue.popleft()  # Output: 1                                                                  |
| **Linked List**        | Nodes connected in sequence | class Node:<br>  def **init**(self, data):<br>    self.data = data<br>    self.next = None<br>head = Node(1)<br>head.next = Node(2)<br>print(head.data)  # Output: 1 |
| **Doubly Linked List** | Each node has prev and next | Similar to linked list, but with `prev` pointer too                                                                                                                  |
| **Tree**               | Hierarchical structure      | class TreeNode:<br>  def **init**(self, value):<br>    self.value = value<br>    self.left = None<br>    self.right = None                                           |
| **Graph**              | Nodes connected by edges    | graph = {<br>  'a': \['b', 'c'],<br>  'b': \['a', 'd'],<br>  'c': \['a'],<br>}<br>print(graph\['a'])  # Output: \['b', 'c']                                          |

🏗️ Advanced Data Structures 
| **Data Structure**             | **Module**    | **Example**                                                                                                                    |
| ------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **deque (Double-ended queue)** | `collections` | from collections import deque<br>dq = deque(\[1, 2, 3])<br>dq.appendleft(0)<br>print(dq)  # Output: deque(\[0, 1, 2, 3])       |
| **defaultdict**                | `collections` | from collections import defaultdict<br>d = defaultdict(int)<br>d\['a'] += 1<br>print(d\['a'])  # Output: 1                     |
| **OrderedDict**                | `collections` | from collections import OrderedDict<br>od = OrderedDict()<br>od\['a'] = 1<br>print(od)                                         |
| **Counter**                    | `collections` | from collections import Counter<br>c = Counter("hello")<br>print(c)  # Output: Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})       |
| **NamedTuple**                 | `collections` | from collections import namedtuple<br>Point = namedtuple('Point', 'x y')<br>p = Point(1, 2)<br>print(p.x)  # Output: 1         |
| **Heap (Priority Queue)**      | `heapq`       | import heapq<br>heap = \[3, 1, 4]<br>heapq.heapify(heap)<br>heapq.heappush(heap, 2)<br>print(heapq.heappop(heap))  # Output: 1 |

# Strings

| **Topic**                                   | **Description**                             | **Example Code**                                                                       | **Output**                             |
| ------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------- |
| **1. String Slicing**                       | Extract a portion using `[start:stop:step]` | `text = "Python"`<br>`print(text[1:4])`                                                | `yth`                                  |
|                                             | Negative indexing                           | `print(text[-4:-1])`                                                                   | `tho`                                  |
| **2. f-Strings**                            | Embed variables inside strings              | `name = "Raj"`<br>`age = 25`<br>`print(f"My name is {name} and I am {age} years old")` | `My name is Raj and I am 25 years old` |
| **3. String Comparison**                    | Compare strings using `==`, `<`, `>`        | `a = "apple"`<br>`b = "banana"`<br>`print(a == b)`<br>`print(a < b)`                   | `False`<br>`True`                      |
| **4. Useful String Functions**              | `.lower()` to lowercase                     | `"HeLLo".lower()`                                                                      | `hello`                                |
|                                             | `.upper()` to uppercase                     | `"python".upper()`                                                                     | `PYTHON`                               |
|                                             | `.strip()` to remove whitespace             | `" hello ".strip()`                                                                    | `hello`                                |
|                                             | `.replace()` to replace characters          | `"hi world".replace("hi", "hello")`                                                    | `hello world`                          |
|                                             | `.find()` to find index                     | `"hello".find("e")`                                                                    | `1`                                    |
|                                             | `.startswith()` to check prefix             | `"hello".startswith("he")`                                                             | `True`                                 |
|                                             | `.endswith()` to check suffix               | `"test.py".endswith(".py")`                                                            | `True`                                 |
| **5. Convert int to string**                | Use `str()` function                        | `num = 123`<br>`s = str(num)`<br>`print(s)`                                            | `123`                                  |
| **6. Convert string to int**                | Use `int()` function                        | `s = "456"`<br>`num = int(s)`<br>`print(num + 1)`                                      | `457`                                  |
| **7. String Concatenation**                 | Using `+` operator                          | `a = "Hi"`<br>`b = "There"`<br>`print(a + b)`                                          | `HiThere`                              |
| **8. Split string into list of characters** | Use `list()`                                | `text = "hello"`<br>`print(list(text))`                                                | `['h', 'e', 'l', 'l', 'o']`            |
| **9. Iterate over characters**              | Use a for loop                              | `for c in "dog":`<br>`    print(c)`                                                    | `d`<br>`o`<br>`g`                      |
| **10. String to List**                      | Using `split()` method                      | `s = "a b c"`<br>`print(s.split())`                                                    | `['a', 'b', 'c']`                      |
| **11. List to String**                      | Use `"".join()`                             | `lst = ['a', 'b', 'c']`<br>`print("".join(lst))`                                       | `abc`                                  |
| **12. String Comparison**                   | Again, for clarity                          | `print("abc" == "ABC")`                                                                | `False`                                |
| **13. String Formatting**                   | `.format()` method                          | `"{} is {}".format("Python", "cool")`                                                  | `Python is cool`                       |
|                                             | `%` operator formatting                     | `"Score: %d" % 90`                                                                     | `Score: 90`                            |
| **14. String Methods**                      | `.title()` capitalizes each word            | `"my name".title()`                                                                    | `My Name`                              |
|                                             | `.capitalize()` first letter capital        | `"hello".capitalize()`                                                                 | `Hello`                                |
| **15. String Exercise**                     | Reverse a string                            | `s = "apple"`<br>`print(s[::-1])`                                                      | `elppa`                                |
| **16. Escape Characters**                   | Use `\\` for backslash                      | `print("Backslash: \\\\")`                                                             | `Backslash: \\`                        |
|                                             | `\'` single quote inside single quotes      | `print('It\\'s fine')`                                                                 | `It's fine`                            |
|                                             | `\"` double quote inside double quotes      | `print("He said, \\\"Hi\\\"")`                                                         | `He said, "Hi"`                        |
|                                             | `\t` tab space                              | `print("Name:\tRaj")`                                                                  | `Name:	Raj`                            |
|--
| **Raw strings `r"string"`**                               | Raw strings treat backslashes `\` as literal characters, useful for Windows paths and regex patterns. |
|                                                           | `path = r"C:\Users\Raj\Documents"`                                                                    |
|                                                           | `print(path)` # Output: C:\Users\Raj\Documents                                                        |
|                                                           | `print("C:\\Users\\Raj\\Documents")` # same output                                                    |
| **Multiline strings `"""string"""`**                      | Used to create strings spanning multiple lines, preserving line breaks and indentation.               |
|                                                           | `text = """This is line 1`                                                                            |
|                                                           | `This is line 2`                                                                                      |
|                                                           | `This is line 3"""`                                                                                   |
|                                                           | `print(text)`                                                                                         |
|                                                           | Output:                                                                                               |
|                                                           | `This is line 1`                                                                                      |
|                                                           | `This is line 2`                                                                                      |
|                                                           | `This is line 3`                                                                                      |
| **String encoding and decoding `.encode()`, `.decode()`** | Strings are Unicode; `.encode()` converts to bytes; `.decode()` converts bytes back to strings.       |
|                                                           | `s = "Hello"`                                                                                         |
|                                                           | `b = s.encode("utf-8")`                                                                               |
|                                                           | `print(b)` # b'Hello'                                                                                 |
|                                                           | `s2 = b.decode("utf-8")`                                                                              |
|                                                           | `print(s2)` # Hello                                                                                   |
| **Regular expressions with `re` module**                  | Used for pattern matching and text processing with powerful regex features.                           |
|                                                           | `import re`                                                                                           |
|                                                           | `text = "The rain in Spain"`                                                                          |
|                                                           | `result = re.findall(r"\bS\w+", text)`  # Finds words starting with 'S'                               |
|                                                           | `print(result)` # \['Spain']                                                                          |
| **Immutable nature of strings**                           | Strings cannot be changed after creation. Any modification returns a new string.                      |
|                                                           | `s = "hello"`                                                                                         |
|                                                           | `# s[0] = 'H'  # Error: TypeError`                                                                    |
|                                                           | `s2 = "H" + s[1:]`                                                                                    |
|                                                           | `print(s2)` # Hello                                                                                   |
| **String translation and mapping `.translate()`**         | Replaces characters according to a translation table created by `.maketrans()`.                       |
|                                                           | `table = str.maketrans("aeiou", "12345")`  # Map vowels to digits                                     |
|                                                           | `s = "hello world"`                                                                                   |
|                                                           | `print(s.translate(table))` # h2ll4 w4rld                                                             |

# List

| Category            | Program Type              | Example Code                                   |
| ------------------- | ------------------------- | ---------------------------------------------- |
| **List Creation**   | Create List with Elements | `my_list = [1, 2, 3, 4, 5]`                    |
|                     | Empty List                | `empty_list = []`                              |
|                     | Using range()             | `range_list = list(range(1, 6))`               |
| **List Add/Append** | Append Element            | `my_list.append(6)`                            |
|                     | Insert at Index           | `my_list.insert(2, 10)`                        |
|                     | Extend List               | `my_list.extend([7, 8])`                       |
| **List Removal**    | Remove by Value           | `my_list.remove(2)`                            |
|                     | Remove by Index           | `del my_list[0]`                               |
|                     | Pop Element               | `last = my_list.pop()`                         |
| **List Count**      | Count Occurrences         | `my_list.count(3)`                             |
|                     | Length of List            | `len(my_list)`                                 |
| **List Checking**   | Element Exists            | `if 4 in my_list:`<br>`    print("Exists")`    |
|                     | List is Empty             | `if not my_list:`<br>`    print("Empty")`      |
| **List with Dict**  | List of Dicts             | `users = [{'name': 'Alice'}, {'name': 'Bob'}]` |
|                     | Access Value              | `print(users[0]['name'])`                      |
| **List of List**    | Create 2D List            | `matrix = [[1, 2], [3, 4]]`                    |
|                     | Access Element            | `val = matrix[1][0]`                           |
| **List with Set**   | Convert List to Set       | `my_set = set(my_list)`                        |
|                     | Remove Duplicates         | `unique = list(set(my_list))`                  |
| **List with Tuple** | List of Tuples            | `pairs = [(1, 'a'), (2, 'b')]`                 |
|                     | Access Tuple Element      | `print(pairs[0][1])`                           |
| **List Methods**    | Sort List                 | `my_list.sort()`                               |
|                     | Reverse List              | `my_list.reverse()`                            |
|                     | Index of Element          | `my_list.index(3)`                             |
|                     | Clear List                | `my_list.clear()`                              |
| **List Slicing**    | Slice Elements            | `slice = my_list[1:4]`                         |
|                     | Reverse with Slicing      | `reversed_list = my_list[::-1]`                |
| List Comprehensions        | Creating lists using concise syntax                   | `[x*x for x in range(5)]`                      |
| Nested List Comprehensions | Comprehensions inside comprehensions                  | `[[i*j for j in range(3)] for i in range(4)]`  |
| List Copying               | Shallow vs deep copy                                  | `copy_list = my_list[:]` or `import copy`      |
| List Iteration             | Looping through list elements                         | `for item in my_list: print(item)`             |
| List Filtering             | Using `filter()` or list comprehension with condition | `[x for x in my_list if x > 3]`                |
| Sorting with Key Function  | Sorting with custom keys                              | `my_list.sort(key=lambda x: x%2)`              |
| List to String Conversion  | Joining list elements into a string                   | `",".join(["a", "b", "c"])`                    |
| Enumerate                  | Get index and value during iteration                  | `for idx, val in enumerate(my_list):`          |
| List Unpacking             | Assign multiple list elements to variables            | `a, b, *rest = [1, 2, 3, 4]`                   |
| Memory Considerations      | Understanding list memory usage and efficiency        | Use `sys.getsizeof()` to check                 |
| Using `any()` and `all()`  | Check conditions across list elements                 | `any(x > 5 for x in my_list)`                  |
| List Flattening            | Convert nested lists into a single list               | Using loops or itertools                       |
| Using `zip()` with Lists   | Combine multiple lists element-wise                   | `list(zip(list1, list2))`                      |
| List Performance Tips      | When to use lists vs other data structures            | For example, prefer sets for membership checks |

# Tuples

| Topic                        | Description                                                | Example Code (line by line)                                      |
| ---------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- |
| Creating tuples              | How to create tuples including empty and multiple values   | `t1 = ()`<br>`t2 = (1, 2, 3)`<br>`t3 = 4, 5, 6`                  |
| Single-element tuple         | Creating a tuple with only one element needs a comma       | `t = (7,)`<br>`print(type(t))`                                   |
| Accessing elements           | Access tuple elements by index                             | `t = (10, 20, 30)`<br>`print(t[0])`                              |
| Negative indexing            | Access elements from the end                               | `print(t[-1])`                                                   |
| Slicing tuples               | Extract a portion of the tuple                             | `print(t[1:3])`                                                  |
| Tuple unpacking              | Assign tuple elements to variables                         | `a, b, c = t`<br>`print(a, b, c)`                                |
| Ignoring values in unpacking | Use underscore to ignore certain elements during unpacking | `a, _, c = t`                                                    |
| Nested tuples                | Tuples inside tuples and accessing nested elements         | `nested = (1, (2, 3), 4)`<br>`print(nested[1][0])`               |
| Immutable nature             | Tuples cannot be changed after creation                    | `t[0] = 10  # Raises error`                                      |
| Tuple methods                | Use built-in methods like count and index                  | `t = (1, 2, 2, 3)`<br>`print(t.count(2))`<br>`print(t.index(3))` |
| Tuple concatenation          | Combine two tuples into one                                | `t1 = (1, 2)`<br>`t2 = (3, 4)`<br>`t3 = t1 + t2`                 |
| Repeating tuples             | Repeat the elements of a tuple multiple times              | `t = (1, 2) * 3`                                                 |
| Tuple length                 | Get the number of elements in a tuple                      | `print(len(t))`                                                  |
| Check element in tuple       | Check if an element exists in the tuple                    | `print(3 in t)`                                                  |
| Iterating over tuples        | Loop through tuple elements                                | `for item in t:`<br>`    print(item)`                            |
| Tuple as dictionary key      | Tuples can be used as keys in dictionaries (immutable)     | `d = { (1, 2): "value" }`                                        |
| Tuple conversion             | Convert lists to tuples and vice versa                     | `list_t = list(t)`<br>`tuple_l = tuple([1, 2, 3])`               |
| Tuple vs List differences    | Tuples are immutable; lists are mutable                    | (Explanation only - no code needed)                              |
| Using tuples in functions    | Pass tuples as arguments and return values                 | `def f(t):`<br>`    return t[0]`<br>`print(f((10, 20)))`         |
| Tuple with mixed data types  | Tuples can hold different data types                       | `t = (1, "hello", 3.14, True)`                                   |

# Dictionary

| Topic                                | Description                                                                                  | Code Example                                                                                                                 |                                                                                 |      |
| ------------------------------------ | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---- |
| **Dictionary Comprehension**         | Create dictionaries using expressions in a concise way                                       | `squares = {x: x*x for x in range(1,6)}`<br>`print(squares)`                                                                 |                                                                                 |      |
|                                      | Conditional comprehension                                                                    | `even_squares = {x: x*x for x in range(1,11) if x % 2 == 0}`<br>`print(even_squares)`                                        |                                                                                 |      |
| **Dictionary Methods**               | Common methods like `keys()`, `values()`, `items()`, `get()`, `pop()`, `update()`, `clear()` | `d = {'a':1, 'b':2}`<br>`print(d.keys())`<br>`print(d.get('a'))`<br>`d.update({'c':3})`<br>`print(d)`                        |                                                                                 |      |
| **Dictionary Creation**              | Different ways to create dictionaries                                                        | `d1 = {}`<br>`d2 = dict()`<br>`d3 = dict(a=1, b=2)`<br>`d4 = dict([('x',10), ('y',20)])`                                     |                                                                                 |      |
| **Dictionary Add/Append**            | Add or update key-value pairs                                                                | `d = {}`<br>`d['key'] = 'value'`<br>`d.update({'new_key': 100})`<br>`print(d)`                                               |                                                                                 |      |
| **Dictionary Removal**               | Remove keys using `pop()`, `popitem()`, `del`, `clear()`                                     | `d = {'a':1,'b':2}`<br>`d.pop('a')`<br>`del d['b']`<br>`d.clear()`<br>`print(d)`                                             |                                                                                 |      |
| **Dictionary Access**                | Access values by key, with or without default values                                         | `d = {'a':1}`<br>`print(d['a'])`<br>`print(d.get('b', 'Not Found'))`                                                         |                                                                                 |      |
| **Dictionary Conversion**            | Convert dictionary keys, values or items to lists, sets, tuples                              | `d = {'a':1, 'b':2}`<br>`keys_list = list(d.keys())`<br>`values_set = set(d.values())`                                       |                                                                                 |      |
| **Dictionary with Lists**            | Store lists as values or create dictionary from lists                                        | `d = {'nums': [1,2,3]}`<br>`print(d['nums'])`<br>`keys = ['a','b']`<br>`values = [10, 20]`<br>`d2 = dict(zip(keys, values))` |                                                                                 |      |
| **Dictionary with String/Tuple/Set** | Use strings, tuples or sets as keys or values                                                | `d = {('x', 'y'): 1}`<br>`print(d[('x','y')])`<br>`d2 = {frozenset([1,2]): 'set_key'}`                                       |                                                                                 |      |
| **Merge Dictionaries**               | Combine dictionaries using `update()` or \`                                                  | \` operator (Python 3.9+)                                                                                                    | `d1 = {'a':1}`<br>`d2 = {'b':2}`<br>`d1.update(d2)`<br>`print(d1)`<br>\`d3 = d1 | d2\` |
| **Nested Dictionaries**              | Dictionaries inside dictionaries                                                             | `d = {'person': {'name': 'Alice', 'age': 25}}`<br>`print(d['person']['name'])`                                               |                                                                                 |      |
| **Check Key Existence**              | Use `in` operator                                                                            | `d = {'a':1}`<br>`if 'a' in d:`<br>   `print('Key exists')`                                                                  |                                                                                 |      |
| **Iterate Over Dictionary**          | Loop through keys, values, or items                                                          | `for k in d:`<br>   `print(k, d[k])`<br>`for k,v in d.items():`<br>   `print(k,v)`                                           |                                                                                 |      |
| **Copy Dictionary**                  | Copy dictionary with `copy()` or `dict()`                                                    | `d1 = {'a':1}`<br>`d2 = d1.copy()`<br>`print(d2)`                                                                            |                                                                                 |      |
| **Default Dictionary**               | Use `collections.defaultdict` to avoid key errors                                            | `from collections import defaultdict`<br>`dd = defaultdict(int)`<br>`dd['x'] += 1`<br>`print(dd)`                            |                                                                                 |      |

# Sets
| Topic                                    | Explanation                                                                                           | Example                                                                                                   |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **What is a Set?**                       | A set is an unordered collection of unique elements.                                                  | `python<br>my_set = {1, 2, 3}<br>print(my_set)  # Output: {1, 2, 3}`                                      |
| **Creating a Set**                       | Use `{}` with comma-separated values or `set()` function.                                             | `python<br>set1 = {1, 2, 3}<br>set2 = set([4, 5, 6])<br>print(set1)<br>print(set2)`                       |
| **Empty Set**                            | `{}` creates an empty dict, so use `set()` for empty set.                                             | `python<br>empty = set()<br>print(empty)  # Output: set()`                                                |
| **Adding Elements**                      | Use `.add()` method to add one element.                                                               | `python<br>s = {1, 2}<br>s.add(3)<br>print(s)  # Output: {1, 2, 3}`                                       |
| **Updating Set**                         | Use `.update()` to add multiple elements from iterable.                                               | `python<br>s = {1, 2}<br>s.update([3, 4])<br>print(s)  # Output: {1, 2, 3, 4}`                            |
| **Removing Elements**                    | `.remove(elem)` removes elem, raises error if not found.<br>`.discard(elem)` removes elem if present. | `python<br>s = {1, 2, 3}<br>s.remove(2)<br>print(s)  # {1, 3}<br>s.discard(4)<br>print(s)  # {1, 3}`      |
| **Set Operations: Union**                | Combines all unique elements from both sets.                                                          | `python<br>a = {1, 2}<br>b = {2, 3}<br>print(a.union(b))  # {1, 2, 3}`                                    |
| **Set Operations: Intersection**         | Elements common to both sets.                                                                         | `python<br>a = {1, 2, 3}<br>b = {2, 3, 4}<br>print(a.intersection(b))  # {2, 3}`                          |
| **Set Operations: Difference**           | Elements in first set but not in second.                                                              | `python<br>a = {1, 2, 3}<br>b = {2, 3}<br>print(a.difference(b))  # {1}`                                  |
| **Set Operations: Symmetric Difference** | Elements in either set but not both.                                                                  | `python<br>a = {1, 2, 3}<br>b = {2, 3, 4}<br>print(a.symmetric_difference(b))  # {1, 4}`                  |
| **Subset and Superset**                  | `.issubset()` checks if all elements of one set are in another.<br>`.issuperset()` is reverse.        | `python<br>a = {1, 2}<br>b = {1, 2, 3}<br>print(a.issubset(b))  # True<br>print(b.issuperset(a))  # True` |
| **Set Comprehension**                    | Create sets with comprehensions like lists.                                                           | `python<br>squares = {x*x for x in range(5)}<br>print(squares)  # {0, 1, 4, 9, 16}`                       |
| **Frozen Set**                           | Immutable version of set, cannot add or remove elements.                                              | `python<br>f = frozenset([1, 2, 3])<br>print(f)<br># f.add(4)  # Error`                                   |
| **Iterating Over Set**                   | Loop through elements in any order.                                                                   | `python<br>s = {1, 2, 3}<br>for elem in s:<br>    print(elem)`                                            |
| **Length of Set**                        | Use `len()` to get the number of elements.                                                            | `python<br>s = {1, 2, 3}<br>print(len(s))  # 3`                                                           |
| **Check Membership**                     | Use `in` keyword to check if element is in set.                                                       | `python<br>s = {1, 2, 3}<br>print(2 in s)  # True<br>print(5 in s)  # False`                              |

# Array

| Topic                                                | Explanation & Code Example                                                                                                                                              |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Declaring an Array in Python                         | Python has `array` module for typed arrays. Example: `import array as arr a = arr.array('i', [1, 2, 3]) print(a)`                                                       |
| Difference between Array and List in Python          | Arrays are typed, lists are heterogeneous and more flexible. Example: `import array as arr a = arr.array('i', [1,2]) l = [1, 'two', 3.0] print(type(a)) print(type(l))` |
| Python Array length                                  | Use `len()` function. Example: `import array as arr a = arr.array('i', [10,20,30]) print(len(a))`                                                                       |
| Numpy Arrays                                         | Powerful numeric arrays with more features. Example: `import numpy as np a = np.array([1,2,3]) print(a) print(type(a))`                                                 |
| Python Unpack Array                                  | Unpack elements to variables. Example: `import array as arr a = arr.array('i', [5,10,15]) x, y, z = a print(x) print(y) print(z)`                                       |
| Python remove Array item                             | Use `remove()` or `pop()`. Example: `import array as arr a = arr.array('i', [1,2,3,2]) a.remove(2) print(a) a.pop(1) print(a)`                                          |
| How to add element to Array in Python                | Use `append()` or `insert()`. Example: `import array as arr a = arr.array('i', [1,2,3]) a.append(4) print(a) a.insert(1, 5) print(a)`                                   |
| Find element in Array in Python                      | Use `in` keyword. Example: `import array as arr a = arr.array('i', [1,2,3]) print(2 in a) print(5 in a)`                                                                |
| Find Common elements in two Arrays in Python         | Convert to sets and intersect. Example: `import array as arr a = arr.array('i', [1,2,3]) b = arr.array('i', [2,3,4]) common = set(a).intersection(b) print(common)`     |
| How to pass an Array to a Function in Python         | Pass as parameter normally. Example: `import array as arr def print_array(ar): for i in ar: print(i) a = arr.array('i', [1,2,3]) print_array(a)`                        |
| How to create String Array in Python                 | Use lists for strings. Example: `str_array = ["apple", "banana", "cherry"] print(str_array)`                                                                            |
| Multidimensional Arrays                              | Use nested lists or numpy. Example numpy: `import numpy as np a = np.array([[1,2],[3,4]]) print(a)`                                                                     |
| Array Slicing                                        | Extract parts of array. Example: `import array as arr a = arr.array('i', [10,20,30,40]) print(a[1:3])`                                                                  |
| Array Iteration                                      | Loop over elements. Example: `import array as arr a = arr.array('i', [1,2,3]) for i in a: print(i)`                                                                     |
| Array Concatenation                                  | Combine arrays. Example: `import array as arr a = arr.array('i', [1,2]) b = arr.array('i', [3,4]) c = arr.array('i', a + b) print(c)`                                   |
| Array Sorting                                        | Sort elements in place. Example: `import array as arr a = arr.array('i', [3,1,2]) a = arr.array('i', sorted(a)) print(a)`                                               |
| Array Copying                                        | Use slicing or `copy` module. Example: `import array as arr import copy a = arr.array('i', [1,2,3]) b = a[:] c = copy.deepcopy(a)`                                      |
| Memory Usage of Arrays vs Lists                      | Arrays use less memory as they store homogeneous data, lists are flexible but use more memory (no direct code example).                                                 |
| Array Broadcasting (Numpy specific)                  | Numpy allows operations on different shapes. Example: `import numpy as np a = np.array([1,2,3]) b = 5 print(a + b)`                                                     |
| Array Reshaping (Numpy specific)                     | Change shape without changing data. Example: `import numpy as np a = np.array([1,2,3,4,5,6]) b = a.reshape(2,3) print(b)`                                               |
| Array Data Types and Typecodes (array module)        | `'i'` for int, `'f'` for float etc. Example: `import array as arr a = arr.array('f', [1.0, 2.0, 3.0]) print(a)`                                                         |
| Performance Comparison: Array vs List vs Numpy Array | Numpy arrays are fastest for numeric computations, arrays (`array` module) save memory vs lists but less flexible.                                                      |
| Using List Comprehensions to Create Arrays           | Create arrays/lists concisely. Example: `squares = [x*x for x in range(5)] print(squares)`                                                                              |
| Array Filtering                                      | Extract elements meeting condition. Example: `a = [1,2,3,4,5] filtered = [x for x in a if x > 2] print(filtered)`                                                       |
| Handling Empty Arrays                                | Initialize empty arrays. Example: `import array as arr a = arr.array('i', []) print(a)`                                                                                 |
| Error Handling with Arrays                           | Catch errors like `IndexError`. Example: `import array as arr a = arr.array('i', [1,2]) try: print(a[3]) except IndexError: print("Index out of range")`                |

# List Comprehension

| **Topic**                     | **Explanation**                                  | **Example**                                                                                                                                             |
| ----------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Basic Syntax**              | Short way to create a new list from an iterable. | numbers = \[1, 2, 3, 4, 5]<br>square = \[x \* x for x in numbers]<br>print(square)  # Output: \[1, 4, 9, 16, 25]                                        |
| **With Condition (if)**       | Include condition to filter elements.            | numbers = \[1, 2, 3, 4, 5]<br>even = \[x for x in numbers if x % 2 == 0]<br>print(even)  # Output: \[2, 4]                                              |
| **With if-else**              | Apply transformation based on condition.         | nums = \[1, 2, 3, 4, 5]<br>labels = \['Even' if x % 2 == 0 else 'Odd' for x in nums]<br>print(labels)  # Output: \['Odd', 'Even', 'Odd', 'Even', 'Odd'] |
| **Nested List Comprehension** | For 2D lists or matrix operations.               | matrix = \[\[1, 2], \[3, 4]]<br>flat = \[num for row in matrix for num in row]<br>print(flat)  # Output: \[1, 2, 3, 4]                                  |
| **Multiple if Conditions**    | Filter with multiple conditions.                 | nums = \[1, 2, 3, 4, 5, 6]<br>filtered = \[x for x in nums if x > 2 if x < 6]<br>print(filtered)  # Output: \[3, 4, 5]                                  |
| **Using Functions**           | Call functions inside list comprehension.        | def square(x):<br>  return x \* x<br>nums = \[1, 2, 3]<br>squares = \[square(n) for n in nums]<br>print(squares)  # Output: \[1, 4, 9]                  |
| **With Strings**              | List comprehension on strings.                   | text = "hello"<br>chars = \[c.upper() for c in text]<br>print(chars)  # Output: \['H', 'E', 'L', 'L', 'O']                                              |
| **Flatten Nested List**       | Useful for converting 2D to 1D.                  | nested = \[\[1, 2], \[3, 4], \[5, 6]]<br>flat = \[item for sublist in nested for item in sublist]<br>print(flat)  # Output: \[1, 2, 3, 4, 5, 6]         |
| **List of Tuples**            | Create tuples directly.                          | result = \[(x, x\*\*2) for x in range(5)]<br>print(result)  # Output: \[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]                                        |
| **Using enumerate()**         | Get index and value.                             | names = \['Alice', 'Bob']<br>indexed = \[f'{i}-{name}' for i, name in enumerate(names)]<br>print(indexed)  # Output: \['0-Alice', '1-Bob']              |
| **Set Comprehension**         | Same as list comp but with `{}`                  | nums = \[1, 2, 2, 3]<br>unique = {x for x in nums}<br>print(unique)  # Output: {1, 2, 3}                                                                |
| **Dict Comprehension**        | Create dictionaries using comprehension.         | keys = \['a', 'b']<br>vals = \[1, 2]<br>mydict = {k: v for k, v in zip(keys, vals)}<br>print(mydict)  # Output: {'a': 1, 'b': 2}                        |
| **Using range()**             | Common with numbers.                             | squares = \[x \* x for x in range(5)]<br>print(squares)  # Output: \[0, 1, 4, 9, 16]                                                                    |
| **With multiple loops**       | Use nested loops in one line.                    | pairs = \[(x, y) for x in \[1, 2] for y in \[3, 4]]<br>print(pairs)  # Output: \[(1, 3), (1, 4), (2, 3), (2, 4)]                                        |
| **Filter None or Empty**      | Clean up data.                                   | data = \['a', '', None, 'b']<br>cleaned = \[d for d in data if d]<br>print(cleaned)  # Output: \['a', 'b']                                              |
| **Conditional Replace**       | Replace specific values.                         | nums = \[0, 1, 2, 0, 3]<br>replaced = \[x if x != 0 else -1 for x in nums]<br>print(replaced)  # Output: \[-1, 1, 2, -1, 3]                             |

# Frozenset

| Topic                                         | Description                                                  | Example Code                                                                                   | Output                                             |
| --------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **1. Creating a frozenset**                   | Convert iterable (list, tuple, set, string) into a frozenset | `fs = frozenset([1, 2, 3, 2])`<br>`print(fs)`                                                  | `frozenset({1, 2, 3})`                             |
| **2. Empty frozenset**                        | Create an empty frozenset                                    | `empty_fs = frozenset()`<br>`print(empty_fs)`                                                  | `frozenset()`                                      |
| **3. From string**                            | Each character becomes an element                            | `fs = frozenset("abcabc")`<br>`print(fs)`                                                      | `frozenset({'c', 'a', 'b'})`                       |
| **4. Set vs Frozenset**                       | Set is mutable, frozenset is immutable                       | `s = set([1, 2])`<br>`fs = frozenset([1, 2])`<br>`s.add(3)`<br>`# fs.add(3)` ← Error           | `s = {1, 2, 3}`<br>`# AttributeError for fs.add()` |
| **5. Membership testing**                     | Check if item exists                                         | `fs = frozenset([1, 2, 3])`<br>`print(2 in fs)`<br>`print(5 in fs)`                            | `True`<br>`False`                                  |
| **6. Iterating**                              | Use a loop to access elements                                | `fs = frozenset([10, 20, 30])`<br>`for i in fs:`<br>`    print(i)`                             | `10`<br>`20`<br>`30` (order may vary)              |
| **7. Length**                                 | Use `len()` function                                         | `fs = frozenset([1, 2, 3])`<br>`print(len(fs))`                                                | `3`                                                |
| **8. Set operations - Union**                 | Combine elements                                             | `a = frozenset([1, 2])`<br>`b = frozenset([2, 3])`<br>`print(a.union(b))`                      | `frozenset({1, 2, 3})`                             |
| **9. Set operations - Intersection**          | Common elements                                              | `a = frozenset([1, 2, 3])`<br>`b = frozenset([2, 3, 4])`<br>`print(a.intersection(b))`         | `frozenset({2, 3})`                                |
| **10. Set operations - Difference**           | Items in one not in the other                                | `a = frozenset([1, 2, 3])`<br>`b = frozenset([3, 4])`<br>`print(a.difference(b))`              | `frozenset({1, 2})`                                |
| **11. Set operations - Symmetric Difference** | Items in either but not both                                 | `a = frozenset([1, 2, 3])`<br>`b = frozenset([2, 3, 4])`<br>`print(a.symmetric_difference(b))` | `frozenset({1, 4})`                                |
| **12. Subset check**                          | Check if A is subset of B                                    | `a = frozenset([1, 2])`<br>`b = frozenset([1, 2, 3])`<br>`print(a.issubset(b))`                | `True`                                             |
| **13. Superset check**                        | Check if A is superset of B                                  | `a = frozenset([1, 2, 3])`<br>`b = frozenset([2])`<br>`print(a.issuperset(b))`                 | `True`                                             |
| **14. Disjoint check**                        | No common elements                                           | `a = frozenset([1, 2])`<br>`b = frozenset([3, 4])`<br>`print(a.isdisjoint(b))`                 | `True`                                             |
| **15. Hashable nature**                       | Can be used as dict key                                      | `d = {frozenset([1, 2]): "value"}`<br>`print(d)`                                               | `{frozenset({1, 2}): 'value'}`                     |
| **16. Immutable proof**                       | Cannot modify                                                | `fs = frozenset([1, 2])`<br>`# fs.add(3)`<br>`# fs.remove(2)`                                  | `AttributeError` for both                          |
