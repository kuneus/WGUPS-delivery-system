# Name: Kunikazu Nishimura
# Student ID:  011703011

import csv
from package import *
from trucks import *
from distance import *
from nearest_neighbor import *
from load_truck import load_trucks
from user_interface import user_interface
from hash_table import HashTable

# load packages data
load_package_data('./csv/wgups-packages.csv', package_hash_table)

# load distance data
load_distance_data('./csv/wgpus-distances.csv', address_hash_table)

# instantiate trucks
truck_1 = Truck(1, '08:00 AM')
truck_2 = Truck(2, '09:05 AM')
truck_3 = Truck(3, '10:00 AM')
trucks = [truck_1, truck_2, truck_3]


# load packages
load_trucks(package_list, trucks)

for truck in trucks:
    truck_hash_table.insert(truck.truck_id, truck)


user_interface( trucks)