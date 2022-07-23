class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top == None:
            self.top = Node(data)
            return

        temp = self.top
        self.top = Node(data)
        self.top.next = temp

    def pop(self):
        if self.top == None:
            print('Empty Stack')
            return
        temp = self.top
        self.top = self.top.next
        return temp.data

    def peek(self):
        if self.top == None:
            print('Empty Stack')
            return
        return self.top.data

    def is_empty(self):
        return (self.top == None)

    def __str__(self):
        if self.top is None:
            return 'Empty Stack'
        temp = self.top
        while temp.next:
            print(temp.data , end=',')
            temp = temp.next
        print(temp.data)
        return ''


stack = Stack()
print(stack.is_empty())
print(stack.peek())

stack.push(1)
print(stack.peek())
stack.pop()
print(stack.is_empty())
print(stack.peek())
print(stack)

stack.push(2)
stack.push(3)
print(stack.is_empty())
print(stack.peek())
print(stack)
