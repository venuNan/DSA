class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, root: Node, data: int) -> Node:
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        elif data >= root.data:
            root.right = self.insert(root.right, data)
        return root

    def preorder(self, root: Node) -> None:
        if root is None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self, root: Node) -> None:
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")
    
    def inorder(self, root: Node) -> None:
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)

    def levelorder(self,root:Node) -> None:
        lst = [root]
        while len(lst)>0:
            for i in range(len(lst)):
                x = lst.pop(0)
                print(x.data,end=" ")
                if x.left is not None:
                    lst.append(x.left)
                if x.right is not None:
                    lst.append(x.right)
                


obj = BST()
obj.root = obj.insert(obj.root, 1)
obj.root = obj.insert(obj.root, 2)
obj.root = obj.insert(obj.root, 3)
obj.root = obj.insert(obj.root, 4)
obj.root = obj.insert(obj.root, 5)
obj.root = obj.insert(obj.root, 6)
obj.root = obj.insert(obj.root, 7)
obj.root = obj.insert(obj.root, 8)
obj.root = obj.insert(obj.root, 9)
obj.root = obj.insert(obj.root, 10)

print("Preorder: ",end=" ")
obj.preorder(obj.root)
print("\n")
print("Postorder: ",end=" ")
obj.postorder(obj.root)
print("\n")
print("Inorder: ",end=" ")
obj.inorder(obj.root)
print("\n")
print("levelorder: ",end=" ")
obj.levelorder(obj.root)