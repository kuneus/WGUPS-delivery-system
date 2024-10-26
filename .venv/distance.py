import csv
from hash_table import HashTable

distance_data = []

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


# find the distance between 2 addresses
# def find_distance(start, destination):

address_table = HashTable()
load_distance_data('./csv/wgpus-distances.csv', address_table)

for i in range (len(distance_data)):
    print(distance_data[i])

print(distance_data)