

class HashTable:

    def __init__(self, size):
        self.size = size
        self.hashtable = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hashtable[hashed_key]
        found_key = False
        for count, ele in enumerate(bucket):
            if key == ele[0]:
                found_key = True
                index = count

        if found_key:
            bucket[index] = (key,value)
        else:
            bucket.append((key,value))


    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hashtable[hashed_key]
        for _, ele in enumerate(bucket):
            if key == ele[0]:
                return ele[1]


    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hashtable[hashed_key]
        found_key = False
        for count, ele in enumerate(bucket):
            if key == ele[0]:
                found_key = True
                index = count

        if found_key:
            bucket.pop(index)


    def __str__(self):
        print(self.hashtable)
        return "hello"



hash_table = HashTable(5)

# insert some values
hash_table.set_val('gfg@example.com', 'some value')
hash_table.set_val("2","2")
print(hash_table)
print()

hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()

# search/access a record with key
print(hash_table.get_val('portal@example.com'))
print(hash_table.get_val('gfg@example.com'))
print()

# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)