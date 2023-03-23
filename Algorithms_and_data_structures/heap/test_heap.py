import pytest
from heap import Heap


@pytest.fixture(
    params=[2, 3, 4]
)
def heap_instance(request):
    heap = Heap(request.param)
    return heap


@pytest.fixture(
    params=[2, 3, 4]
)
def heap_with_values(request):
    input_val = [2, 6, 4, 1, 7, 54, 45]
    heap = Heap(request.param)
    heap.make_heap(input_val)
    return heap


def test_fulfilling_heap(heap_instance):
    input_values = [6, 2, 7, 1, 8, 4, 11, 65, 18, 62]
    heap_instance.make_heap(input_values)
    heap_values = heap_instance.get_raw_data()
    if heap_instance.n_arn == 2:
        assert heap_values == [1, 2, 4, 6, 8, 7, 11, 65, 18, 62]
    else:
        assert heap_values == [1, 2, 7, 6, 8, 4, 11, 65, 18, 62]


def test_pushing_heap(heap_instance):
    input_val = [2, 6, 4, 1, 7, 54, 45]
    for i in input_val:
        heap_instance.push(i)
    heap_values = heap_instance.get_raw_data()
    if heap_instance.n_arn == 2:
        assert heap_values == [1, 2, 4, 6, 7, 54, 45]
    else:
        assert heap_values == [1, 6, 4, 2, 7, 54, 45]


def test_pop(heap_with_values):
    m = heap_with_values.pop()
    assert m == 1
    assert len(heap_with_values) == 6
    m = heap_with_values.pop()
    assert m == 2
    assert len(heap_with_values) == 5
    m = heap_with_values.pop()
    assert m == 4
    assert len(heap_with_values) == 4


def test_push(heap_with_values):
    assert len(heap_with_values) == 7
    old_vals = heap_with_values.get_raw_data().copy()
    heap_with_values.push(13)
    assert len(heap_with_values) == 8
    old_vals.append(13)
    assert heap_with_values.get_raw_data().sort() == old_vals.sort()
    heap_with_values.push(90)
    assert len(heap_with_values) == 9
    old_vals.append(90)
    assert heap_with_values.get_raw_data().sort() == old_vals.sort()
    heap_with_values.push(3)
    assert len(heap_with_values) == 10
    old_vals.append(3)
    assert heap_with_values.get_raw_data().sort() == old_vals.sort()
