from StackUsingLinkedList import Stack
from QueueUsingLinkedList import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryHeap:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return
        else:
            q = Queue()
            current_node = self.root
            q.push(current_node)
            while current_node.right is not None and current_node.left is not None:
                if current_node.left is not None:
                    q.push(current_node.left)
                if current_node.right is not None:
                    q.push(current_node.right)
                current_node = q.pop()
        if current_node.left:
            current_node.right = TreeNode(data)
            new_node = current_node.right
        else:
            current_node.left = TreeNode(data)
            new_node = current_node.left

        next_node = new_node
        while not q.is_empty():
            current_node = q.pop()
            if current_node.data > next_node.data:
                temp_data = next_node.data
                next_node.data = current_node.data
                current_node.data = temp_data
                next_node = current_node
            else:
                break

    def extract_min(self):
        if self.root is None:
            print("Empty Tree")
            return

        if self.root.right is not None and self.root.left is not None:
            data_to_return = self.root.data
            self.root = None
            return data_to_return

        data_to_return = self.root.data
        current_node = self.root
        q = Queue
        while current_node.right is not None and current_node.left is not None:
            parent_node = current_node
            if current_node.right is not None:
                current_node = current_node.right
            else:
                current_node = current_node.left
            q.push(current_node)

        self.root.data = current_node.data
        if parent_node.left == current_node:
            parent_node.left = None
        else:
            parent_node.right = None

        current_node = self.root.data
        next_node = q.pop()
        while len(q):
            if current_node.data > next_node.data:
                temp_data = next_node.data
                next_node.data = current_node.data
                current_node.data = temp_data
                current_node = next_node
                next_node = q.pop()
            else:
                return data_to_return
        return data_to_return

    def get_min(self):
        if self.root is None:
            print("Empty Tree")
            return
        return self.root.data


def levelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        print(queue[0].data, end=" ")
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
    print()


bh = BinaryHeap()
bh.insert(4)
levelOrder(bh.root)
# # bst.insert(1)
# # bst.remove(4)
# # print("After root removal")
# # inOrder(bst.root)
bh.insert(2)
bh.insert(7)
print("Level order")
levelOrder(bh.root)
# # inOrder(bst.root)
# # bst.remove(2)
# # inOrder(bst.root)
bh.insert(1)
bh.insert(5)
print("Level order")
levelOrder(bh.root)
bh.insert(9)
bh.insert(3)
print("Level order")
levelOrder(bh.root)
#
# bh.extract_min()
# print("Level order")
# levelOrder(bh.root)
#
# bh.insert(8)
#
# print("Level order")
# levelOrder(bh.root)
