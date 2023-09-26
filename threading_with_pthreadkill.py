import threading
import time,signal

# event_exit=threading.Event()

def runner1():
    for i in range(0,15):
        print(i)
        time.sleep(1)
        # if event_exit.is_set():
        #     break
    
# signal.pause()
# signal.pthread_kill(s1.nati)

# def signal_event(signum,frame):
#     event_exit.set()
# signal.signal(signal.SIGINT,signal_event)
s1=threading.Thread(target=runner1)
s1.start()
time.sleep(5)
s1.kill()
# signal.pthread_kill(threading.get_ident(),1)

print("Done")