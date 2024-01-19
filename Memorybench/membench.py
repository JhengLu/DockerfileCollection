import os
import sys
import string
import random
import argparse
from multiprocessing import Pool, Manager

def store_data(q):
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    value = os.urandom(1024) # creates a 1KB data
    q[key] = value

# create a parser object
parser = argparse.ArgumentParser()

# defining a argument for the parser object
parser.add_argument('--size', type=int, help='The size of data you want to store in memory in GB')

# parse the arguments
args = parser.parse_args()

# create manager object and dictionary
manager = Manager()
my_data = manager.dict()

# specify pool size equal to the number of cores
pool = Pool()

# generate random key-value pairs and store them in the dictionary
for _ in range(args.size * (10**6)):  # multiply size by 10^6 since each data block is 1KB
    pool.apply_async(store_data, args=(my_data,))

pool.close()
pool.join()

# check memory usage of the dictionary
print('Memory size of my_data: ', sys.getsizeof(my_data) / (1024**3), 'GB') # prints the size in GB

# keep the program running to keep data in memory
while True:
    pass
