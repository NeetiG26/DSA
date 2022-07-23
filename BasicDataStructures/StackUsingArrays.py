
class Stack:
    def __init__(self):
        self.stack = None

    def push(self, data):
        if self.stack == None:
            self.stack = [data]
            return
        self.stack.append(data)

    def pop(self):
        if self.stack == None:
            print('Empty Stack')
            return

        if len(self.stack) == 1:
            temp = self.stack[-1]
            self.stack = None
            return temp

        return self.stack.pop()

    def peek(self):
        if self.stack == None:
            print('Empty Stack')
            return
        return self.stack[-1]

    def is_empty(self):
        return (self.stack == None)

    def __str__(self):
        if self.stack is None:
            return 'Empty Stack'

        print(self.stack)
        return ''


stack = Stack()
print('is empty', stack.is_empty())
print('peek', stack.peek())

stack.push(1)
print('peek', stack.peek())
stack.pop()
print('is empty', stack.is_empty())
print('peek', stack.peek())
print('stack ', stack)

stack.push(2)
stack.push(3)
print(stack.is_empty())
print(stack.peek())
print(stack)
stack.pop()
print(stack)
