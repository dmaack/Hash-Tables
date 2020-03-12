import hashlib

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity # allocating memory with python list


    def _hash(self, key): # what does the leading underscore mean? Dont use it outside the class, private
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        # hash = 5381
        # for k in key:
        #     hash = (hash * 33) + ord(k)
   
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # hash = 5381
        # for k in key:
        #     hash = (hash * 33) + ord(k)
        # return hash
        pass


    def _hash_mod(self, key): # calls hash and returns 
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value): 
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # index = self._hash_mod(key) # need to find the index, take the key and turn it into the index of our array

        # if self.storage[index] is not None: # if the index is full give an error
        #     print('ERROR: Key in use')
        # else: # otherwise, the index becomes our value 
        #     self.storage[index] = value


        # accepts a key and value
        # hash the key
        # stores the key-value pair in the hash table via separate chaining (nested structure)
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            current = self.storage[index]
            while current:
                if current.key == key:
                    current.value = value
                    break
                if current.next is not None:
                    current = current.next
                else:
                    break
            current.next = LinkedPair(key, value)
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)

        # if self.storage[index] is not None: # if there is an index in our storage
        #     self.storage[index] = None # then remove it / make it none
        # else:
        #     print('ERROR: Key not found')

        index = self._hash_mod(key)
        current = self.storage[index]

        if current is None:
            print('ERROR: Key not found')
        
        while current.key is not key:
            if current.next is None:
                print('ERROR: Key is not found')
                return
            current = current.next

        current.value = None
                


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)

        # return self.storage[index] # return storage at the index, nothing is there already so dont 'have' to handle none conditional

        index = self._hash_mod(key)
        

        if self.storage[index] is not None:
            current = self.storage[index]

            while True:
                if current.key == key:
                    return current.value
                elif current.next is not None:
                    current = current.next
                else:
                    return None
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # old_storage = self.storage.copy()
        # self.capacity = self.capacity * 2 # double the capacity
        # self.storage = [None] * self.capacity

        # for bucket_item in old_storage:
        #     self.insert(bucket_item.key, bucket_item.value)
        old_storage = self.storage[:]
        self.capacity *= 2
        self.storage = [None] * self.capacity
        
        for bucket_item in old_storage:
            if bucket_item is not None:
                current = bucket_item
                while current:
                    self.insert(current.key, current.value)
                    current = current.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
'''
Linked List hash table key/value pair
'''

'''
Linked List hash table key/value pair
'''

