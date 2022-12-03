class Node:

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data!r})'

    def __str__(self):
        return f'{self.data}'


class LinkedList:

    def __init__(self, head) -> None:
        if isinstance(head, list):
            self.head = Node(head[0])
            current_node = self.head
            for i in range(1, len(head)):
                current_node.next = Node(head[i])
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
            if (step > 0 and abs(start) < abs(stop)) or (step < 0 and abs(start) > abs(stop)):
                return LinkedList([node_list[i] for i in range(start, stop, step)])
            elif step == 0:
                raise ValueError('slice step cannot be zero')
        elif isinstance(key, int):
            return node_list[key]
        elif isinstance(key, tuple):
            raise NotImplementedError('Tuple as index')
        else:
            raise TypeError(f'Invalid argument {type(key)}')

    def __setitem__(self, key, new_node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)
        if key == 0:
            prev_node = self.head
            self.head = new_node
            self.head.next = prev_node
        elif key < 0:
            print('Invalid argument')
        else:
            try:
                prev_node = self.__getitem__(key - 1)
            except IndexError:
                print('Invalid argument')
            else:
                try:
                    next_node = self.__getitem__(key)
                except IndexError:
                    next_node = None
                    prev_node.next = new_node
                else:
                    prev_node.next = new_node
                    new_node.next = next_node

    def __delitem__(self, key):
        if key == 0:
            next_node = self.__getitem__(key + 1)
            self.head = next_node
        elif key < 0:
            print('Invalid argument')
        else:
            try:
                prev_node = self.__getitem__(key - 1)
            except IndexError:
                print('Invalid argument')
            else:
                if prev_node.next is not None:
                    try:
                        next_node = self.__getitem__(key + 1)
                    except IndexError:
                        next_node = None
                        prev_node.next = next_node
                    else:
                        prev_node.next = next_node
                else:
                    print('Invalid argument')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
