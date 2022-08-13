class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, data):
        if self.root is None:
            return

        current_node = self.root
        while current_node:
            if current_node.data == data:
                print(current_node.data)
                return current_node
            if current_node.data > data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        print("No such node found")

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)

        else:
            current_node = self.root
            while True:
                if current_node.data > data:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = TreeNode(data)
                        break
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = TreeNode(data)
                        break

    def remove(self, data):
        if self.root is None:
            print("Empty Tree")
            return

        if self.root.data == data:
            if self.root.left is None and self.root.right is None:
                self.root = None

            elif self.root.left is None and self.root.right is not None:
                self.root = self.root.right

            elif self.root.left is not None and self.root.right is None:
                self.root = self.root.left

            else:
                if self.root.right.left is None:
                    self.root.right.left = self.root.left
                    self.root = self.root.right
                else:
                    parent_node = self.root
                    current_node = self.root.right
                    while current_node.left is not None or current_node.right is not None:
                        parent_node = current_node
                        current_node = current_node.left
                    if current_node.right is not None:
                        data_to_shift = current_node.data
                        parent_node.left = current_node.right
                        self.root.data = data_to_shift
                    else:
                        self.root.data = current_node.data
                        parent_node.left = None

            return

        current_node = self.root
        parent_node_of_target = None
        node_to_be_deleted = self.find(data)
        while parent_node_of_target is None:
            if node_to_be_deleted is None:
                return
            else:
                if data > current_node.data:
                    prev_node = current_node
                    current_node = current_node.right
                elif data < current_node.data:
                    prev_node = current_node
                    current_node = current_node.left
                else:
                    parent_node_of_target = prev_node
                    print("parent_node_of_target: ", parent_node_of_target.data)

        if node_to_be_deleted.left is None and node_to_be_deleted.right is None:
            if parent_node_of_target.left == node_to_be_deleted:
                parent_node_of_target.left = None
            if parent_node_of_target.right == node_to_be_deleted:
                parent_node_of_target.right = None

        elif node_to_be_deleted.left is None and node_to_be_deleted.right is not None:
            if parent_node_of_target.left == node_to_be_deleted:
                parent_node_of_target.left = node_to_be_deleted.right
            if parent_node_of_target.right == node_to_be_deleted:
                parent_node_of_target.right = node_to_be_deleted.right

        elif node_to_be_deleted.left is not None and node_to_be_deleted.right is None:
            if parent_node_of_target.left == node_to_be_deleted:
                parent_node_of_target.left = node_to_be_deleted.left
            if parent_node_of_target.right == node_to_be_deleted:
                parent_node_of_target.right = node_to_be_deleted.left

        else:
            if node_to_be_deleted.right.left is None:
                node_to_be_deleted.right.left = node_to_be_deleted.left
                if parent_node_of_target.left == node_to_be_deleted:
                    parent_node_of_target.left = node_to_be_deleted.right
                if parent_node_of_target.right == node_to_be_deleted:
                    parent_node_of_target.right = node_to_be_deleted.right

            else:
                current_node = node_to_be_deleted.right
                while current_node.left is not None or current_node.right is not None:
                    parent_node = current_node
                    current_node = current_node.left
                if current_node.right is not None:
                    data_to_shift = current_node.data
                    parent_node.left = current_node.right
                    node_to_be_deleted.data = data_to_shift
                else:
                    node_to_be_deleted.data = current_node.data
                    parent_node.left = None



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
        elif stack:
            current = stack.pop()
            print(current.data, end=" ")  # Python 3 printing

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right

        else:
            break

    print()


def preOrder(root):

    if (root == None):
        return

    st = []

    # start from root node (set current node to root node)
    curr = root

    # run till stack is not empty or current is
    # not NULL
    while (len(st) or curr != None):

        # Print left children while exist
        # and keep appending right into the
        # stack.
        while (curr != None):

            print(curr.data, end=" ")

            if (curr.right != None):
                st.append(curr.right)

            curr = curr.left

        # We reach when curr is NULL, so We
        # take out a right child from stack
        if (len(st) > 0):
            curr = st[-1]
            st.pop()
    print()


def postOrder(root):
    if root is None:
        return

        # Create two stacks
    s1 = []
    s2 = []

    # Push root to first stack
    s1.append(root)

    # Run while first stack is not empty
    while s1:

        # Pop an item from s1 and
        # append it to s2
        node = s1.pop()
        s2.append(node)

        # Push left and right children of
        # removed item to s1
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

        # Print all elements of second stack
    while s2:
        node = s2.pop()
        print(node.data, end=" ")
    print()


bst = BinarySearchTree()
bst.remove(2)
bst.insert(4)
# bst.insert(2)
# bst.insert(8)
# bst.insert(5)
# bst.insert(9)
# bst.insert(6)
# bst.insert(7)
inOrder(bst.root)
# bst.insert(1)
# bst.remove(4)
# print("After root removal")
# inOrder(bst.root)
bst.insert(2)
bst.insert(7)
# inOrder(bst.root)
# bst.remove(2)
# inOrder(bst.root)
bst.insert(1)
bst.insert(5)

inOrder(bst.root)
bst.remove(4)
inOrder(bst.root)

bst.insert(6)
print("Inorder")
inOrder(bst.root)
print("Preorder")
preOrder(bst.root)
print("Postorder")
postOrder(bst.root)
bst.find(2)
bst.find(8)

bst.remove(5)
inOrder(bst.root)
