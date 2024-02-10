class Node:
    def __init__(self,item = None, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self,root = None):
        self.root =  root

# insert an item to the tree....
    def insertItem(self,data):
        self.root = self.rinsert(self.root,data)
# rrecursive func. for insert an item to the tree....
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        elif data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data > root.item:
            root.right = self.rinsert(root.right,data)
        return root
    
# search an item in the tree....
    def search(self,data):
        self.root = self.rsearch(self.root,data)
# recursive function for search an item in the tree....
    def rsearch(self,root,data):
        if root is None or data == root.item:
            return root
        elif data < root.item:
            return self.rsearch(root.left,data)
        elif data > root.item:
            return self.rsearch(root.right,data)
    
# inorder travesel in the tree....
    def inorder(self):
        result = []
        self.root = self.rinorder(self.root,result)
# recursive function inorder travesel in the tree....
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.left,result)

# preorder travesel in the tree....
    def preorder(self):
        result = []
        self.root = self.rpreorder(self.root,result)
# recursive function preorder travesel in the tree....
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.left,result)

# postorder travesel in the tree....        
    def postorder(self):
        result = []
        self.root = self.rpostorder(self.root,result)
# recursive function postorder travesel in the tree....        
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.left,result)
            result.append(root.item)
    
    