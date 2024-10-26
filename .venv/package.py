#create package class
import csv

class Package:
    def __init__(self, package_id, address, city, state, zipcode, due, weight, notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.due = due
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.state, self.zipcode, self.due, self.weight, self.notes, self.status)

# load packages csv data, create package object, and insert into hash table
def load_package_data(file, table):
    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for package in reader:
            package_id = package[0]
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_due = package[5]
            package_weight = package[6]
            package_notes = package[7]
            status = "Loaded"

            package_object = Package(package_id, package_address, package_city, package_state, package_zipcode, package_due, package_weight, package_notes, status)
            table.insert(package_id, package_object)


