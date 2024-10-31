#create package class
import csv
from hash_table import HashTable

# create package list to keep track of packages
package_list = []
# package hash table for accessing package information
package_hash_table = HashTable()

class Package:
    def __init__(self, package_id, address, city, state, zipcode, due, weight, notes, status, truck_id=1, delayed=False):
        self.package_id = package_id
        self.address = address
        if package_id == '9': # TEMPORARY, MUST REMOVE AND ADDRESS LATER
            self.address = '410 S State St'
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.due = due
        self.weight = weight
        self.notes = notes
        self.status = status
        self.truck_id = truck_id
        self.delayed = delayed

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state, self.zipcode, self.due, self.weight, self.notes, self.status, self.truck_id, self.delayed)

# load packages csv data, create package object, and insert into hash table
def load_package_data(file, table):
    with open(file, encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for package in reader:
            package_id = package[0]
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_due = package[5]

            # check if due at EOD and set to 5PM
            if package_due == 'EOD':
                package_due = '5:00 PM'

            package_weight = package[6]
            package_notes = package[7]
            status = "en route"
            truck_id = 1
            # check if must be in truck 2
            if "truck 2" in package_notes:
                truck_id = 2
            if "delayed" or "Wrong address" in package_notes:
                delayed = True

            package_object = Package(package_id, package_address, package_city, package_state, package_zipcode, package_due, package_weight, package_notes, status, truck_id, delayed)
            table.insert(package_id, package_object)
            package_list.append(package_object)


