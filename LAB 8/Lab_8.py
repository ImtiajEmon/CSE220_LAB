'''
Name: MD IMTIAJ HOSSAIN
ID  : 19201031
Sec : 08'''
class Node():
    def __init__(self, key, p, l, r):
        self.key = key
        self.parent = p
        self.left = l
        self.right = r
class Tree():
    def __init__(self):
        pass

    def binary_tree(self, arr, i):
        if i < 0 or i >= len(arr) or arr[i] == None:
            return

        root = Node(arr[i], None, None, None)
        root.left = self.binary_tree(arr, 2*i)
        root.right = self.binary_tree(arr, 2*i + 1)

        if root.left != None:
            root.left.parent = root

        if root.right != None:
            root.right.parent = root

        return root

    # Task - 1
    def height(self, root):
        if root == None:
            return -1

        return 1 + max(self.height(root.left), self.height(root.right))

    # Task - 2
    def level(self, node):
        if node.parent == None:
            return 0

        return 1 + self.level(node.parent)

    # Task - 3
    def pre_order(self, root):
        if root == None:
            return

        print(root.key, end = ' ')
        self.pre_order(root.left)
        self.pre_order(root.right)

    # Task - 4
    def in_order(self, root):
        if root == None:
            return

        self.in_order(root.left)
        print(root.key, end = ' ')
        self.in_order(root.right)

    #Task - 5
    def post_order(self, root):
        if root == None:
            return

        self.post_order(root.left)
        self.post_order(root.right)
        print(root.key, end = ' ')

    # Task - 6
    def is_same(self, root1, root2):
        if root1 == None and root2 == None:
            return True

        if root1 == None or root2 == None:
            return False

        if root1.key != root2.key:
            return False

        return self.is_same(root1.left, root2.left) and self.is_same(root1.right, root2.right)

    # Task - 7
    def copy(self, root, p = None, left = None):
        if root == None:
            return

        node = Node(root.key, None, None, None)
        node.parent = p

        if left == True:
            p.left = node
        if left == False:
            p.right = node

        self.copy(root.left, node, True)
        self.copy(root.right, node, False)

        return node

#======================================================================
'''                     Tester                        '''      

arr = [None, 10, 5, 7, 17, 9, None, 28]
root = Tree().binary_tree(arr, 1) # creating a tree

#Task - 1:
#print(Tree().height(root))

#Task - 2:
#print(Tree().level(root.right))

#Task - 3:
#print("Pre-order:", end = ' ')
#Tree().pre_order(root)

#Task - 4:
#print("In-order:", end = ' ')
#Tree().in_order(root)

#Task - 5:
#print("Post-order:", end = ' ')
#Tree().post_order(root)

#Task - 6:
#arr1 = [None, 10, 5, 7, 17, 9, None]
#root1 = Tree().binary_tree(arr1, 1)
#same = Tree().is_same(root, root1)
#if same:
#    print("These trees are same.")
#else:
#    print("These trees are not same.")

#Task - 7:
#new_root = Tree().copy(root)
#print(Tree().is_same(root, new_root)) # checking the copied root is same or not
