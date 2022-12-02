class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data!r})'

    def __str__(self):
        return f'{self.data}'


class LinkedList:

    def __init__(self, head) -> None:
        if isinstance(head, list):
            self.head = Node(head.pop(0))
            current_node = self.head
            while head:
                current_node.next = Node(head.pop(0))
                current_node = current_node.next
        elif isinstance(head, Node):
            self.head = head
        else:
            raise NotImplementedError(f'Invalid argument {type(head)}')

    def __repr__(self):
        nodes = list()
        for node in self.__iter__():
            nodes.append(str(node))
        return f"LinkedList({' -> '.join(nodes)})"

    def __str__(self):
        return self.__repr__()[11:-1] + ' -> None'

    def __len__(self):
        return len(self.__repr__()[11:-1].split(' -> '))

    def __iter__(self):
        self.n = self.head
        return self

    def __next__(self):
        if self.n is not None:
            next_node = self.n
            self.n = self.n.next
            return next_node
        else:
            raise StopIteration

    def __getitem__(self, key):
        node_list = list()
        for node in self.__iter__():
            node_list.append(node)
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return LinkedList([node_list[i] for i in range(start, stop, step)])
        elif isinstance(key, int):
            return node_list[key]
        elif isinstance(key, tuple):
            raise NotImplementedError('Tuple as index')
        else:
            raise TypeError(f'Invalid argument {type(key)}')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

