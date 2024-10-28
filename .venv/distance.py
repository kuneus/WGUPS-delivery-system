import csv
from hash_table import HashTable

distance_data = []
address_hash_table = HashTable()

# load distance data
def load_distance_data(file, table):
    with open(file, encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        # iterate through each row in csv file
        index = 0
        for row in reader:
            # create a list to hold distance data for each row
            address = []
            # append each column into each row list
            for column in range(1, len(row)):
                # remove the duplicate address string in the first column of each row
                clean_string = row[column].split('\n')[0].strip()
                address.append(clean_string)
            distance_data.append(address)
            # use address as key to find its index in distance list
            table.insert(address[0], index)
            index+=1


# find the distance between 2 addresses using their indexes as input
def find_distance(start_index, destination_index):
    # use indexes to locate in 2d list of distance data
    distance = distance_data[destination_index][start_index + 1]

    if distance == '':
        # switch indexes if empty cell
        distance = distance_data[start_index][destination_index + 1]
    return distance

# find the shortest distance between input address and remaining packages
def find_min_distance(start_address_index, remaining_packages):
    shortest_distance = 100000.0
    destination_address_index = 0

    # loop through each address and record minimum distance
    for package in remaining_packages:
        package_index = address_hash_table.lookup(package.address)

        # check for package with address error
        if package_index is None:
            continue

        current_distance = find_distance(start_address_index, package_index)
        # compare current shortest distance with current distance
        # must be greater than zero to avoid returning same address
        if float(shortest_distance) > float(current_distance) > 0.0:
            shortest_distance = current_distance
            destination_address_index = package_index
    return destination_address_index