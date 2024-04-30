class Array:
    def __init__(self,size,data_type):
        self.data_type = data_type
        self.size = size
        self.arr = [None]*self.size

    def insert(self,index,data):
        if not isinstance(data, self.data_type):
            raise TypeError("Invalid data type. Expected: {}, Got: {}".format(self.data_type, type(data)))
        if len(self.arr)<= self.size:
            self.arr[index] = data
            return
        print("The array is full.")
        return
    
    def remove(self, index):
        if index < 0 or index >= len(self.arr):
            print("Index out of range")
            return
        else:
            self.arr.pop(index)

    def search(self,element):
        if self.arr:
            for i in enumerate(self.arr):
                if i == element:
                    return self.arr.index(element)
        print("Array is empty")

    def update(self, index, data):
        if not isinstance(data, self.data_type):
            raise TypeError("Invalid data type. Expected: {}, Got: {}".format(self.data_type, type(data)))
        if index < 0 or index >= len(self.arr):
            print("Index out of range")
            return
        self.arr[index] = data

    def sorting(self):
        self.arr.sort()

    def merge(self, lst):
        for item in lst:
            if not isinstance(item, self.data_type):
                raise TypeError("Invalid data type. Expected: {}, Got: {}".format(self.data_type, type(item)))
        if len(self.arr) + len(lst) > self.size:
            print("Arrays size exceeds the limit")
            return
        self.arr += lst
    
    def split(self,index):
        if index < 0 or index >= len(self.arr):
            print("Index out of range")
            return None,None
        else:
            return self.arr[:index],self.arr[index:]
        
    def display(self):
        for i in self.arr:
            print(i,end= " ")

    def reverse(self):
        i = 0
        while i < self.size//2:
            self.arr[i],self.arr[self.size-i-1]= self.arr[self.size-i-1],self.arr[i]
            i = i+1
