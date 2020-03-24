import time


class StopWatch:
    def __init__(self):
        self.start_time = time.time() # record the first timestamp
        self.end_time = -1

    def start(self):
        self.start_time = time.time()
        self.end_time = -1

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        self.end_time -= self.start_time
        # boundary case? never started
        # 1. end_time = -1 never stopped
        # 2. start stop start: endtime! = 0
        if self.end_time < 0:
            return None
        return round(self.end_time, 1)


sw = StopWatch ()
time.sleep (0.1)
sw.stop()
print(sw.elapsed_time())
sw.start()
time.sleep(0.2)
print(sw.elapsed_time())
sw.stop()
print(sw.elapsed_time())