class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """
        There are diferent types of hashing techniques to use in hash function.They are :- 1) K mod 10
                                                                                           2) K mod size_of_the_hashtable(n)
                                                                                           3) Mid square folding method
        
        But here i used pythons built-in function hash and take modulo with the size of the table.
        This ensures the index value falls in table size range.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])

    def delete(self, key):
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return True
        return False

    def lookup(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None


