from distance import *
from datetime import datetime, timedelta
from nearest_neighbor import calculate_time

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

