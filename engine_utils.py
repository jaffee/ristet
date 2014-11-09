import time

def do_sleep(start, count, frame):
    sleep_until = frame*count + start
    try:
        time.sleep(sleep_until - time.time())
    except IOError:
        pass
