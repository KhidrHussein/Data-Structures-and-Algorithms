class HashTable:
    """A hash table is basically a dictionary in python terms, so the creation of this class is not necessary in
    practical terms"""
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]  # each item in the initial array is an empty list, this enables
        # chaining as a form of collision handling

    def get_hash(self, key):
        """This method generates indexes based on the mod of the summation of all the ASCII characters of the key"""
        h = 0
        for char in key:
            h += ord(char)  # ord returns the ASCII value of any character
        return h % self.MAX  # assuming the size of the list is 100

    def __setitem__(self, key, value):  # __setitem__ is a python operator that allows us to give values
        h = self.get_hash(key)  # in the standard dictionary format i.e: HashTableObject["key"] = value
        found = False
        for idx, element in enumerate(self.arr[h]):    # we check to see if the key already exists, if it does then we
            if len(element) == 2 and element[0] == key:  # change the value of the arr at that index to the new value
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:                   # if the key doesn't exist, then we append a tuple containing the key value pair
            self.arr[h].append((key, value))  # to the list existing at that index

    def __getitem__(self, key):  # __getitem__ is a python operator that allows us to give values
        h = self.get_hash(key)  # in the standard dictionary format i.e: HashTableObject["key"]

        for element in self.arr[h]:  # we iterate through the list at the location of the index and return the value of
            if element[0] == key:    # the key
                return element[1]

    def __delitem__(self, key):  # __delitem__ allows us to implement the del keyword to delete a key value
        h = self.get_hash(key)  # pair with the key
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashTable()
t["march 6"] = 302
print(t["march 6"])

del t["march 6"]
print(t["march 6"])
