import time
import webbrowser


print("This program started on " + time.ctime())

total_breaks = 3
break_count = 0
while (break_count < total_breaks):
    time.sleep(10)  # 10 sec for testing purpouses. 2 hours would be 2*60*60.
    webbrowser.open("https://www.youtube.com/watch?v=tIdIqbv7SPo")
    break_count = break_count + 1
