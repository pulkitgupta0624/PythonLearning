'''
Normal (synchronous) code:
Python runs one line at a time, waiting for each operation to complete before moving to the next.

Asynchronous code with asyncIO:
- pause a task when it is wating (sleep, network, I/O operations).
- do other tasks in that waiting time.
- all in one thread
'''

import asyncio

# async def main():
#     print("Task 1: Starting")
#     await asyncio.sleep(2)  # Simulate a long-running operation
#     print("Task 1: Completed after 2 seconds")

#     print("Task 2: Starting")
#     await asyncio.sleep(1)  # Simulate another long-running operation
#     print("Task 2: Completed after 1 second")

# # Run the main async function
# asyncio.run(main())

# Demonstrating concurrent tasks with asyncIO
async def task(name, duration):
    print(f"{name}: Starting")
    await asyncio.sleep(duration)
    print(f"{name}: Completed after {duration} seconds")    

async def main_concurrent():
    await asyncio.gather(
        task("Task A", 2),
        task("Task B", 1),
        task("Task C", 3)
    )
# Run the concurrent tasks
asyncio.run(main_concurrent())
