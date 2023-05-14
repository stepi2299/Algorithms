from threads_synchronization.monitor.custom_monitor import pipeline
from threads_synchronization.buffer import FIFO


fifo_empty = FIFO()

fifo_even = FIFO([2, 4, 6, 8, 12])

fifo_odd = FIFO([1, 3, 5, 7, 9, 13, 15, 17, 19])

fifo_mix = FIFO([1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 15, 17, 8])

fifo_more_even = FIFO([2, 5, 4, 6, 11, 8, 12])


def a1_test(fifo_empty):
    pipeline(fifo_empty, a1=True, a2=False, b1=False, b2=False)


def a2_empty_test(fifo_empty):
    pipeline(fifo_empty, a1=False, a2=True, b1=False, b2=False)


def a2_more_even_test(fifo_more_even):
    pipeline(fifo_more_even, a1=False, a2=True, b1=False, b2=False)


def a2_more_odd_test(fifo_mix):
    pipeline(fifo_mix, a1=False, a2=True, b1=False, b2=False)


def b1_empty_test(fifo_empty):
    pipeline(fifo_empty, a1=False, a2=False, b1=True, b2=False)
    # assert len(fifo_empty) == 0


def b1_even_test(fifo_even):
    pipeline(fifo_even, a1=False, a2=False, b1=True, b2=False)
    # assert len(fifo_even) == 2


def b1_odd_test(fifo_odd):
    len_fifo = len(fifo_odd)
    pipeline(fifo_odd, a1=False, a2=False, b1=True, b2=False)
    # assert len(fifo_odd) == len_fifo


def b2_empty_test(fifo_empty):
    pipeline(fifo_empty, a1=False, a2=False, b1=False, b2=True)
    # assert len(fifo_empty) == 0


def b2_even_test(fifo_even):
    old = len(fifo_even)
    pipeline(fifo_even, a1=False, a2=False, b1=False, b2=True)
    # assert len(fifo_even) == old


def b2_odd_test(fifo_odd):
    pipeline(fifo_odd, a1=False, a2=False, b1=False, b2=True)
    # assert len(fifo_odd) == 6


def a1_a2_empty_test(fifo_empty):
    pipeline(fifo_empty, a1=True, a2=True, b1=False, b2=False)
    # assert len(fifo_empty) == 20 or len(fifo_empty) == 21


def b1_b2_empty_test(fifo_empty):
    pipeline(fifo_empty, a1=False, a2=False, b1=True, b2=True)
    # assert len(fifo_empty) == 0


def b1_b2_mix_test(fifo_more_even):
    pipeline(fifo_more_even, a1=False, a2=False, b1=True, b2=True)
    # assert len(fifo_more_even) == 2
    # assert fifo_more_even.even_values == 0
    # assert fifo_more_even.odd_values == 2


def b1_b2_odd_test(fifo_odd):
    pipeline(fifo_odd, a1=False, a2=False, b1=True, b2=True)
    # assert len(fifo_odd) == 6
    # assert fifo_odd.odd_values == 6


def a1_b1_test(fifo_empty):
    pipeline(fifo_empty, a1=True, a2=False, b1=True, b2=False)
    # assert len(fifo_empty) == fifo_empty.even_values
    # assert fifo_empty.even_values == 3 or fifo_empty.even_values == 2
    # assert fifo_empty.odd_values == 0


def all_test(fifo_empty):
    pipeline(fifo_empty)
    # assert len(fifo_empty) > 2
    # assert fifo_empty.odd_values >= fifo_empty.even_values


a1_a2_empty_test(fifo_empty)
