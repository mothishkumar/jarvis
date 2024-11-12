# Functions/greeting.py

from datetime import datetime

def greet():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning sir!"
    elif 12 <= current_hour < 18:
        return "Good afternoon sir!"
    elif 18 <= current_hour < 22:
        return "Good evening sir!"
    else:
        return "Good night sir!"
