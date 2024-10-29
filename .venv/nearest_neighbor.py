from distance import *
from package import *

# TODO:
# nearest neighbor algo
# create 3 separate lists of packages to deliver of length 16, 16, 8
# instantiate/load trucks using 3 separate lists of packages
# be able to add miles to each truck delivery
# calculate package delivery time based on miles driven + 18mph speed
# abide by constraints

# truck variables that need to be updated during delivery:
# - package status
# - current time
# - delivered and to deliver
# - mileage

def create_route(packages):
    to_deliver = packages
    route = []
    current_address = '4001 South 700 East'
    miles = 0.0

    while len(to_deliver) > 0:
        current_address_index = address_hash_table.lookup(current_address)
        closest_address = find_min_distance(current_address_index, to_deliver)
        next_address_index = closest_address[0] # returns index of next address in to_deliver list
        next_address = to_deliver.pop(next_address_index) # returns package object
        route.append(next_address)
        current_address = next_address.address
        miles = miles + float(closest_address[1])

    print('TOTAL MILES FOR THIS ROUTE: ' + str(miles))
    # TODO: figure out how to add and keep track of mileage
    # TODO: comply with constraints
    # TODO: truck must return to hub after route to load more packages
    return route




# about each route list:
# order of the list determines order of deliveries
# the list contains the package ids of each package
# can find the time of delivery by finding its index in the list,
# then sum up the distances up to that delivery,
# then divide the total distance driven by 18 mph