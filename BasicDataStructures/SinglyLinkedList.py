class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def __str__(self):
        print(self.data, self.next)
        return ''


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        if self.head is None:
            return

        first = self.head
        second_node = first.next
        while second_node:
            temp = second_node.next
            second_node.next = first
            first = second_node
            second_node = temp
        self.head.next = None
        self.head = first


ll = LinkedList()

ll.head = Node(1)
print(ll.head)
second = Node(2)
print(second)
third = Node(3)
print(third)

ll.head.next = second
second.next = third
# print(ll.head)
# print(second)
# print(third)
ll.printlist()

ll.push(4)
ll.printlist()

ll.insert_after(second, 5)
ll.printlist()

ll.append(6)
ll.printlist()

ll.reverse()
ll.printlist()
