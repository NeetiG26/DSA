class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, data):
        if self.first == None:
            self.first = Node(data)
            self.last = self.first
            return

        second_last = self.last
        self.last = Node(data)
        second_last.next = self.last

    def pop(self):
        if self.first == None:
            print('Empty Queue')
            return

        temp = self.first
        self.first = self.first.next
        return temp.data

    def peek(self):
        if self.first == None:
            print('Empty Queue')
            return
        return self.first.data

    def is_empty(self):
        return (self.first == None)

    def __str__(self):
        if self.first is None:
            return 'Empty Queue'
        temp = self.first
        while temp.next:
            print(temp.data , end=',')
            temp = temp.next
        print(temp.data)
        return ''


queue = Queue()
print(queue.is_empty())
print(queue.peek())

queue.push(1)
print(queue.peek())
queue.pop()
print(queue.is_empty())
print(queue.peek())
print(queue)

queue.push(2)
queue.push(3)
print(queue.is_empty())
print(queue.peek())
print(queue)
queue.pop()
print(queue)