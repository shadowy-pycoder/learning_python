class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data!r})'

    def __str__(self):
        return self.data


class LinkedList:

    def __init__(self, head: Node) -> None:
        self.head = head

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

    def __getitem__(self, index):
        current_index = 0
        for node in self.__iter__():
            if current_index == index:
                return node.data
            current_index += 1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
