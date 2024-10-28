# Name: Kunikazu Nishimura
# Student ID:  011703011

import csv
from package import *
from hash_table import HashTable # remove after testing
from distance import *

# load packages data
load_package_data('./csv/wgups-packages.csv', package_hash_table)

# load distance data
load_distance_data('./csv/wgpus-distances.csv', address_hash_table)

# test address data and functions
address_1 = address_hash_table.lookup('4001 South 700 East')
closest_neighbor_test_2 = str(find_min_distance(address_1, package_list))
print('index of closest address using method 2: ' + closest_neighbor_test_2)