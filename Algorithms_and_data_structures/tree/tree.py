from abc import ABC, abstractmethod
COUNT = [10]


class Tree(ABC):
    def __init__(self, key=None, val=None, size=None):
        self.key = key
        if val is None:
            val = key
        self.value = val
        self.size = size
        self.left = None
        self.right = None

    def get(self, key):
        if key is None:
            raise Exception(f"Pass None as Key, key")
        if self.key is None:
            return None
        if key < self.key:
            return Tree.get(self.left, key)
        elif key > self.key:
            return Tree.get(self.right, key)
        else:
            return self.value

    @abstractmethod
    def insert(self, key, value=None):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    def custom_display(self):
        lines = {}
        self._custom_display(lines, 0)
        keys = lines.keys()
        sorted_keys = sorted(keys)
        for i in sorted_keys:
            print(lines[i])


    def _custom_display(self, lines, depth):
        # mnoznik razy 4
        if self.left and self.right:
            self.left._custom_display(lines, depth+1)
            self.right._custom_display(lines, depth+1)
            try:
                lines[depth] += f"{(self.size*2)*' '}--{self.value}--{(self.size*2)*' '}"
            except:
                lines[depth] = f"{(self.size*2)*' '}--{self.value}--{(self.size*2)*' '}"
        elif self.left:
            self.left._custom_display(lines, depth+1)
            try:
                lines[depth] += f"{(self.size) * ' '}--{self.value}{(self.size * 3) * ' '}"
            except:
                lines[depth] = f"{(self.size) * ' '}--{self.value}{(self.size * 3) * ' '}"
        elif self.right:
            self.right._custom_display(lines, depth+1)
            try:
                lines[depth] += f"{(self.size * 3) * ' '}{self.value}--{(self.size) * ' '}"
            except:
                lines[depth] = f"{(self.size * 3) * ' '}{self.value}--{(self.size) * ' '}"
        else:
            try:
                lines[depth] += f"-{(self.size * 4) * ' '}{self.value}{(self.size*4) * ' '}-"
            except:
                lines[depth] = f"-{(self.size * 4) * ' '}{self.value}{(self.size*4) * ' '}-"

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f"{self.key}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f"{self.key}"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f"{self.key}"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f"{self.key}"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def get_all_tree_values(self):
        values_list = []
        Tree._get_tree_values(self, values_list)
        return values_list

    @staticmethod
    def _get_tree_values(root, values_list):
        if root.left:
            Tree._get_tree_values(root.left, values_list)
        if root.left is None:
            values_list.append(root.key)
        if root.right:
            Tree._get_tree_values(root.right, values_list)
        if root.key not in values_list:
            values_list.append(root.key)

    def _min(self):
        if self.left is None:
            return self
        else:
            return Tree._min(self.left)

    def _delete_min(self):
        if self.left is None:
            return self.right
        self.left = Tree._delete_min(self.left)
        tmp_size = 1
        if self.left:
            tmp_size += self.left.size
        if self.right:
            tmp_size += self.right.size
        self.size = tmp_size
        return self

    def rebuild_node(self, node):
        self.key = node.key
        self.value = node.value
        self.left = node.left
        self.right = node.right
        self.size = node.size
