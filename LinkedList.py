## Linked List implementation

class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self) -> str:
        return str(self.data)


class LinkedList():
    def __init__(self, data=None) -> None:
        self.head = None
        self.tail = None

        if data is not None:
            self.add_multiple_nodes(data)

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def prepend(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data, self.head)
        return self.head

    def append(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
        return self.tail

    def add_multiple_nodes(self, data):
        for elem in data:
            self.append(elem)

    def printList(self):
        array = []
        currentNode = self.head
        while currentNode != None:
            array.append(currentNode.data)
            currentNode = currentNode.next
        print(array)

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return self
        elif index > len(self) - 1:
            raise IndexError('list index out of range')

        newNode = Node(data)
        leadNode = self.traverse(index-1)
        pointer_holder = leadNode.next

        leadNode.next = newNode
        newNode.next = pointer_holder

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return self
        leadNode = self.traverse(index-1)
        pointer_holder = self.traverse(index)
        leadNode.next = pointer_holder.next

    def traverse(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode.next
            counter += 1
        return currentNode

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def reverse(self):
        if not self.head.next:
            return self.head

        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first


if __name__ == '__main__':
    l_list = LinkedList()
    l_list.prepend(13)
    l_list.prepend(12)
    l_list.append(14)
    l_list.append(16)
    l_list.prepend(1)
    l_list.insert(2, 56)
    l_list.remove(2)
    l_list.reverse()
    l_list.printList()
    print(len(l_list))
