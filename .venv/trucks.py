from distance import *
from datetime import datetime, timedelta
from nearest_neighbor import calculate_time
from distance import *

# create truck class here
class Truck:
    def __init__(self, truck_id, depart_time, ):
        self.capacity = 16
        self.speed = 18
        self.miles = 0.0
        self.truck_id = truck_id
        self.address = '4001 South 700 East'
        self.to_deliver = []
        self.delivered = []
        self.group_packages = []
        self.depart_time = datetime.strptime(depart_time, '%I:%M %p')
        self.current_time = datetime.strptime(depart_time, '%I:%M %p')

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (self.capacity, self.speed, self.miles, self.address, self.packages, self.depart_time, self.truck_id, self.current_time)

    # return truck to hub and add the miles for the return
    def return_to_hub(self):
        current_address_index = address_hash_table.lookup(self.address)
        self.address = '4001 South 700 East'
        self.miles = self.miles + float(find_distance(0, current_address_index))
        self.current_time = calculate_time(self.current_time, float(find_distance(0, current_address_index)), self.speed)

    def get_info(self, time):
        current_address = '4001 South 700 East'
        current_miles = 0
        current_time = self.depart_time

        # iterate through each address and set the last address as current address
        for pkg in self.to_deliver:
            if time < pkg.delivered_at:
                break
            # get previous and current address indexes
            prev_address_index = address_hash_table.lookup(current_address)
            curr_address_index = address_hash_table.lookup(pkg.address)

            # find distance between previous and current address and add to miles
            miles_to_add = find_distance(prev_address_index, curr_address_index)
            current_miles += float(miles_to_add)
            # update current address
            current_address = pkg.address

        return [current_miles, current_address]

    def get_packages(self):
        package_ids = []
        for pkg in self.to_deliver:
            package_ids.append(pkg.package_id)

        return package_ids



truck_hash_table = HashTable()

# instantiate trucks
truck_1 = Truck(1, '08:00 AM')
truck_2 = Truck(2, '09:05 AM')
truck_3 = Truck(3, '10:00 AM')
trucks = [truck_1, truck_2, truck_3]

# add trucks to hash table
for truck in trucks:
    truck_hash_table.insert(truck.truck_id, truck)
