'''
Multithreading means running multiple threads (tasks) at the same time within a single program.

Multithreading is useful when:
- your program waits a lot (I/O operations, network requests, file reading/writing).
- tasks are independent of each other.
- you want better responsiveness in GUI applications.
'''

import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Simulate a time-consuming task

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulate a time-consuming task

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()
print("Finished printing numbers and letters.")
