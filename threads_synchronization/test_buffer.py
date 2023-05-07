import pytest

from buffer import FIFO


@pytest.fixture(name="fifo")
def fixture_fifo():
    return FIFO([4, 5, 6, 7, 8, 1, 6])


class TestFIFO:
    def test_get(self, fifo):
        assert len(fifo) == 7
        num = fifo.get()
        assert num == 4
        assert len(fifo) == 6
        num = fifo.get()
        assert num == 5
        assert len(fifo) == 5

    def test_get_even(self, fifo):
        assert len(fifo) == 7
        num = fifo.get_even()
        assert num == 4
        assert len(fifo) == 6
        num = fifo.get_even()
        assert num == 6
        assert len(fifo) == 5
        num = fifo.get_even()
        assert num == 8
        assert len(fifo) == 4

    def test_get_odd(self, fifo):
        assert len(fifo) == 7
        num = fifo.get_odd()
        assert num == 5
        assert len(fifo) == 6
        num = fifo.get_odd()
        assert num == 7
        assert len(fifo) == 5
        num = fifo.get_odd()
        assert num == 1
        assert len(fifo) == 4

    def test_put(self, fifo):
        fifo.put(10)
        assert len(fifo) == 8
        ind = fifo.data.index(10)
        assert ind == 7

    def test_even_values(self, fifo):
        even_count = fifo.even_values
        assert even_count == 4
        fifo.put(10)
        even_count = fifo.even_values
        assert even_count == 5
        fifo.put(11)
        even_count = fifo.even_values
        assert even_count == 5

    def test_odd_values(self, fifo):
        even_count = fifo.odd_values
        assert even_count == 3
        fifo.put(10)
        even_count = fifo.odd_values
        assert even_count == 3
        fifo.put(11)
        even_count = fifo.odd_values
        assert even_count == 4
