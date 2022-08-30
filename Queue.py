class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0

    def peek(self):
        return self.first

    def enqueue(self, data):
        if self.len == 0:
            self.first = self.last = Node(data)
        else:
            node = Node(data)
            self.last.next = node
            self.last = self.last.next
        self.len += 1

    def dequeue(self):
        if not self.first:
            return None
        elif self.len == 1:
            self.last = None
        self.first = self.first.next
        self.len -= 1


if __name__ == '__main__':
    queue1 = Queue()
    queue1.enqueue('Joy')
    queue1.enqueue('Matt')
    queue1.enqueue('Jeff')
    queue1.dequeue()

    print(queue1.last.data)
