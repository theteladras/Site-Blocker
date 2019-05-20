import time
from datetime import datetime as date

win_path = "C:\\Windows\\System32\\drivers\\etc"
other_path = "/etc"
test_path = "hosts"
redirect = "127.0.0.1"

block_url = ["www.linkedin.com", "linkedin.com",
             "www.youtube.com", "youtube.com"]

itteration_num = 0
while True:
    start_time = date(date.now().year, date.now().month, date.now().day, 9)
    current_time = date.now()
    end_time = date(date.now().year, date.now().month, date.now().day, 17)
    if start_time < current_time < end_time:
        print("Radno vreme")
        if itteration_num == 0:
            itteration_num = 1
            with open(test_path, 'r+') as file:
                content = file.read()
                print(content)
                for index, uri in enumerate(block_url):
                    if uri not in content:
                        if index == 0:
                            file.write("\n" + redirect + " " + uri + "\n")
                        else:
                            file.write(redirect + " " + uri + "\n")
                        print("added to the block list: ", uri)
    else:
        print("Vreme odmora")
    time.sleep(10)
