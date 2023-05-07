class FIFO:
    def __init__(self, init_values=None):
        if init_values:
            self.data = init_values
        else:
            self.data = []

    def get(self) -> int:
        return self.data.pop(0)

    def get_even(self) -> int:
        even_index = None
        for i, data in enumerate(self.data):
            if data % 2 == 0:
              even_index = i
              break
        if even_index is None:
            return -1
        else:
            return self.data.pop(even_index)

    def get_odd(self) -> int:
        odd_index = None
        for i, data in enumerate(self.data):
            if data % 2 != 0:
                odd_index = i
                break
        if odd_index is None:
            return -1
        return self.data.pop(odd_index)

    def put(self, number: int):
        self.data.append(number)

    @property
    def even_values(self):
        even_values = 0
        for val in self.data:
            if val % 2 == 0:
                even_values += 1
        return even_values

    @property
    def odd_values(self):
        odd_values = 0
        for val in self.data:
            if val % 2 != 0:
                odd_values += 1
        return odd_values

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return str(self.data)

