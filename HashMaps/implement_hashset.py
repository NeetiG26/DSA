'''
Implement Hash Set

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

'''

class Bucket:
    def __init__(self):
        self.math_func = []

    def update(self, key):
        found = False
        for i, k in enumerate(self.math_func):
            # print(i,k)
            if key==k:
                self.math_func[i] = key
                found = True
        if not found:
            self.math_func.append(key)

    def remove(self, key):
        for i,k in enumerate(self.math_func):
            if k == key:
                del self.math_func[i]

    def get(self,key):
        # print(self.math_func)
        for k in self.math_func:
            if k == key:
                print("true")
                return True
        print("false")
        return False

class MyHashSet:
    def __init__(self):
        self.key_space = 2096
        self.hash_map = [Bucket() for i in range(self.key_space)]
    
    def _hash_value(self,key):
        hash_key  = key%self.key_space
        return hash_key

    def add(self,key):
        b_index = self._hash_value(key)
        self.hash_map[b_index].update(key)

    def remove(self,key):
        b_index = self._hash_value(key)
        self.hash_map[b_index].remove(key)

    def contains(self,key):
        b_index = self._hash_value(key)
        return self.hash_map[b_index].get(key)


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
# print(obj)
obj.add(3)
# obj.remove(key)
param_3 = obj.contains(3)
# print(obj)
print('param',param_3)