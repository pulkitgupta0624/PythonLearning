"""
Create a python program capable of greeting you with good morning, good afternoon
and good evening. Your program should use time module to get current hour.
"""

import time

# Get current hour (0-23)
current_hour = int(time.strftime("%H"))

if current_hour < 12:
    print("Good Morning 🌞")
elif current_hour < 17:
    print("Good Afternoon 🌤️")
else:
    print("Good Evening 🌙")
