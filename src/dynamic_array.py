class DynamicArray:
    # my_array = [4] we need an inital size - make an empty array of size 4, NOT a 1 size array with a 4
    def __init__(self, capacity):
        self.capacity = capacity # less ambiguous
        self.count = 0 # length, how many we're using -- starts at zero
        self.storage = [None] * self.capacity  # we need a place to store our actual data. We have to emmulate it. capaacity is the number of empty spots where we can input stuff

    def insert(self, index, value): # need to fill it with something before you can really do anything with it. what 2 parameters do we need? value and place
        # make sure we have open space
        if self.count >= self.capacity:
            # # TODO: Make array dynamically resize
            # print('ERROR: Array is full')
            self.double_size()
            # return

        # make sure index is in range
        if index > self.count:
            print('ERROR: Index out of range')
            return

        # if so, shift everything to right
        # start with the last one, and move it to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        # insert our value
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value) # insert a count

    def double_size(self): # WHEN SHOULD THIS BE CALLED? -- when we try to insert and there is not room 
        self.capacity *= 2 # allocate 
        new_storage = [None] * self.capacity # allocated + made storage for our new array
        for i in range(self.count): 
            new_storage[i] = self.storage[i] # new storage becomes old storage
        self.storage = new_storage # replace old storage with new storage


my_array = DynamicArray(4)
print(my_array.storage)
my_array.insert(0, 1)
my_array.insert(0, 2)
my_array.insert(1, 3)
my_array.insert(3, 4)
my_array.insert(0, 5)
my_array.append(20)
print(my_array.storage)

# [ 2, 3, 1, 4 ]
# After adding double capacity:
# [ 5, 2, 3, 1, 4, 20, None, None ]