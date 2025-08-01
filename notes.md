
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
