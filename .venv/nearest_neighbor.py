from distance import *
from package import *
from datetime import datetime, timedelta

# truck variables that need to be updated during delivery:
# - package status
# - current time
# - delivered and to deliver
# - mileage

# calculate time based on miles driven
def calculate_time(current_time, miles, mph):
    miles_to_hours = float(miles / mph)
    new_time = current_time + timedelta(hours=miles_to_hours)
    return new_time

# easier to read format to return time object
def time_obj(time):
    return datetime.strptime(time, '%I:%M %p')

def create_route(packages, trucks):
    remaining_packages = packages
    wrong_address_packages = []

    # iterate through each truck and create its route
    for truck in trucks:
        # temporary list to hold special packages currently in truck
        special_packages = truck.to_deliver.copy()
        truck.to_deliver.clear()

        # set last truck time based on when 1st truck returns
        if truck == trucks[len(trucks) - 1]:
            truck.current_time = trucks[0].current_time

        # iterate until truck reaches capacity or all remaining packages have been assigned
        while truck.capacity > len(truck.to_deliver) and len(remaining_packages) > 0 :
            # get index of current address and find nearest address
            current_address_index = address_hash_table.lookup(truck.address)

            # add package with wrong address to remaining packages list after 10:20 AM
            if truck.current_time >= time_obj('10:20 AM') and wrong_address_packages:
                wrong_address = wrong_address_packages.pop(0)
                remaining_packages.append(wrong_address)

            # determine which list to take from, starting with special packages first
            if len(special_packages) > 0:
                current_delivery_list = special_packages
            else:
            # if no more special packages, begin taking from remaining packages
                current_delivery_list = remaining_packages

            # find the closest address from current location out of chosen list
            closest_address = find_min_distance(current_address_index, current_delivery_list)

            # get index of closest address
            next_address_index = closest_address[0]

            # remove package object from list and set as variable
            next_address = current_delivery_list.pop(next_address_index)

            if next_address.wrong_address:
                if truck.current_time >= time_obj('10:20 AM'):
                    next_address.address = '410 S State St'
                    next_address.wrong_address = False
                    remaining_packages.append(next_address)
                else:
                    wrong_address_packages.append(next_address)
                continue

            # add mileage and calculate current time
            miles_to_add = closest_address[1]
            truck.current_time = calculate_time(truck.current_time, float(miles_to_add), truck.speed)

            # update truck info and package info
            truck.address = next_address.address
            truck.miles+= float(miles_to_add)
            next_address.truck_id = truck.truck_id
            next_address.delivered_at = truck.current_time

            # finally place package into truck
            truck.to_deliver.append(next_address)

            ## END DELIVERY WHILE LOOP ##

        # return truck to hub
        truck.return_to_hub()
        ## END TRUCK FOR LOOP ##

# about each route list:
# order of the list determines order of deliveries
# the list contains the package objects
# can find the time of delivery by finding its index in the list,
# then sum up the distances up to that delivery,
# then divide the total distance driven by 18 mph

# ASSUMPTIONS:
#     truck capacity of 16
#     average speed 18mph
#     earliest time to leave 8am
#
#
# CONSTRAINT CONDITIONALS LOGICAL PRIORITY:
#     1. Check if package must be delivered on truck 2
#     2. Check if package needs to be delivered with others in same truck
#     3. Check if package has priority deadline
#     4. Check if package is delayed
#
# CONSTRAINTS SUMMARY:
#     Package pairs: (14, 15, 19) , (13, 16, 19) , ( 13, 15, 20)
#     Delayed packages: (6, 9:05am), (9, 10:20am), (25, 9:05am), (27, 9:05am) , (32, 9:05am)
#     Package truck 2 only: 3, 18, 36, 38
#     Deadlines:
#         9:00am : [15]
#         10:30 am : [1, 6, 13, 14, 16, 20, 25, 29, 30, 31, 34, 37, 40]
#         EOD



