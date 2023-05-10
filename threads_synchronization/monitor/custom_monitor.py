from threads_synchronization.monitor.monitor import Monitor, Condition
from threads_synchronization.utils import generate_even_number, generate_odd_number
from threads_synchronization.buffer import FIFO
from threading import Event, Thread
import time
from typing import Dict


class CustomMonitor(Monitor):
    def __init__(self, buffer: FIFO, conditions: Dict[str, Condition]):
        super().__init__()
        self.buffer = buffer
        self.conditions = conditions
        self.gen_even_waiting = 0
        self.gen_odd_waiting = 0
        self.cons_even_waiting = 0
        self.cons_odd_waiting = 0

    def a1_condition(self):
        if self.buffer.even_values < 10:
            return True
        else:
            return False

    def a2_condition(self):
        if self.buffer.even_values > self.buffer.odd_values:
            return True
        else:
            return False

    def b1_condition(self):
        if len(self.buffer) >= 3:
            return True
        else:
            return False

    def b2_condition(self):
        if len(self.buffer) >= 7:
            return True
        else:
            return False

    def put_even_number(self, number: int):
        self.enter()
        if not self.a1_condition():
            self.gen_even_waiting += 1
            self.wait(self.conditions["gen_even"])
            self.gen_even_waiting -= 1
        self.buffer.put(number=number)
        print(f"A1: {self.buffer}")
        if self.a2_condition() and self.gen_odd_waiting:
            self.signal(self.conditions["gen_odd"])
        elif self.b1_condition() and self.cons_even_waiting:
            self.signal((self.conditions["cons_even"]))
        elif self.b2_condition() and self.cons_odd_waiting:
            self.signal(self.conditions["cons_odd"])
        else:
            self.leave()

    def put_odd_number(self, number: int):
        self.enter()
        if not self.a2_condition():
            self.gen_odd_waiting += 1
            self.wait(self.conditions["gen_odd"])
            self.gen_odd_waiting -= 1
        self.buffer.put(number=number)
        print(f"A2: {self.buffer}")
        if self.a1_condition() and self.gen_even_waiting:
            self.signal(self.conditions["gen_even"])
        elif self.b1_condition() and self.cons_even_waiting:
            self.signal((self.conditions["cons_even"]))
        elif self.b2_condition() and self.cons_odd_waiting:
            self.signal(self.conditions["cons_odd"])
        else:
            self.leave()

    def get_even_number(self):
        self.enter()
        if not self.b1_condition():
            self.cons_even_waiting += 1
            self.wait(self.conditions["cons_even"])
            self.cons_even_waiting -= 1
        self.buffer.get_even()
        print(f"B1: {self.buffer}")
        if self.a1_condition() and self.gen_even_waiting:
            self.signal((self.conditions["gen_even"]))
        elif self.a2_condition() and self.gen_odd_waiting:
            self.signal(self.conditions["gen_odd"])
        elif self.b2_condition() and self.cons_odd_waiting:
            self.signal(self.conditions["cons_odd"])
        else:
            self.leave()

    def get_odd_number(self):
        self.enter()
        if not self.b2_condition():
            self.cons_odd_waiting += 1
            self.wait(self.conditions["cons_odd"])
            self.cons_odd_waiting -= 1
        self.buffer.get_odd()
        print(f"B2: {self.buffer}")
        if self.a1_condition() and self.gen_even_waiting:
            self.signal((self.conditions["gen_even"]))
        elif self.a2_condition() and self.gen_odd_waiting:
            self.signal(self.conditions["gen_odd"])
        elif self.b1_condition() and self.cons_even_waiting:
            self.signal((self.conditions["cons_even"]))
        else:
            self.leave()


def a1_loop(custom_monitor: CustomMonitor, stop_event: Event):
    while not stop_event.is_set():
        num = generate_even_number()
        custom_monitor.put_even_number(number=num)
        time.sleep(0.1)


def a2_loop(custom_monitor: CustomMonitor, stop_event: Event):
    while not stop_event.is_set():
        num = generate_odd_number()
        custom_monitor.put_odd_number(number=num)
        # time.sleep(random.uniform(0, 0.2))
        time.sleep(0.1)


def b1_loop(custom_monitor: CustomMonitor, stop_event: Event):
    while not stop_event.is_set():
        custom_monitor.get_even_number()
        # time.sleep(random.uniform(0, 0.2))
        time.sleep(0.1)


def b2_loop(custom_monitor: CustomMonitor, stop_event: Event):
    while not stop_event.is_set():
        custom_monitor.get_odd_number()
        # time.sleep(random.uniform(0, 0.2))
        time.sleep(0.1)


def pipeline(buffer_fifo: FIFO, a1=True, a2=True, b1=True, b2=True, working_time=3):
    condition_dict = {
        "gen_even": Condition(),
        "gen_odd": Condition(),
        "cons_even": Condition(),
        "cons_odd": Condition()
    }
    print(f"Init buffer: {buffer_fifo}")
    custom_monitor = CustomMonitor(buffer_fifo, condition_dict)
    events_list, threads_lists, workers = [], [], []
    if a1:
        print("Working a1 process")
        events_list.append(Event())
        threads_lists.append(a1_loop)
    if a2:
        print("Working a2 process")
        events_list.append(Event())
        threads_lists.append(a2_loop)
    if b1:
        print("Working b1 process")
        events_list.append(Event())
        threads_lists.append(b1_loop)
    if b2:
        print("Working b2 process")
        events_list.append(Event())
        threads_lists.append(b2_loop)
    for loop, event in zip(threads_lists, events_list):
        workers.append(Thread(target=loop, args=(custom_monitor, event)))
    for worker in workers:
        worker.start()
    time.sleep(working_time)
    for event in events_list:
        event.set()
    for worker in workers:
        worker.join()


def main(init_values=None):
    buffer_fifo = FIFO(init_values=init_values)
    pipeline(buffer_fifo)


if __name__ == "__main__":
    main()


