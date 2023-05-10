from threads_synchronization.semaphores.main import pipeline
from threads_synchronization.buffer import FIFO
import pytest


@pytest.fixture(name="fifo_empty")
def fixture_fifo_empty():
    return FIFO()


@pytest.fixture(name="fifo_even")
def fixture_fifo_even():
    return FIFO([2, 4, 6, 8, 12])


@pytest.fixture(name="fifo_odd")
def fixture_fifo_odd():
    return FIFO([1, 3, 5, 7, 9, 13, 15, 17, 19])


@pytest.fixture(name="fifo_mix")
def fixture_fifo_mix():
    return FIFO([1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 15, 17, 8])


@pytest.fixture(name="fifo_more_even")
def fixture_fifo_more_even():
    return FIFO([2, 5, 4, 6, 11, 8, 12])


def test_a1(fifo_empty):
    pipeline(fifo_empty, a1=True, a2=False, b1=False, b2=False)
    assert len(fifo_empty) == 10


def test_a2_empty(fifo_empty):
    pipeline(fifo_empty, a1=False, a2=True, b1=False, b2=False)
    assert len(fifo_empty) == 0


def test_a2_more_even(fifo_more_even):
    pipeline(fifo_more_even, a1=False, a2=True, b1=False, b2=False)
    assert len(fifo_more_even) == 10
    assert fifo_more_even.even_values == fifo_more_even.odd_values


def test_a2_more_odd(fifo_mix):
    pipeline(fifo_mix, a1=False, a2=True, b1=False, b2=False)
    assert len(fifo_mix) == 13
    assert fifo_mix.even_values < fifo_mix.odd_values


def test_b1_empty(fifo_empty):
    pipeline(fifo_empty, a1=False, a2=False, b1=True, b2=False)
    assert len(fifo_empty) == 0


def test_b1_even(fifo_even):
    pipeline(fifo_even, a1=False, a2=False, b1=True, b2=False)
    assert len(fifo_even) == 2


def test_b1_odd(fifo_odd):
    len_fifo = len(fifo_odd)
    pipeline(fifo_odd, a1=False, a2=False, b1=True, b2=False)
    assert len(fifo_odd) == len_fifo


def test_b2_empty(fifo_empty):
    pipeline(fifo_empty, a1=False, a2=False, b1=False, b2=True)
    assert len(fifo_empty) == 0


def test_b2_even(fifo_even):
    old = len(fifo_even)
    pipeline(fifo_even, a1=False, a2=False, b1=False, b2=True)
    assert len(fifo_even) == old


def test_b2_odd(fifo_odd):
    pipeline(fifo_odd, a1=False, a2=False, b1=False, b2=True)
    assert len(fifo_odd) == 6


def test_a1_a2_empty(fifo_empty):
    pipeline(fifo_empty, a1=True, a2=True, b1=False, b2=False)
    assert len(fifo_empty) == 20 or len(fifo_empty) == 21


def test_b1_b2_empty(fifo_empty):
    pipeline(fifo_empty, a1=False, a2=False, b1=True, b2=True)
    assert len(fifo_empty) == 0


def test_b1_b2_mix(fifo_more_even):
    pipeline(fifo_more_even, a1=False, a2=False, b1=True, b2=True)
    assert len(fifo_more_even) == 2
    assert fifo_more_even.even_values == 0
    assert fifo_more_even.odd_values == 2


def test_b1_b2_odd(fifo_odd):
    pipeline(fifo_odd, a1=False, a2=False, b1=True, b2=True)
    assert len(fifo_odd) == 6
    assert fifo_odd.odd_values == 6


def test_a1_b1(fifo_empty):
    pipeline(fifo_empty, a1=True, a2=False, b1=True, b2=False)
    assert len(fifo_empty) == fifo_empty.even_values
    assert fifo_empty.even_values == 3 or fifo_empty.even_values == 2
    assert fifo_empty.odd_values == 0


def test_all(fifo_empty):
    pipeline(fifo_empty)
    assert len(fifo_empty) > 2
    assert fifo_empty.odd_values >= fifo_empty.even_values

