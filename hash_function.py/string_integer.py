"""
To convert a string into an integer, hashing functions operate on the 
individual characters that make up the string.

Let's use what we know to create a hashing function in Python.

In Python, we can encode strings into their bytes representation with the .encode() 
method (read more here (Links to an external site.)). 
Once encoded, an integer represents each character.

Let's do this with the string hello
"""

bytes_representation = "hello".encode()

for byte in bytes_representation:
    print(byte)

### Print Output
### 104
### 101
### 108
### 108
### 111

"""
Now that we’ve converted our string into a series of integers, 
we can manipulate those integers somehow. We want one number for one string.
For simplicity’s sake, we can use a simple accumulator pattern to get a sum 
of all the integer values.
"""

bytes_representation = "hello".encode()

sum = 0
for byte in bytes_representation:
    sum += byte

print(sum)

### Print Output - map a string to an integer
### 532

"""
Great! We turned a string into a number. 
Now, let's generalize this into a function.
"""

# def my_hashing_func(str):
#     bytes_representation = str.encode()

#     sum = 0
#     for byte in bytes_representation:
#         sum += byte

#     return sum

"""
We aren't done yet 🤪. As shown earlier, hello returns 532. 
But, what if our hash table only has ten slots? 
We have to make 532 a number less than 10 😱.

Remember the modulo operator %? 
We can use that in our hashing function to ensure that the integer 
the function returns is within a specific range.
"""
def my_hashing_func(str, table_size):
    bytes_representation = str.encode()

    sum = 0
    for byte in bytes_representation:
        sum += byte

    return sum % table_size     # will be less than the table size. Within the range of our table size.