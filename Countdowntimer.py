#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

class CountdownTimer:
    
    def __init__(self, duration):
        self.duration = duration
        self.paused = False
        self.started = False
        self.reset()
        
    def reset(self):
        self.start_time = time.time()
        self.remaining_time = self.duration
        self.paused = False
        self.started = False
        
    def start(self):
        self.started = True
        while self.remaining_time > 0 and not self.paused:
            self.remaining_time = self.duration - (time.time() - self.start_time)
            mins, secs = divmod(self.remaining_time, 60)
            time_format = '{:02d}:{:02d}'.format(int(mins), int(secs))
            print("Time remaining:", time_format, end='\r')
            time.sleep(1)
            
    def pause(self):
        if self.started and not self.paused:
            self.remaining_time = self.duration - (time.time() - self.start_time)
            self.paused = True
            
    def resume(self):
        if self.paused:
            self.start_time = time.time() - (self.duration - self.remaining_time)
            self.paused = False
            self.start()
            
    def stop(self):
        self.remaining_time = 0
        self.paused = False
        
timer = CountdownTimer(120) # Set duration of 2 minutes
timer.start()

while timer.remaining_time > 0:
    command = input("\nEnter 'r' to reset, 'p' to pause, 'c' to continue, or 's' to stop: ")
    if command == 'r':
        timer.reset()
        timer.start()
    elif command == 'p':
        timer.pause()
    elif command == 'c':
        timer.resume()
    elif command == 's':
        timer.stop()
        break
print("\nTimer stopped.")


# In[ ]:




