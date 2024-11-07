# Name: Kunikazu Nishimura
# Student ID:  011703011

import csv
from package import *
from trucks import *
from distance import *
from nearest_neighbor import *
from load_truck import load_trucks

# load packages data
load_package_data('./csv/wgups-packages.csv', package_hash_table)

# load distance data
load_distance_data('./csv/wgpus-distances.csv', address_hash_table)

# instantiate trucks
truck_1 = Truck(1, '08:00 AM')
truck_2 = Truck(2, '09:05 AM')
truck_3 = Truck(3, '10:00 AM')
trucks = [truck_1, truck_2, truck_3]

# test nearest neighbor algorithm
# final_route = create_route(package_list, trucks)

# load packages
load_trucks(package_list, trucks)

for truck in trucks:
    print('------------------------------------------------------------')
    print('TRUCK #%s, Length of deliver list: %s, total miles: %s, current time: %s' % (truck.truck_id, len(truck.to_deliver), truck.miles, truck.current_time))
    for package in truck.to_deliver:
        print('Package ID: %s, address: %s, due: %s, delayed: %s, special circumstances: %s, notes: %s' % (package.package_id, package.address, package.due.strftime('%I:%M %p'), package.delayed, package.special_circumstances, package.notes))

# for truck in final_route:
#     for package in truck:
#         print('ID: %s, Address: %s, Due at: %s, Delivered at: %s, Delivered on Truck %s' % (package.package_id, package.address, package.due, package.delivered_at, package.truck_id))
#
