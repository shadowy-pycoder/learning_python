import operator
from random import shuffle


class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data!r})'

    def __str__(self):
        return f'{self.data!r}'


class LinkedList:

    all: list["LinkedList"] = []

    def __init__(self, head) -> None:
        try:
            iter(head)
        except TypeError:
            raise NotImplementedError('head must be iterable')
        self.__nodes = self.__nodize(head)
        LinkedList.all.append(self)

    def __repr__(self):
        cls_name = type(self).__name__
        return f"{cls_name}({' -> '.join([str(node) for node in self][:5])} -> ...)"

    def __str__(self):
        return ' -> '.join([str(node) for node in self]) + ' -> None'

    def __len__(self):
        return len(self.__nodes)

    def __iter__(self):
        return iter(self.__nodes)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self.__nodes[key])
        key = operator.index(key)
        return self.__nodes[key]

    def __setitem__(self, key, new_node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)
        self.__nodes[key] = new_node
        self.__nodize(self.__nodes)

    def __delitem__(self, key):
        del self.__nodes[key]
        self.__nodize(self.__nodes)

    def __iadd__(self, other):
        cls = type(self)
        if isinstance(other, cls):
            self.__nodes.extend(other)
        else:
            try:
                self.__nodes.extend(other)
            except TypeError:
                msg = (
                    f"right operand in += must be '{cls.__name__}' or an iterable")
                raise TypeError(msg) from None
        self.__nodize(self.__nodes)
        return self

    def __add__(self, other):
        cls = type(self)
        if isinstance(other, cls):
            return cls(self.__nodize(self.__nodes + other.__nodes))
        else:
            return NotImplemented

    def reverse(self):
        self.__nodes = self.__nodes[::-1]
        self.__nodize(self.__nodes)

    def shuffle(self):
        shuffle(self.__nodes)
        self.__nodize(self.__nodes)

    def insert_node(self, key, new_node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)
        self.__nodes.insert(key, new_node)
        self.__nodize(self.__nodes)

    def __nodize(self, iterable):
        nodes = list(iterable)
        nodes = [node if isinstance(node, Node) else Node(node)
                 for node in nodes]
        self.head = nodes[0]
        current_node = self.head
        for i in range(1, len(nodes)):
            current_node.next = nodes[i]
            current_node = current_node.next
        return nodes

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        for line in lines:
            head = ''.join(char for char in line if char.isalnum())
            if head:
                cls(head)
