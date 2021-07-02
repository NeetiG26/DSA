'''
Design Hashmap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
'''

class Bucket:
    def __init__(self):
        self.bucket = []

    def add(self, key, value):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key,value)
                return            
        self.bucket.append((key,value))

    def give(self, key):
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        for i, (k,v) in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]


class MyHashMap:
    def __init__(self):
        self.key_space = 196
        self.hash_map = [Bucket() for i in range(self.key_space)]

    def put(self, key,value):
        hash_value = key%self.key_space
        self.hash_map[hash_value].add(key,value)

    def get(self, key):
        hash_value = key%self.key_space
        return self.hash_map[hash_value].give(key)

    def remove(self, key):
        hash_value = key%self.key_space
        self.hash_map[hash_value].remove(key)


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(3,4)
param_2 = obj.get(3)
print(param_2)
obj.remove(3)