import time

max_tries = 5
current_try = 0
sleep_time = 1

while current_try < max_tries:
    print("Current try:",current_try + 1," sleep-time: ", sleep_time)
    time.sleep(sleep_time)
    sleep_time *= 2
    current_try += 1