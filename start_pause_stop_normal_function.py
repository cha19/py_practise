
from time import sleep


class Task:
    def __init__(self):
        self.status=None
        self.count=None
    
    def start(self):
        if self.count==None:
            a=range(0,100)
        else:
            a=range(self.count,100)
        for i in a:
            print(i)
            sleep(1)
            if self.status=='pause':
                self.count=i
                while True:
                    if self.status=='pause':
                        pass
                    elif self.status=='resume':
                        self.count-=1
                        break
                    elif self.status=='stop':
                        break
            elif self.status=='stop':
                break
        print('The end')
    def pause(self):
        self.status='pause'
    def resume(self):
        self.status='resume'
    def stop(self):
        self.status='stop'
if __name__=='__main__':
    t=Task()
    t.start()

print("done")