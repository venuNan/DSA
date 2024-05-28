class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Singlylinkedlist:
    def __init__(self) -> None:
        self.head = None

    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
    
    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end="-->")
            temp = temp.next

obj = Singlylinkedlist()
obj.insert(5)
obj.insert(6)
obj.insert(7)
obj.insert(8)
obj.insert(9)
obj.insert(10)
obj.print()