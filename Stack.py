class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.len = 0

    def peek(self):
        return self.top

    def push(self, data):
        if self.len == 0:
            self.top = self.bottom = Node(data)
        else:
            holding_pointer = self.top
            self.top = Node(data)
            self.top.next = holding_pointer
        self.len += 1
        return self.top

    def pop(self):
        if not self.top:
            return None
        elif self.len == 1:
            self.bottom = None
        current_node = self.top
        self.top = current_node.next
        self.len -= 1
        return current_node


if __name__ == '__main__':
    stack1 = Stack()
    stack1.push('google')
    stack1.push('udemy')
    stack1.push('discord')
    print(stack1.pop())
    # print(stack1.peek().next.data)
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.bottom)
    print(stack1.len)
