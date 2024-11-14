# Name: Kunikazu Nishimura
# Student ID:  011703011

import csv
from package import package_hash_table, package_list
from trucks import *
from distance import *
from nearest_neighbor import *
from load_truck import load_trucks
from user_interface import user_interface
from hash_table import HashTable


class Main:
    # load packages data
    load_package_data('./csv/wgups-packages.csv', package_hash_table)

    # load distance data
    load_distance_data('./csv/wgpus-distances.csv', address_hash_table)

    # load packages onto trucks
    load_trucks(package_list, trucks)

    # start main program
    user_interface(trucks)