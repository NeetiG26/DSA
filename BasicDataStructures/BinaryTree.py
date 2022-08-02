from QueueUsingLinkedList import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return

        q = Queue()
        current_node = self.root
        while current_node.left and current_node.right:
            q.push(current_node.left)
            q.push(current_node.right)
            current_node = q.pop()

        if current_node.left is None:
            current_node.left = TreeNode(data)
        else:
            current_node.right = TreeNode(data)


    def remove(self, data):
        if self.root is None:
            print("Tree has no nodes to be removed")
            return BinaryTree()

        if self.root.left is None and self.root.right is None:
            if self.root.data == data:
                return None
            else:
                return self.root

        q = Queue()
        current_node = None
        node_to_be_deleted = None
        node_to_be_moved = None
        q.push(self.root)

        while not q.is_empty():
            previous_node = current_node
            current_node = q.pop()
            if current_node.data == data:
                node_to_be_deleted = current_node
            if current_node.left is None and current_node.right is None:
                node_to_be_moved = current_node

            if current_node.left:
                q.push(current_node.left)

            if current_node.right:
                q.push(current_node.right)

        print("Node to be deleted ", node_to_be_deleted.data)
        print("Node to be moved ", node_to_be_moved.data)

        if node_to_be_deleted is not None:
            q.push(self.root)
            while not q.is_empty():
                current_node = q.pop()
                if current_node.left:
                    if current_node.left == node_to_be_moved:
                        current_node.left = None
                        if node_to_be_deleted != node_to_be_moved:
                            node_to_be_deleted.data = node_to_be_moved.data
                        return
                    else:
                        q.push(current_node.left)

                if current_node.right:
                    if current_node.right == node_to_be_moved:
                        current_node.right = None
                        if node_to_be_deleted != node_to_be_moved:
                            node_to_be_deleted.data = node_to_be_moved.data
                        return
                    else:
                        q.push(current_node.right)




def inOrder(root):
    # Set current to root of binary tree
    current = root
    stack = []  # initialize stack

    while True:

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.left

            # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif (stack):
            current = stack.pop()
            print(current.data, end=" ")  # Python 3 printing

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right

        else:
            break

    print()


bt = BinaryTree()
bt.root = TreeNode(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)

inOrder(bt.root)

bt.insert(6)
inOrder(bt.root)

bt.remove(2)
inOrder(bt.root)