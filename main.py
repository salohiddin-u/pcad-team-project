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


def ask_int(a):
    while True:
        value = input(a)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a positive whole number.")

def find_vehicle(vehicle_id):
    vehicle_id = ask_int(vehicle_id)
    while vehicle_id not in vehicles:
        vehicle_id = ask_int(f"Vehicle #{vehicle_id} is not found\nEnter a valid ID: ")
    return vehicles[vehicle_id]

def valid_status(status):
    status = ask_int(status)
    while not status in statuses:
        print("Please choose 1, 2, or 3.")
        status = ask_int(">>> ")
    return statuses[status]

def add_vehicle():
    while True:
        vehicle_id = ask_int("Enter Vehicle ID: ")
        if vehicle_id not in vehicles:
            break
        print(f"Vehicle ID {vehicle_id} already exists.")
        
    capacity = ask_int("Enter the capacity of the vehicle: ")

    max_distance = ask_int("Enter max distance: ")
 
    vehicle = Vehicle(vehicle_id, capacity, statuses[1], max_distance)
    vehicles[vehicle_id] = vehicle
    return vehicle

def change_status():
    vehicle = find_vehicle("Enter vehicle ID: ")
    new_status = valid_status("Select status of vehicle:\n1. Available\n2. Loaded\n3. On road\n>>> ")
    return vehicle.change_status(new_status)

def calculate_cost():
    vehicle = find_vehicle("Enter vehicle ID: ")
    distance = ask_int("Enter distance: ")
    while distance > vehicle.max_distance:
        print(f"Distance must not exceed {vehicle.max_distance} km.")
        distance = ask_int("Enter distance: ")
    cost = vehicle.calculate_cost(distance)
    return cost

def show_vehicles():
    if not vehicles:
        return "No vehicles yet."
    return "\n\n".join(str(v) for v in vehicles.values())
