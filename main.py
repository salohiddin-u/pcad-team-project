statuses = {1: "Available", 2: "Loaded", 3: "On road"}


class Vehicle:
    rate = 100
    label = "Vehicle"
    def __init__(self, vehicle_id, capacity, status, max_distance):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.status = status
        self.max_distance = max_distance

    def calculate_cost(self, distance):
        return distance*self.rate

    def change_status(self, new_status):
        if new_status == self.status:
            return f"{self.label} ID: {self.vehicle_id} status is already {self.status}"
        self.status = new_status
        return f"{self.label} ID: {self.vehicle_id} status changed to {self.status}"

    def __str__(self):
        return f"{self.label} ID: {self.vehicle_id}\nCapacity: {self.capacity} tonne\nStatus: {self.status}\nMax distance: {self.max_distance} km"

class Truck(Vehicle):
    rate = 250
    label = "Truck"


class Van(Vehicle):
    rate = 150
    label = "Van"

vehicle_types = {1: Truck, 2: Van}

vehicles = {
    1: Vehicle(1, 5, statuses[1], 500),
    2: Vehicle(2, 10, statuses[1], 800),
    3: Truck(3, 20, statuses[2], 1200),
    4: Vehicle(4, 8, statuses[3], 650),
    5: Truck(5, 15, statuses[1], 1000),
    6: Van(6, 5, statuses[1], 500),
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

def ask_vehicle_type():
    t = "\n".join(f"{i}. {v.label}" for i, v in vehicle_types.items()) + "\n>>> "
    choice = ask_int("Select type: \n" + t)
    while choice not in vehicle_types:
        print("Please choose 1 or 2.")
        choice = ask_int(">>> ")
    return vehicle_types[choice]

def add_vehicle():
    vehicle_type = ask_vehicle_type()

    while True:
        vehicle_id = ask_int("Enter Vehicle ID: ")
        if vehicle_id not in vehicles:
            break
        print(f"Vehicle ID {vehicle_id} already exists.")
        
    capacity = ask_int("Enter the capacity of the vehicle: ")

    max_distance = ask_int("Enter max distance: ")
 
    vehicle = vehicle_type(vehicle_id, capacity, statuses[1], max_distance)
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


menu = """\nLogistics Management\n
1. Load shipment\n
2. Change shipment status\n
3. All shipments\n
4. Show all vehicles\n
5. Add vehicle\n
6. Warehouses\n
7. Change vehicle status\n
8. Calculate cost\n
0. Exit\n
>>> """


while True:
    choice = ask_int(menu)

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print(show_vehicles())
    elif choice == 5:
        print(add_vehicle())
    elif choice == 6:
        print(show_warehouses())
    elif choice == 7:
        print(change_status())
    elif choice == 8:
        print(calculate_cost())
    elif choice == 0:
        print("Exiting the program.")
        break