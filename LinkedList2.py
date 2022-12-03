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
        return (i for i in self.nodes)

    def __getitem__(self, key):
        return LinkedList(self.nodes[key])

    def __setitem__(self, key, new_node: Node):
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
        self.head = self.nodes[0]
        current_node = self.head
        for i in range(1, len(self.nodes)):
            current_node.next = self.nodes[i]
            current_node = current_node.next
