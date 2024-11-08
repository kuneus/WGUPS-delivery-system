from load_truck import time_obj
from datetime import datetime

# user must be able to
# 1. view the delivery status of any package at any time
# 2. view the total mileage traveled by all trucks

# main function should act as a loop until the user quits
# options:
#   view delivery status of specific or all packages
#   view mileage of all trucks
#   exit program

# check if time input is valid
def validate_time(time_str, time_format):
    try:
        datetime.strptime(time_str, time_format)
        return True
    except ValueError:
        return False

# view delivery status function
# - input parameter: time
# - return status of specific or total packages and estimated delivery time
def user_interface(package_hash_table, truck_hash_table):
    # welcome message
    print('---------------------------------------------------------------')
    print('------------------     Welcome to WGUPS!     ------------------')
    print('---------------------------------------------------------------')

    response = input("Type '1' to view the status of a specific package, '2' to view the status of all packages, or 'q' to quit the program:  ")

    while response != 'q':
        if response == '1':
            # run do-while loop until user inputs valid package ID
            print('Please input the package ID: ')
            while True:
                package_id = input()
                pkg_obj = package_hash_table.lookup(package_id)
                if pkg_obj:
                    break
                else:
                    print('Invalid package ID. Please try again with a valid package ID.')

            # find which truck the package will be delivered in
            pkg_truck_id = pkg_obj.truck_id
            truck_obj = truck_hash_table.lookup(pkg_truck_id)
            print('Package will be delivered in Truck %s' % truck_obj.truck_id)

            # run do-while loop until user inputs valid time format
            while True:
                print('Input time to view status in HH:MM AM/PM format:  ')
                time = input()
                time_format = '%I:%M %p'
                if validate_time(time, time_format):
                    current_time_obj = time_obj(time)
                    break
                else:
                    print('Invalid time format.')

            print('Package ID: %s, address: %s, delivered at: %s, status: %s' % (
                pkg_obj.package_id, pkg_obj.address, pkg_obj.delivered_at, pkg_obj.status))

            # compare input time to package's delivered at time
            # if input time greater than package's delivered time, then status = delivered
            # if less than, status = en route or on hub
            # to determine if en route, find truck's depart time
            # if depart time less than input time, status = en route
            # if depart time greater than input time, status = at hub

            print('At %s, package %s is currently ' % (current_time_obj, package_id))
        elif response == '2':
            print('Input time to view stat®us in HH:MM AM/PM format:  ')
            time = input()
            print('Here are all the packages: ')
            # iterate through each package on each truck
            # generate status based on input time and delivered at time
        else:
            print('Invalid input. Please put 1, 2, or q only.')
            response = input()
            continue
        print('Request complete. Press 1 or 2 to resume search or q to quit program.')
        response = input()

    print('Exiting program')
