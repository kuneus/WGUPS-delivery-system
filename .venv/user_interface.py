from load_truck import time_obj
from datetime import datetime
from package import package_hash_table

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

# determine status of package
def calculate_package_status(truck_obj, pkg_obj, time_input):
    if time_input >= pkg_obj.delivered_at:
        pkg_obj.status = 'Delivered'
    elif time_input >= truck_obj.depart_time:
        pkg_obj.status = 'En route'
    else:
        pkg_obj.status = 'At hub'
    return pkg_obj.status

def display_all_packages(trucks, time_input):
    time_str = time_input.strftime('%I:%M %p')
    for truck in trucks:
        print('--------------------- Truck %s Status Info at %s---------------------' % (truck.truck_id, time_str))
        # next = get status
        print('Package ID ----- Status')
        for pkg in truck.to_deliver:
            id_str = pkg.package_id
            # add 0 in front of single digit numbers for consistent spacing
            if int(pkg.package_id) < 10:
                id_str = '0' + pkg.package_id
            print('%s ------------- %s' % (id_str, calculate_package_status(truck, pkg, time_input)))


def user_interface( truck_hash_table, trucks):
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

            status = calculate_package_status(truck_obj,pkg_obj,current_time_obj)
            time_str = current_time_obj.strftime('%I:%M %p')
            print('At %s, package %s status: %s' % (time_str, pkg_obj.package_id, status))
        elif response == '2':
            # print('Input time to view status in HH:MM AM/PM format:  ')
            # time = input()
            #
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

            display_all_packages(trucks, current_time_obj)

        else:
            print('Invalid input. Please put 1, 2, or q only.')
            response = input()
            continue
        print('Request complete. Press 1 or 2 to resume search or q to quit program.')
        response = input()

    print('Exiting program')
