# Python - Async

![img](https://realpython.com/cdn-cgi/image/width=1920,format=auto/https://files.realpython.com/media/Understanding-Asynchronous-Programming-in-Python_Watermarked.4b590c7c03ea.jpg)

## Description
asyncio is a library to write `concurrent` code using the `async/await` syntax.
asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
asyncio is often a perfect fit for IO-bound and high-level `structured` network code.

## Resources
### Read or Watch:
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

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

### 0. The basics of async
Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.

Use the `random` module.
- File: [`0-basic_async_syntax.py`](https://github.com/ali-jin/holbertonschool-web_back_end/blob/main/python_async_function/0-basic_async_syntax.py)

-------------------------
### 1. Let's execute multiple coroutines at the same time with async
Import `wait_random` from the previous python file that you’ve written and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified max_delay.

`wait_n` should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.
- File: [`1-concurrent_coroutines.py`](https://github.com/ali-jin/holbertonschool-web_back_end/blob/main/python_async_function/1-concurrent_coroutines.py)

-------------------------
### 2. Measure the runtime
From the previous file, import `wait_n` into `2-measure_runtime.py`.

Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a float.

Use the `time` module to measure an approximate elapsed time.
- File: [`2-measure_runtime.py`](https://github.com/ali-jin/holbertonschool-web_back_end/blob/main/python_async_function/2-measure_runtime.py)

-------------------------
### 3. Tasks
Import `wait_random` from `0-basic_async_syntax`.

Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`.
- File: [`3-tasks.py`](https://github.com/ali-jin/holbertonschool-web_back_end/blob/main/python_async_function/3-tasks.py)

-------------------------
### 4. Tasks
Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.
- File: [`4-tasks.py`](https://github.com/ali-jin/holbertonschool-web_back_end/blob/main/python_async_function/4-tasks.py)
