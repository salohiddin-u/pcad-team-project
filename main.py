statuses = {1: "Available", 2: "Loaded", 3: "On road"}

class Vehicle:
    def __init__(self, vehicle_id, capacity, status, max_distance):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.status = status
        self.max_distance = max_distance

    def calculate_cost(self, distance):
        return distance*100

    def change_status(self, new_status):
        if new_status == self.status:
            return f"Vehicle ID: {self.vehicle_id} status is already {self.status}"
        self.status = new_status
        return f"Vehicle ID: {self.vehicle_id} status changed to {self.status}"

    def __str__(self):
        return f"Vehicle ID: {self.vehicle_id}\nCapacity: {self.capacity} tonne\nStatus: {self.status}\nMax distance: {self.max_distance} km"

vehicles = {
    1: Vehicle(1, 5, statuses[1], 500),
    2: Vehicle(2, 10, statuses[1], 800),
    3: Vehicle(3, 2, statuses[2], 200),
    4: Vehicle(4, 8, statuses[3], 650),
    5: Vehicle(5, 3, statuses[1], 300),
}


