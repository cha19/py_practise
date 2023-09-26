import threading
import time,signal

event_exit=threading.Event()

def runner1():
    for i in range(0,50):
        print(i)
        time.sleep(1)
        if event_exit.is_set():
            break
    
signal.pause()

def signal_event(signum,frame):
    event_exit.set()
signal.signal(signal.SIGINT,signal_event)
s1=threading.Thread(target=runner1)
s1.start()
