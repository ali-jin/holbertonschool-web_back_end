# Python - Async Comprehension

![img](https://miro.medium.com/v2/resize:fit:1244/format:webp/1*hhLSOv3kdBfEBn5OC6fAGg.png)

## Description
Asynchronous Comprehensions in Python is a feature that allows you to use the await keyword inside list, set, dictionary, and generator comprehensions.
Asynchronous comprehensions are a way to work with asynchronous sequences efficiently. They allow you to perform asynchronous operations on each item of a sequence and collect the results in a new sequence.

## Resources
### Read or Watch:
- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

-------------------------
## Tasks

### 0. Async Generator
Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.
- File: [`0-async_generator.py`](https://github.com/ali-jin/holbertonschool-web_back_end/blob/main/python_async_comprehension/0-async_generator.py)

-------------------------
### 1. Async Comprehensions
Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.
- File: [`1-async_comprehension.py`](https://github.com/ali-jin/holbertonschool-web_back_end/blob/main/python_async_comprehension/1-async_comprehension.py)

-------------------------
### 2. Run time for four parallel comprehensions
Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
- File: [`2-measure_runtime.py`](https://github.com/ali-jin/holbertonschool-web_back_end/blob/main/python_async_comprehension/2-measure_runtime.py)
