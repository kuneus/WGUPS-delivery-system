#create package class
import csv
from hash_table import HashTable
from datetime import datetime

# create package list to keep track of packages
package_list = []
# package hash table for accessing package information
package_hash_table = HashTable()

class Package:
    def __init__(self, package_id, address, city, state, zipcode, due, weight, notes, status, truck_id=1, group_with=None,
                 delayed=False, wrong_address=False, special_circumstances=False):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.due = due
        self.weight = weight
        self.notes = notes
        self.status = status
        self.truck_id = truck_id
        self.group_with = group_with
        self.delayed = delayed
        self.wrong_address = wrong_address
        self.special_circumstances = special_circumstances
        self.delivered_at = None
        self.visited = False

    def __str__(self):
        return ('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' %
                (self.package_id, self.address, self.city, self.state, self.zipcode, self.due, self.weight,self.notes,
                 self.status, self.truck_id, self.group_with, self.delayed, self.wrong_address,
                 self.special_circumstances))

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
            # format due time with time object
            package_due = datetime.strptime(package_due, '%I:%M %p')

            package_weight = package[6]
            package_notes = package[7]
            status = "at hub"
            truck_id = 1

            group_with = []
            # check if package must be grouped with other packages
            if 'delivered with' in package_notes:
                package_1 = package_notes[23:25]
                package_2 = package_notes[26:]
                group_with.append(int(package_1))
                group_with.append(int(package_2))

            # instantiate package object
            pkg_obj = Package(package_id, package_address, package_city, package_state, package_zipcode, package_due, package_weight, package_notes, status, truck_id, group_with )

            # check if must be in truck 2
            if 'truck 2' in pkg_obj.notes:
                pkg_obj.truck_id = 2

            # check if delayed or wrong address
            if 'Delayed' in pkg_obj.notes:
                pkg_obj.delayed = True
                pkg_obj.truck_id = 2
            if 'Wrong address' in pkg_obj.notes:
                pkg_obj.wrong_address = True

            # check if package has special circumstances: delayed, wrong address, priority, truck 2, or grouped with others
            if pkg_obj.delayed or pkg_obj.wrong_address or pkg_obj.due < datetime.strptime('05:00 PM', '%I:%M %p') or pkg_obj.truck_id == 2 or len(pkg_obj.group_with) > 0:
                pkg_obj.special_circumstances = True

            table.insert(package_id, pkg_obj)
            package_list.append(pkg_obj)


