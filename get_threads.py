from concurrent.futures import thread
import threading
import time,signal

event_exit=threading.Event()

def runner1():
    for i in range(0,100):
        print(i)
        time.sleep(1)
        if event_exit.is_set():
            break
    

# def runner2():
#     for j in range(400,600):
#         print("      "+str(j))
#         time.sleep(0.5)
def signal_event(signum,frame):
    event_exit.set()
signal.signal(signal.SIGINT,signal_event)
s1=threading.Thread(target=runner1)
s1.start()

# s1._is_stopped=True
# time.sleep(6)
# s1._is_stopped=False
# s1._stop.set()
# print(s1.is_alive())
# s2=threading.Thread(target=runner2)
# s2.start()