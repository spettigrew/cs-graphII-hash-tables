class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys. Basic hash table class
    """

    def __init__(self, capacity):   # capacity - how big the hash table will be
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity    # store all of our values for the hash table that is set to an empty array
        self.item_count = 0 # count the numbers of in our hash table. 

    def get_num_slots(self):    # how many slots are in our self.storage
        """
        Return the length of the list you're using to hold the hash table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        """
        return len(self.storage)    #return the length of that storage

    def djb2(self, key):    #common hashing function that returns a number
        """
        DJB2 hash, 32-bit
        """
        # Cast the key to a string and get bytes
        str_key = str(key).encode()

        # Start from an arbitrary large prime
        hash_value = 5381

        # Bit-shift and sum value for each character
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits

        return hash_value

    def hash_index(self, key):  # giving a key, turn it into an index in our array
        """
        Take an arbitrary key and return a valid integer index within the hash table's storage capacity.
        """
        return self.djb2(key) % self.capacity #modolo the returned the keyed string

"""
The put Method
Let's create our put function. Before we code, let's break down what needs to happen:

Given a key and a value, insert the respective value into a hash table array using the hashed key to determine the storage location index.
Let's think about what we need to do:

Hash the key into an index using the hash function
Put the value into that index
First, let's call the hash function and store the return value in index:
Next, let's insert the value at that index:
"""

def put(self, key, value):  #put values in the key:value pair
    """
    Store the value with the given key.
    """
    index = self.hash_index(key)    #turns key into an index within our hash-table array 
    self.storage[index] = value # put value in the corresponding index that maps with our key
    return

"""
The delete Method
Next, let's write our delete method. 
What does this method need to do? 
We can think about it as the inverse of the put method that we just defined. 
The function will receive a key as its input, 
then pass that key through the hash function to get the index where the hash table's value needs to be deleted.

Let's start by getting the index by passing the key through the hashing function:
Next, we need to delete the value from that index in our storage by setting it to None.
"""

def delete(self, key):
    """
    Remove the value stored with the given key.
    Print a warning if the key is not found.
    """
    index = self.hash_index(key)    # index of where the value of the key is stored
    self.storage[index] = None   #remove the value at the index in the array

"""
The get Method
The last method we need to deal with is our get method. 
get is a simple method that retrieves the value stored at a specific key. 
The function needs to receive a key as an input, pass that key through the hashing function to find the index where the value is stored, 
and then return the value at that index.

Let's start by getting the index from the key:
Next, we need to return the value that is stored at the index.
"""

def get(self, key):
    """
    Retrieve the value stored with the given key.
    Returns None if the key is not found.
    """
    index = self.hash_index(key)
    return self.storage[index]
