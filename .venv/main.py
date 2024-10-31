# Name: Kunikazu Nishimura
# Student ID:  011703011

import csv
from package import *
from trucks import *
from distance import *
from nearest_neighbor import *

# load packages data
load_package_data('./csv/wgups-packages.csv', package_hash_table)

# load distance data
load_distance_data('./csv/wgpus-distances.csv', address_hash_table)

# instantiate trucks
# truck_1 = Truck()

# test nearest neighbor algorithm
final_route = create_route(package_list)
route_1 = final_route[:16]
route_2 = final_route[16:32]
route_3 = final_route[32:]


new_route_1 = create_route(route_1)
new_route_2 = create_route(route_2)
new_route_3 = create_route(route_3)

