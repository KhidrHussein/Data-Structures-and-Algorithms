class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        """This method generates indexes based on the mod of the summation of all the ASCII characters of the key"""
        h = 0
        for char in key:
            h += ord(char)  # ord returns the ASCII value of any character
        return h % self.MAX  # assuming the size of the list is 100

    def __setitem__(self, key, value):       # __setitem__ is a python operator that allows us to give values
        h = self.get_hash(key)       # in the standard dictionary format i.e: HashTableObject["key"] = value
        self.arr[h] = value

    def __getitem__(self, item):                     # __getitem__ is a python operator that allows us to give values
        h = self.get_hash(item)              # in the standard dictionary format i.e: HashTableObject["key"]
        return self.arr[h]


t = HashTable()
t["march 6"] = 302
print(t["march 6"])


