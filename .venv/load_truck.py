from distance import *
from package import *
from datetime import datetime, timedelta
from nearest_neighbor import create_route


# calculate time based on miles driven
def calculate_time(current_time, miles, mph):
    miles_to_hours = float(miles / mph)
    new_time = current_time + timedelta(hours=miles_to_hours)
    return new_time

# easier to read format to return time object
def time_obj(time):
    return datetime.strptime(time, '%I:%M %p')

# function to partition packages into the appropriate truck
def load_trucks(packages, trucks):
    to_load = packages
    to_hold = []

    # priority lists
    deadline_9am = []
    deadline_1030am = []
    special_circumstances = []
    group_packages = []

    # identify and add special packages into their respective priority lists
    for package in packages:
        if package.special_circumstances:
            special_circumstances.append(package)

            # add grouped packages
            if package.group_with:
                group_packages += package.group_with

            # add early due time packages
            match package.due.strftime('%I:%M %p'):
                case '09:00 AM':
                    deadline_9am.append(package)
                case '10:30 AM':
                    deadline_1030am.append(package)
                case _:
                    continue # list not needed for 5pm deadline

    # remove duplicates in group packages
    group_packages = list(set(group_packages))

    # loop through packages again to assign special circumstances for packages grouped with others
    for package in packages:
        if int(package.package_id) in group_packages:
            if not package.special_circumstances:
                package.special_circumstances = True
                special_circumstances.append(package)

    # iterate through each truck and partition packages
    for truck in trucks:
        # assign special packages to each truck first
        while len(special_circumstances) > 0 and len(truck.to_deliver) <= truck.capacity:
            # get first item in list
            pkg_obj = special_circumstances.pop(0)
            load = False
            hold = False

            # CONSTRAINT 1: PACKAGE MUST BE ON TRUCK 2
            if int(pkg_obj.truck_id) == 2:
                if int(truck.truck_id) == int(pkg_obj.truck_id):
                    load = True
                else:
                    # if not correct truck, load to hold list
                    hold = True

            # CONSTRAINT 2: PACKAGE IS DELAYED
            elif pkg_obj.delayed:
                if truck.depart_time >= time_obj('09:05 am'):
                    load = True
                else:
                    # load to hold list
                    hold = True

            # CONSTRAINT 3: PACKAGE HAS PRIORITY DEADLINE
            # load 9am package first
            elif pkg_obj.due == time_obj('09:00 AM') and truck.depart_time == time_obj('08:00 AM'):
                load = True
                deadline_9am.remove(pkg_obj)
            # if 9am package hasn't been delivered yet
            elif len(deadline_9am) > 0 and pkg_obj.due == time_obj('10:30 AM'):
                if not pkg_obj.visited:
                    # reload to list if it hasn't been visited
                    special_circumstances.append(pkg_obj)
                    pkg_obj.visited = True
                else:
                    # if it has been visited, load to truck
                    load = True
                    pkg_obj.visited = False
                    deadline_1030am.remove(pkg_obj)
            # load to truck for 10:30 AM packages once 9am package delivered
            elif pkg_obj.due == time_obj('10:30 AM'):
                load = True
                deadline_1030am.remove(pkg_obj)

            # CONSTRAINT 4: PACKAGE MUST BE DELIVERED WITH OTHERS
            # check if item needs to be grouped with others
            # load priority packages first, followed by other packages
            elif int(pkg_obj.package_id) in group_packages:
                if len(truck.group_packages) > 0:
                    load = True
                elif pkg_obj.visited:
                    # hold package if already visited
                    hold = True
                    pkg_obj.visited = False
                else:
                    # reload package to list if not visited
                    special_circumstances.append(pkg_obj)
                    pkg_obj.visited = True

            # load packages to truck or hold
            if load:
                truck.to_deliver.append(pkg_obj)
                to_load.remove(pkg_obj)
                if int(pkg_obj.package_id) in group_packages:
                    truck.group_packages.append(pkg_obj)
            elif hold:
                to_hold.append(pkg_obj)
            # END INNER LOOP

        # reload special packages to list
        for pkg in to_load:
            if pkg.special_circumstances:
                special_circumstances.append(pkg)
        # END OUTER LOOP

    # Load remaining packages
    # use to_load list
    # first make order for truck's current to_deliver list
    # then continue from last package with remaining packages
    create_route(to_load, trucks)






