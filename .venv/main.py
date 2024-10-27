# Name: Kunikazu Nishimura
# Student ID:  011703011

import csv
from package import load_package_data
from hash_table import HashTable
from distance import *

# create hash table for packages and load packages data
package_hash_table = HashTable()
load_package_data('./csv/wgups-packages.csv', package_hash_table)
package_hash_table.print_table()
print(package_hash_table.lookup('32'))

# create hash table for distances and load distance data
address_hash_table = HashTable()
load_distance_data('./csv/wgpus-distances.csv', address_hash_table)

# test address data and functions
address_1 = address_hash_table.lookup('4001 South 700 East')
address_2 = address_hash_table.lookup('1330 2100 S')

print(find_min_distance(address_1))