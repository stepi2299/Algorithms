from random import shuffle
import sys


sys.setrecursionlimit(10000)


def quick_sort(contents):
    shuffle(contents)
    sort_table(contents, 0, len(contents) - 1)
    return contents


def sort_table(contents, start, stop):
    if stop <= start:
        return
    split_point = split_table(contents, start, stop)
    sort_table(contents, start, split_point - 1)
    sort_table(contents, split_point + 1, stop)


def split_table(contents, start, stop):
    mid = contents[start]
    i = start + 1
    j = stop
    while True:
        while contents[i] < mid and i != j:
            i = i + 1
        while contents[j] >= mid and i != j:
            j = j - 1
        if i == j:
            break
        else:
            contents[i], contents[j] = contents[j], contents[i]
    if contents[i] >= mid:
        contents[start], contents[i - 1] = contents[i - 1], contents[start]
        return i - 1
    else:
        contents[start], contents[i] = contents[i], contents[start]
        return i
