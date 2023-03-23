import numpy as np
import math


class Heap:
    def __init__(self, n_arn=2):
        self.n_arn = n_arn
        self.heap = []

    def _parent(self, k: int) -> int:
        return (k-1) // self.n_arn

    def _find_idx_min_value_child(self, k: int) -> int:
        starting_idx = k * self.n_arn + 1
        ending_idx = starting_idx + self.n_arn
        if ending_idx < len(self.heap):
            min_idx = np.argmin(self.heap[starting_idx:ending_idx])
            return starting_idx + min_idx
        else:
            min_idx = np.argmin(self.heap[starting_idx:])
            return starting_idx + min_idx

    def _left(self, k: int) -> int:
        return self.n_arn * k + 1

    def up_heap(self, k: int):
        while k != 0 and self.heap[self._parent(k)] > self.heap[k]:
            self.heap[k], self.heap[self._parent(k)] = self.heap[self._parent(k)], self.heap[k]
            k = self._parent(k)

    def down_heap(self, k: int):
        while self._left(k) < len(self.heap):
            j = self._find_idx_min_value_child(k)
            if self.heap[k] < self.heap[j]:
                break
            self.heap[k], self.heap[j] = self.heap[j], self.heap[k]
            k = j

    def top(self):
        return self.heap[0]

    def pop(self):
        root = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop(-1)
        self.down_heap(0)
        return root

    def push(self, element):
        self.heap.append(element)
        self.up_heap(len(self.heap) - 1)

    def make_heap(self, elements: list):
        self.heap = elements
        for a in range((len(self.heap) - 2)//self.n_arn, -1, -1):
            self.down_heap(a)

    def __len__(self) -> int:
        return len(self.heap)

    def get_raw_data(self):
        return self.heap

    def display(self):
        size = len(self.heap)
        line = f"{size*' '}{self.heap[0]}{size*' '}"
        print(line)
        max_height = math.floor(math.log(size, self.n_arn)) + 1
        if not self.n_arn == 2:
            max_height+=1
        current_idx = 1
        for i in range(1, max_height-1, 1):
            nodes_in_line = pow(self.n_arn, i)
            line = ""
            for j in range(nodes_in_line):
                tmp_size = size//nodes_in_line
                line += f"{tmp_size*' '}{self.heap[current_idx]}{(tmp_size-1)*' '}"
                current_idx += 1
            print(line)
        possible_nodes_in_last_line = self.n_arn * max_height
        last_line = ""
        last_size = size//possible_nodes_in_last_line
        for i in range(possible_nodes_in_last_line):
            if current_idx == size:
                break
            if i == 0:
                last_line += f"{self.heap[current_idx]}"
            else:
                last_line += f"{last_size*' '}{self.heap[current_idx]}"
            current_idx += 1
        print(last_line)

