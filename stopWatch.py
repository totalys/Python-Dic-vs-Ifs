import time
#Thanks to Morgan Thrapp
class StopWatch:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0

    def start(self):
        self.start_time = time.time()
        return self.start_time

    def stop(self):
        self.stop_time = time.time()
        return self.stop_time

    def elapsed(self):
        print(str(self.stop_time - self.start_time))
