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
        index = operator.index(key)
        return self.nodes[index]

#    if the key argument is a slice...
# ...get the class of the instance (i.e., LinkedList) and...
# ...invoke the class to build another LinkedList instance from a slice of the
# _components array.
# If we can get an index from key...
# ...return the specific item from _components.

    def __setitem__(self, key, new_node: Node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)
        if key == 0:
            self.head = new_node
        if key < 0:
            raise IndexError('Index cannot be negative')
        self.nodes[key] = new_node
        for index, node in enumerate(self.nodes):
            if index == key - 1:
                node.next = new_node
            if index == key + 1:
                new_node.next = node
                break

    def __delitem__(self, key):
        if key == 0:
            self.head = self.head.next
            del self.nodes[key]
        elif key < 0 or key >= len(self.nodes):
            raise IndexError('Invalid index')
        elif key == len(self.nodes) - 1:
            self.nodes[key-1].next = None
            del self.nodes[key]
        else:
            self.nodes[key-1].next = self.nodes[key+1]
            del self.nodes[key]

    def reverse(self):
        self.nodes = self.nodes[::-1]
        self.__nodize(self.nodes)

    def shuffle(self):
        shuffle(self.nodes)
        self.__nodize(self.nodes)

    def insert_node(self, key, new_node):
        self.nodes.insert(key, new_node)
        self.__nodize(self.nodes)

    def __add__(self, other):
        cls = type(self)
        if not isinstance(other, cls):
            raise NotImplementedError(
                f'both values must be of the same class {cls}')
        return cls(self.__nodize(self.nodes + other.nodes))

    def __nodize(self, node_list):
        self.head = node_list[0]
        current_node = self.head
        for i in range(1, len(node_list)):
            current_node.next = node_list[i]
            current_node = current_node.next
        return node_list
