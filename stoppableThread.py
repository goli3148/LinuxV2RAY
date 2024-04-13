import threading
import time

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

def a(args):
    while True:
        time.sleep(1)
        print(f"running:{args}")

# th = StoppableThread(target=a)
# th.start()
# time.sleep(5)
# th._stop()
# th.stopped()

import multiprocessing
proc = multiprocessing.Process(target=a, args=(1,))
proc.start()
time.sleep(3)
# Terminate the process
proc.terminate() 