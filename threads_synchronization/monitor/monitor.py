from threading import Semaphore


class Condition:
    def __init__(self):
        self.w = Semaphore(0)
        self.waiting_count = 0

    def wait(self):
        self.w.acquire()

    def signal(self) -> bool:
        if self.waiting_count > 0:
            self.waiting_count -= 1
            self.w.release()
            return True
        else:
            return False


class Monitor:
    def __init__(self):
        self.s = Semaphore(1)

    def enter(self):
        self.s.acquire()

    def leave(self):
        self.s.release()

    def wait(self, cond: Condition):
        cond.waiting_count += 1
        self.leave()
        cond.wait()

    def signal(self, cond: Condition):
        if cond.signal():
            self.enter()
