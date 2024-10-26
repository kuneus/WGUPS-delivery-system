# create truck class here
class Truck:
    def __init__(self, capacity, address, packages, depart_time, truck_id):
        self.capacity = capacity
        self.speed = 18
        self.miles = 0
        self.address = address
        self.packages = packages
        self.depart_time = depart_time
        self.truck_id = truck_id


    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.capacity, self.speed, self.miles, self.address, self.packages, self.depart_time, self.truck_id)