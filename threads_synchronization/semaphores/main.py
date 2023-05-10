import time
from threads_synchronization.buffer import FIFO
from threading import Semaphore, Thread, Event
from threads_synchronization.utils import generate_even_number, generate_odd_number

gen_even_waiting = 0
gen_odd_waiting = 0
cons_even_waiting = 0
cons_odd_waiting = 0


def a1_condition(queue: FIFO):
    if queue.even_values < 10:
        return True
    else:
        return False


def a2_condition(queue: FIFO):
    if queue.even_values > queue.odd_values:
        return True
    else:
        return False


def b1_condition(queue: FIFO):
    if len(queue) >= 3:
        return True
    else:
        return False


def b2_condition(queue: FIFO):
    if len(queue) >= 7:
        return True
    else:
        return False


def put_even_number(queue: FIFO, number: int, semaphores) -> None:
    global gen_even_waiting
    global gen_odd_waiting
    global cons_even_waiting
    global cons_odd_waiting
    allow = True

    semaphores["global"].acquire()
    if not a1_condition(queue):
        gen_even_waiting += 1
        semaphores["global"].release()
        allow = semaphores["gen_even"].acquire(timeout=2)
        gen_even_waiting -= 1
    if allow:
        queue.put(number)
    if gen_odd_waiting > 0 and a2_condition(queue):
        semaphores["gen_odd"].release()
    elif cons_even_waiting > 0 and b1_condition(queue):
        semaphores["cons_even"].release()
    elif cons_odd_waiting > 0 and b2_condition(queue):
        semaphores["cons_odd"].release()
    else:
        semaphores["global"].release()


def put_odd_number(queue: FIFO, number: int, semaphores) -> None:
    global gen_even_waiting
    global gen_odd_waiting
    global cons_even_waiting
    global cons_odd_waiting
    allow = True

    semaphores["global"].acquire()
    if not a2_condition(queue):
        gen_odd_waiting += 1
        semaphores["global"].release()
        allow = semaphores["gen_odd"].acquire(timeout=2)
        gen_odd_waiting -= 1
    if allow:
        queue.put(number)
    if gen_even_waiting > 0 and a1_condition(queue):
        semaphores["gen_even"].release()
    elif cons_even_waiting > 0 and b1_condition(queue):
        semaphores["cons_even"].release()
    elif cons_odd_waiting > 0 and b2_condition(queue):
        semaphores["cons_odd"].release()
    else:
        semaphores["global"].release()


def get_even_number(queue: FIFO, semaphores) -> None:
    global gen_even_waiting
    global gen_odd_waiting
    global cons_even_waiting
    global cons_odd_waiting

    allow = True

    semaphores["global"].acquire()
    if not b1_condition(queue):
        cons_even_waiting += 1
        semaphores["global"].release()
        allow = semaphores["cons_even"].acquire(timeout=2)
        cons_even_waiting -= 1
    if allow:
        queue.get_even()
    if gen_even_waiting > 0 and a1_condition(queue):
        semaphores["gen_even"].release()
    elif gen_odd_waiting > 0 and a2_condition(queue):
        semaphores["gen_odd"].release()
    elif cons_odd_waiting > 0 and b2_condition(queue):
        semaphores["cons_odd"].release()
    else:
        semaphores["global"].release()


def get_odd_number(queue: FIFO, semaphores) -> None:
    global gen_even_waiting
    global gen_odd_waiting
    global cons_even_waiting
    global cons_odd_waiting

    allow = True

    semaphores["global"].acquire()
    if not b2_condition(queue):
        cons_odd_waiting += 1
        semaphores["global"].release()
        allow = semaphores["cons_odd"].acquire(timeout=2)
        cons_odd_waiting -= 1
    if allow:
        queue.get_odd()
    if gen_even_waiting > 0 and a1_condition(queue):
        semaphores["gen_even"].release()
    elif gen_odd_waiting > 0 and a2_condition(queue):
        semaphores["gen_odd"].release()
    elif cons_even_waiting > 0 and b1_condition(queue):
        semaphores["cons_even"].release()
    else:
        semaphores["global"].release()


def a1_loop(queue: FIFO, semaphores: dict, stop_event: Event):
    while not stop_event.is_set():
        num = generate_even_number()
        put_even_number(queue, num, semaphores)
        # time.sleep(random.uniform(0, 0.2))
        time.sleep(0.1)


def a2_loop(queue: FIFO, semaphores: dict, stop_event: Event):
    while not stop_event.is_set():
        num = generate_odd_number()
        put_odd_number(queue, num, semaphores)
        # time.sleep(random.uniform(0, 0.2))
        time.sleep(0.1)


def b1_loop(queue: FIFO, semaphores: dict, stop_event: Event):
    while not stop_event.is_set():
        get_even_number(queue, semaphores)
        # time.sleep(random.uniform(0, 0.2))
        time.sleep(0.1)


def b2_loop(queue: FIFO, semaphores: dict, stop_event: Event):
    while not stop_event.is_set():
        get_odd_number(queue, semaphores)
        # time.sleep(random.uniform(0, 0.2))
        time.sleep(0.1)



semaphores_dict = {
    "global": Semaphore(1),
    "gen_even": Semaphore(0),
    "gen_odd": Semaphore(0),
    "cons_even": Semaphore(0),
    "cons_odd": Semaphore(0)
            }


def pipeline(buffer_fifo, a1=True, a2=True, b1=True, b2=True, working_time=3):
    events_list, threads_lists, workers = [], [], []
    if a1:
        events_list.append(Event())
        threads_lists.append(a1_loop)
    if a2:
        events_list.append(Event())
        threads_lists.append(a2_loop)
    if b1:
        events_list.append(Event())
        threads_lists.append(b1_loop)
    if b2:
        events_list.append(Event())
        threads_lists.append(b2_loop)
    for loop, event in zip(threads_lists, events_list):
        workers.append(Thread(target=loop, args=(buffer_fifo, semaphores_dict, event)))
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

