from distance import *
from package import *
from datetime import datetime, timedelta

# calculate time based on miles driven
def calculate_time(current_time, miles, mph):
    miles_to_hours = float(miles / mph)
    new_time = current_time + timedelta(hours=miles_to_hours)
    return new_time

# easier to read format to return time object
def time_obj(time):
    return datetime.strptime(time, '%I:%M %p')

def create_route(packages, trucks):
    # list to hold remaining packages to be delivered
    remaining_packages = packages
    # list to hold wrong package(s)
    wrong_address_packages = []

    # iterate through each truck and create its route
    for truck in trucks:
        # temporary list to hold special packages currently in truck
        special_packages = truck.to_deliver.copy()
        truck.to_deliver.clear()

        # set last truck time based on when 1st truck returns
        if truck == trucks[len(trucks) - 1]:
            truck.current_time = trucks[0].current_time
            truck.depart_time = trucks[0].current_time

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
        if truck.truck_id == 1:
            truck.return_to_hub()
        ## END TRUCK FOR LOOP ##



