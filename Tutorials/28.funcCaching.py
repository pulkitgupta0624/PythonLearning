'''
Function caching means:
- Store the resut of function call, so next time same input comes, python doesn't recompute it.
- Instead it returns the stored result.

Some functions are:
- slow
- computationally expensive (loops, recursions, complex calculations etc.)
- called again and again with same inputs.
'''

## Without caching
import time
def slow_function(n):
    time.sleep(2)  # Simulate a slow computation
    return n * n

start_time = time.time()
print(slow_function(5))  # First call, takes time
print("Time taken (1st call):", time.time() - start_time)
start_time = time.time()
print(slow_function(5))  # Second call, takes time again
print("Time taken (2nd call):", time.time() - start_time)

# With caching using functools.lru_cache
from functools import lru_cache
@lru_cache(maxsize=None)
def cached_slow_function(n):
    time.sleep(2)  # Simulate a slow computation
    return n * n

start_time = time.time()
print(cached_slow_function(5))  # First call, takes time
print("Time taken (1st call with caching):", time.time() - start_time)
start_time = time.time()
print(cached_slow_function(5))  # Second call, returns instantly
print("Time taken (2nd call with caching):", time.time() - start_time)

