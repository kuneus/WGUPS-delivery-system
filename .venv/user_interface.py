from load_truck import time_obj
from datetime import datetime
from package import package_hash_table
from trucks import truck_hash_table

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

# display status of a single package
def display_single_package(time_obj):
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

    # determine package status by calculating delivery time and comparing it to input time
    status = calculate_package_status(truck_obj, pkg_obj, time_obj)
    time_str = time_obj.strftime('%I:%M %p')
    print('At %s, package %s status: %s' % (time_str, pkg_obj.package_id, status))

# display status of all packages in each truck
def display_all_statuses(trucks, time_input):
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

# find miles for each truck and calculate and display all miles
def display_all_mileage(trucks):
    total_miles = 0
    print('Truck ID ----- Miles')
    for truck in trucks:
        total_miles += round(truck.miles, 2)
        print('%s ------------ %.1f' % (truck.truck_id, truck.miles))
    print('Total miles: %.1f' % total_miles)

def user_interface( trucks):
    # welcome message
    print('---------------------------------------------------------------')
    print('------------------     Welcome to WGUPS!     ------------------')
    print('---------------------------------------------------------------')

    # run loop of user interface program until user quits
    while True:
        response = input("Please input one of the following options: \n"
                         " '1' to view the status of a specific package, \n "
                         "'2' to view the status of all packages, \n"
                         " '3' to view total miles by all trucks, \n"
                         "  or 'q' to quit the program:  ")

        # quit program
        if response == 'q':
            break

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

        # view status of a specific package
        if response == '1':
            display_single_package(current_time_obj)
        elif response == '2':
            # display status of all packages in each truck
            display_all_statuses(trucks, current_time_obj)
        elif response == '3':
            # display mileage of each truck and total mileage
            display_all_mileage(trucks)
        else:
            print('Invalid input. Try again.')
        print('---------------------------------------------------------------')
        # END WHILE LOOP
    print('Exiting program')
