import os
import sys
import string
import random
import argparse

# create a parser object
parser = argparse.ArgumentParser()

# defining a argument for the parser object
parser.add_argument('--size', type=int, help='The size of data you want to store in memory in GB')

# parse the arguments
args = parser.parse_args()

# create an empty dictionary to store your data in
my_data = {}

# generate a random key-value pairs and store them in the dictionary
for i in range(args.size * (10**6)):  
    # create a 1KB data
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    value = os.urandom(1024) # creates a 1KB data
    my_data[key] = value

# check memory usage of the dictionary
print('Memory size of my_data: ', sys.getsizeof(my_data) / (1024**3), 'GB') # prints the size in GB

# keep the program running to keep data in memory
while True:
    pass
