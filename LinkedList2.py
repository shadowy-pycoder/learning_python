import operator
from random import shuffle


class Node:

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'

    def __str__(self):
        return f'{self.data}'


class LinkedList:

    def __init__(self, head) -> None:
        self.nodes = self.__nodize(head)

    def __repr__(self):
        cls_name = type(self).__name__
        return f"{cls_name}({' -> '.join([str(node) for node in self][:5])} -> ...)"

    def __str__(self):
        return ' -> '.join([str(node) for node in self]) + ' -> None'

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self.nodes[key])
        key = operator.index(key)
        return self.nodes[key]

    def __setitem__(self, key, new_node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)
        self.nodes[key] = new_node
        self.__nodize(self.nodes)

    def __delitem__(self, key):
        del self.nodes[key]
        self.__nodize(self.nodes)

    def __add__(self, other):
        cls = type(self)
        if not isinstance(other, cls):
            raise NotImplementedError(
                f'both values must be of the same class {cls}')
        return cls(self.__nodize(self.nodes + other.nodes))

    def reverse(self):
        self.nodes = self.nodes[::-1]
        self.__nodize(self.nodes)

    def shuffle(self):
        shuffle(self.nodes)
        self.__nodize(self.nodes)

    def insert_node(self, key, new_node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)
        self.nodes.insert(key, new_node)
        self.__nodize(self.nodes)

    def __nodize(self, iterable):
        nodes = list(iterable)
        if not isinstance(nodes[0], Node):
            nodes = [Node(node) for node in nodes]
        self.head = nodes[0]
        current_node = self.head
        for i in range(1, len(nodes)):
            current_node.next = nodes[i]
            current_node = current_node.next
        return nodes

