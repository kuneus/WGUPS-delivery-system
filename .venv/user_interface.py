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
    # if time is later than delivery time
    if time_input >= pkg_obj.delivered_at:
        pkg_obj.status = 'Delivered'
    # if time is later than depart time but before delivery time
    elif time_input >= truck_obj.depart_time:
        pkg_obj.status = 'En route'
    else:
    # if time is before depart time
        pkg_obj.status = 'At hub'
    return pkg_obj.status

def print_output_line(truck_obj, pkg_obj, time_obj, truck_info=False):
    # determine package status by calculating delivery time and comparing it to input time
    status = calculate_package_status(truck_obj, pkg_obj, time_obj)
    # change time to string format
    input_time_str = time_obj.strftime('%I:%M %p')

    if not truck_info:
        print('%s| %s| %s| %s' % (input_time_str.ljust(10), pkg_obj.package_id.ljust(11), status.ljust(11),
                                                    pkg_obj.delivered_at.strftime('%I:%M %p')))
    else:
        # add truck ID if requested in arguments
        print('%s| %s| %s| %s| %s' % (input_time_str.ljust(10), pkg_obj.package_id.ljust(11), status.ljust(11),
                                             pkg_obj.delivered_at.strftime('%I:%M %p').ljust(14), pkg_obj.truck_id))

# display status of a single package or specific packages
def display_single_package(time_obj):
    print('Please input the package ID or multiple IDs separated by commas: ')

    # run do-while loop until user inputs valid package ID
    while True:
        package_id = input()

        #  split into a list of IDs
        package_ids = package_id.split(',')
        # keep track of valid and invalid inputs
        valid_list = []
        invalid_list = []

        # check each input and separate into valid and invalid IDs
        for single_id in package_ids:
            # remove any white space
            single_id = single_id.strip()
            # find if package id exists
            pkg_obj = package_hash_table.lookup(single_id)
            if pkg_obj:
                valid_list.append(pkg_obj)
            else:
                invalid_list.append(single_id)

        # exit loop if no invalid inputs
        if len(invalid_list) == 0:
            break
        else:
        # List invalid inputs and enter loop again
            invalid_str_list = ','.join(invalid_list)
            print('Invalid package ID: %s. Please try again with a valid package ID.' % invalid_str_list)

    # print header
    print('%s| PACKAGE ID | %s| DELIVERY TIME | TRUCK ID' % ('TIME'.ljust(10), 'STATUS'.ljust(11)))
    for pkg_obj in valid_list:
        # find which truck the package will be delivered in
        pkg_truck_id = pkg_obj.truck_id
        truck_obj = truck_hash_table.lookup(pkg_truck_id)
        # print status of each package input
        print_output_line(truck_obj, pkg_obj, time_obj, True)

# display status of all packages in each truck
def display_all_statuses(trucks, time_input):
    time_str = time_input.strftime('%I:%M %p')
    for truck in trucks:
        print()
        print('          Truck %s Status Info at %s          ' % (truck.truck_id, time_str))
        print('%s| %s| %s| DELIVERY TIME' % ('TIME'.ljust(10), 'PACKAGE ID'.ljust(11), 'STATUS'.ljust(11)))
        for pkg in truck.to_deliver:
            print_output_line(truck, pkg, time_input)

# find miles for each truck and calculate and display all miles
def display_all_mileage(trucks, time_input):
    total_miles = 0
    alt_miles = 0
    # print header with fixed length strings
    print('%s| %s| %s| %s| PACKAGES' % ('TRUCK ID'.ljust(9), 'DEPART TIME'.ljust(12), 'CURRENT MILES'.ljust(14),
                                        'CURRENT LOCATION'.ljust(40)))
    for truck in trucks:
        # # calculate total miles from all trucks
        # total_miles += round(truck.miles, 2)

        # get truck info
        truck_depart_time = truck.depart_time.strftime('%I:%M %p')
        truck_info = truck.get_info(time_input)
        current_miles = round(truck_info[0], 2)

        # calculate total miles from all trucks
        total_miles += round(current_miles, 2)

        current_address = truck_info[1]
        truck_package_ids = truck.get_packages()

        # print output with fixed length strings
        print('%s| %s| %s| %s| %s' % (str(truck.truck_id).ljust(9), truck_depart_time.ljust(12),
                                      str(current_miles).ljust(14), current_address.ljust(40), truck_package_ids))

    print('TOTAL    | %.1f miles' % total_miles)

def user_interface( trucks):
    # welcome message
    print('---------------------------------------------------------------')
    print('------------------     Welcome to WGUPS!     ------------------')
    print('---------------------------------------------------------------')

    # run loop of user interface program until user quits
    while True:
        print("Please input one of the following options: \n"
                         " '1' to view the status of a specific package, \n "
                         "'2' to view the status of all packages, \n"
                         " '3' to view total miles by all trucks, \n"
                         "  or 'q' to quit the program:  ")

        response = input()

        # quit program
        if response == 'q':
            break

        current_time_obj = None
        # run do-while loop until user inputs valid time format
        while response == '1' or '2' or '3':
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
            display_all_mileage(trucks, current_time_obj)
        else:
            print('Invalid input. Try again.')
        print('---------------------------------------------------------------')
        # END WHILE LOOP
    print('Exiting program')
