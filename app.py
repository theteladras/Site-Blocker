import time
from datetime import datetime as date
import services


win_path = "C:\\Windows\\System32\\drivers\\etc"
other_path = "/etc"
test_path = "hosts"
work_begin_h = 9
work_end_h = 17
start_time = date(date.now().year, date.now().month,
                  date.now().day, work_begin_h)
end_time = date(date.now().year, date.now().month,
                date.now().day, work_end_h)
if services.hourCheck(start_time, end_time):
    redirect = services.initial_setup()

block_url = [
    "www.twitter.com", "twitter.com",
    "www.youtube.com", "youtube.com",
    "www.facebook.com", "facebook.com",
    "www.instagram.com", "instagram.com"
]

print_once_switch = services.hourCheck(start_time, end_time)
while True:
    if services.hourCheck(start_time, end_time):
        print("\nRadno vreme...\n")
        if print_once_switch:
            print_once_switch = False
            with open(test_path, 'r+') as file:
                content = file.read()
                print(content)
                for index, uri in enumerate(block_url):
                    if uri not in content:
                        if index == 0:
                            flag = file.write(
                                "\n" + redirect + " " + uri + "\n")
                        else:
                            file.write(redirect + " " + uri + "\n")
                        print("Added to the block list: ", uri)
    else:
        print("\nSada si slobodan!\n")
        if not print_once_switch:
            print_once_switch = True
            with open(test_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in block_url):
                        file.write(line)
                file.truncate()
    time.sleep(10)
