import pytest
from quick_sort import quick_sort
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort


@pytest.mark.parametrize("func", [merge_sort, bubble_sort, selection_sort, quick_sort])
def test_empty_input(func):
    data = func([])
    assert data == []


@pytest.mark.parametrize("func", [merge_sort, bubble_sort, selection_sort, quick_sort])
def test_sorting_numbers(func):
    input_data = [2, 1, 9, 55, 2, 44, 4, 7, 89]
    data = func(input_data)
    assert data == [1, 2, 2, 4, 7, 9, 44, 55, 89]


@pytest.mark.parametrize("func", [merge_sort, bubble_sort, selection_sort, quick_sort])
def test_sorting_big_chars(func):
    input_data = ["C", "R", "A", "L", "E"]
    data = func(input_data)
    assert data == ['A', 'C', 'E', 'L', 'R']


@pytest.mark.parametrize("func", [merge_sort, bubble_sort, selection_sort, quick_sort])
def test_sorting_small_chars(func):
    input_data = ["c", "r", "a", "l", "e"]
    data = func(input_data)
    assert data == ['a', 'c', 'e', 'l', 'r']


@pytest.mark.parametrize("func", [merge_sort, bubble_sort, selection_sort, quick_sort])
def test_sorting_strings(func):
    input_data = ["ZZZ", "CBA", "ABC", "DRZEWO"]
    data = func(input_data)
    assert data == ['ABC', 'CBA', 'DRZEWO', 'ZZZ']


@pytest.mark.parametrize("func", [merge_sort, bubble_sort, selection_sort, quick_sort])
def test_sorting_strings_with_different_letter_size(func):
    input_data = ["zzz", "CBa", "AbC", "DRZEWO", "abac"]
    data = func(input_data)
    assert data == ['AbC', 'CBa', 'DRZEWO', 'abac', 'zzz']






