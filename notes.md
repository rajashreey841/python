
# 🐍Python
## Preset
- Created by Guido van Rossum in 1990, Python 3 released in 2008
- Emphasizes readability and simplicity
- Official docs: [docs.python.org/3](https://docs.python.org/3)

## Table of Contents

- [Input and Output ](#input-and-output)
- [Variables, Assignment & Naming](#variables-assignment--naming)


## Input and Output 

This document summarizes all major types of input and output declarations in Python for quick reference.

### 📥 Input Methods

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

## 📤 Output Methods

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| Basic Print               | `print("Hello")`                                                                 |
| Print Variables           | `print("Name:", name)`                                                           |
| f-string Output           | `print(f"My name is {name}")`                                                    |
| Custom Separator          | `print("A", "B", sep="-")`                                                       |
| No Newline                | `print("Hello", end="")`                                                         |
| Format               | `print("{0} and Portal".format("Geeks"))`                                                         |


## 📂 File Input/Output

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| Read File                 | `with open("input.txt") as f: data = f.read()`                                   |
| Write to File             | `with open("file.txt", "w") as f: f.write("text")`                               |
| Append to File            | `with open("file.txt", "a") as f: f.write("more")`                               |
| Read Line by Line         | `for line in open("file.txt"):`                                                  |

## 🔄 Loop Input

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| Loop Input List           | `nums = []\\nfor _ in range(n): nums.append(int(input()))`                       |
| Loop 2D Matrix Input      | `for i in range(rows):\\n row = list(map(int, input().split()))\\n matrix.append(row)` |

## ⚡ List Comprehension

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| List of Ints              | `[int(x) for x in input().split()]`                                              |
| 2D Matrix Input           | `[list(map(int, input().split())) for _ in range(rows)]`                         |
| List of Squares           | `[x**2 for x in nums]`                                                           |
| Conditional List          | `[x for x in nums if x % 2 == 0]`                                                |

## 🛡️ Error Handling

| Type                       | Syntax / Example                                                                 |
|---------------------------|-----------------------------------------------------------------------------------|
| Try/Except Input          | `try: val = int(input())\\nexcept ValueError: print("Invalid input")

# variables

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
| Assign Function to Variable         | Functions can be assigned to variables              | `say_hello = greet`                               |


