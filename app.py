import time
from datetime import datetime as date

win_path = "C:\\Windows\\System32\\drivers\\etc"
other_path = "/etc"
redirect = "127.0.0.1"

block_url = ["www.linkedin.com", "linkedin.com",
             "www.youtube.com", "youtube.com"]

while True:
    start_time = date(date.now().year, date.now().month, date.now().day, 8)
    current_time = date.now()
    end_time = date(date.now().year, date.now().month, date.now().day, 16)
    if start_time < current_time < end_time:
        print("Radno vreme")
    else:
        print("Vreme odmora")
    time.sleep(5)
