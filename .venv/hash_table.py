class HashTable:
    # constructor with default initial capacity set at 20
    def __init__(self, initial_capacity=20):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # calculate bucket index and create bucket list where item will be inserted
    def __create_bucket_list(self,key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        return bucket_list

    # insert new item or update its value if it already exists
    def insert(self, key, item):
        bucket_list = self.__create_bucket_list(key)

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_item = [key,item]
        bucket_list.append(key_item)
        return True

    # search for an item using a key and return the item if found, or None if not found
    def search(self,key):
        bucket_list = self.__create_bucket_list(key)

        for kv in bucket_list:
            if kv[0] == key:
                # move most recently searched item to the front
                bucket_list.remove(kv)
                bucket_list.insert(0,kv)
                return kv[1]

        return None

    # remove method an item using a key
    def hash_remove(self,key):
        bucket_list = self.__create_bucket_list(key)

        for kv in bucket_list:
                if kv[0] == key:
                    bucket_list.remove(kv)

    def print_table(self):
        print(self.table)
