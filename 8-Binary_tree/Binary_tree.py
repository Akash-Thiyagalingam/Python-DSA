# Creating class for Binary tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#Function for inserting an element in a Binary tree
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

#Function for deleting an element in a Binary tree
def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = get_min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

#Function for getting minimum value in a Binary tree
def get_min_value(root):
    while root.left is not None:
        root = root.left
    return root

#Function for In Order Traversal of a Binary tre
def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.key, end=' ')
        in_order_traversal(root.right)

#Function for Pre Order Traversal of a Binary tre
def pre_order_traversal(root):
    if root is not None:
        print(root.key, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

#Function for Post Order Traversal of a Binary tre
def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.key, end=' ')
