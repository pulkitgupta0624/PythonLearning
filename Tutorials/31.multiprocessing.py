'''
Multiprocessing means:
- Running multiple processes (programs) at the same time.
- Each process has its own memory space.
- It runs truly in parallel on multiple CPU cores.
'''

import multiprocessing
import time

def worker(name):
    print(f"Worker {name}: Starting")
    time.sleep(2)  # Simulate a time-consuming task
    print(f"Worker {name}: Finished")

# if __name__ == '__main__':
#     # Create processes
#     process1 = multiprocessing.Process(target=worker, args=('A',))
#     process2 = multiprocessing.Process(target=worker, args=('B',))

#     # Start processes
#     process1.start()
#     process2.start()

#     # Wait for both processes to complete
#     process1.join()
#     process2.join()
#     print("Finished all workers.")

# Demonstrating multiple processes
def multiple_workers():
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=worker, args=(f'Process-{i}',))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    print("All multiple workers finished.")

if __name__ == '__main__':
    multiple_workers()
