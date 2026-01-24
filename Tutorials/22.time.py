import time

current_time = time.time()
print("Current Time in seconds since Epoch:", current_time)

# print("starting a timer for 3 seconds...")
# time.sleep(3)
# print("Timer ended after 3 seconds.")

print("Getting local time...")
local_time = time.localtime()
print("Local Time:", local_time)

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted Local Time:", formatted_time)

