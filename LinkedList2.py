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
        if isinstance(head, list):
            if not isinstance(head[0], Node):
                self.head = Node(head[0])
                self.nodes = [self.head]
                current_node = self.head
                for i in range(1, len(head)):
                    current_node.next = Node(head[i])
                    self.nodes.append(current_node.next)
                    current_node = current_node.next
            else:
                self.head = head[0]
                self.nodes = [self.head]
                current_node = self.head
                for i in range(1, len(head)):
                    current_node.next = head[i]
                    self.nodes.append(current_node.next)
                    current_node = current_node.next
        elif isinstance(head, Node):
            self.head = head
            current, self.nodes = head, []
            while current is not None:
                self.nodes.append(current)
                current = current.next
        else:
            raise NotImplementedError(f'Invalid argument {type(head)}')

    def __repr__(self):
        nodes = [str(node) for node in self.nodes]
        return f"LinkedList({' -> '.join(nodes[:6])} -> ...)"

    def __str__(self):
        nodes = [str(node) for node in self.nodes]
        return f"{' -> '.join(nodes)} -> None"

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
        self.nodes.insert(key, new_node)
        self.__nodize(self.nodes)

    def __nodize(self, node_list):
        self.head = node_list[0]
        current_node = self.head
        for i in range(1, len(node_list)):
            current_node.next = node_list[i]
            current_node = current_node.next
        return node_list
