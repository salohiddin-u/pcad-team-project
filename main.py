# ---------- Status dictionaries ----------
# number -> text. The user chooses a number, the program uses the text.
vehicle_statuses = {1: "Available", 2: "Loaded", 3: "On road"}
shipment_status = {1: "Created", 2: "In transit", 3: "Delivered"}

# ---------- Helper functions for input ----------
# ask a whole positive number, repeat until the input is correct
def ask_int(a):
    while True:
        value = input(a)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a positive whole number")

# ask a positive decimal number (for example 0.5)
def ask_float(a):
    while True:
        value = input(a)
        if isinstance(float(value), float) and float(value) > 0:
            return float(value)
        print("Please enter a positive number (for example 0.5)")

# ask a number and check that it is one of the keys of the dictionary
# returns the value from the dictionary
def ask_choice(a, options):
    choice = ask_int(a)
    while choice not in options:
        print(f"Please choose one of: {', '.join(map(str, options))}")
        choice = ask_int(">>> ")
    return options[choice]

# ---------- Classes ----------
class Warehouse:
    # create a warehouse with its data
    def __init__(self, warehouse_id, name, capacity, current_load):
        self.warehouse_id = warehouse_id
        self.name = name
        self.capacity = capacity
        self.current_load = current_load

    # text for print(warehouse)
    def __str__(self):
        return f"Warehouse #{self.warehouse_id}\nName: {self.name}\nCapacity: {self.capacity} tonne\nCurrent load: {self.current_load} tonne"


class Vehicle:
    rate = 100                     # price per km (children change it)
    label = "Vehicle"              # name of the type (children change it)
    def __init__(self, vehicle_id, capacity, status, max_distance):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.status = status
        self.max_distance = max_distance

    # cost of delivery = distance * price per km
    def calculate_cost(self, distance):
        return distance*self.rate
  
    # change the status of the vehicle and return a message
    def change_status(self, new_status):
        if new_status == self.status:
            return f"{self.label} ID: {self.vehicle_id} status is already {self.status}"
        self.status = new_status
        return f"{self.label} ID: {self.vehicle_id} status changed to {self.status}"

    # text for print(vehicle)
    def __str__(self):
        return f"{self.label} ID: {self.vehicle_id}\nCapacity: {self.capacity} tonne\nStatus: {self.status}\nMax distance: {self.max_distance} km"

# child class: a truck has its own price and label
class Truck(Vehicle):
    rate = 250
    label = "Truck"

# child class: a van can be refrigerated
class Van(Vehicle):
    rate = 150
    label = "Van"

    def __init__(self, vehicle_id, capacity, status, max_distance, refrigerated=False):
         # super() calls the constructor of the parent class
        super().__init__(vehicle_id, capacity, status, max_distance)
        self.refrigerated = refrigerated

    # overriding: refrigerated vans cost 20% more
    def calculate_cost(self, distance):
        cost = super().calculate_cost(distance)
        if self.refrigerated:
            cost *= 1.2
        return cost
    
    # overriding: parent text + one more line
    def __str__(self):
        return super().__str__() + f"\nRefrigerated: {'Yes' if self.refrigerated else 'No'}"


class Shipment:
    def __init__(self, shipment_id, weight, distance, warehouse, vehicle, cost, status):
        self.shipment_id = shipment_id
        self.weight = weight
        self.distance = distance
        self.warehouse = warehouse         # Warehouse object
        self.vehicle = vehicle             # Vehicle object, or None if not loaded
        self.cost = cost
        self.status = status

     # change the status of the shipment and return a message
    def change_status(self, new_status):
        if new_status == self.status:
            return f"Shipment #{self.shipment_id} status is already {self.status}"
        self.status = new_status
        return f"Shipment #{self.shipment_id} status changed to {self.status}"

     # text depends on whether the shipment is loaded into a vehicle
    def __str__(self):
        if self.vehicle is None:
            return f"Shipment #{self.shipment_id}\nWeight: {self.weight} tonne\nDistance: {self.distance} km\nWarehouse: {self.warehouse.name}\nVehicle: Not loaded yet\n{self.cost}\nStatus: {self.status}"    
        return f"Shipment #{self.shipment_id}\nWeight: {self.weight} tonne\nDistance: {self.distance} km\nWarehouse: {self.warehouse.name}\n{self.vehicle.label} ID: {self.vehicle.vehicle_id}\n{self.cost}\nStatus: {self.status}"

# ---------- Start data (dictionaries: id -> object) ----------
# number -> class, used when the user adds a vehicle
vehicle_types = {1: Truck, 2: Van}

vehicles = {
    1: Truck(1, 20, vehicle_statuses[3], 1200),
    2: Truck(2, 15, vehicle_statuses[2], 1000),
    3: Truck(3, 10, vehicle_statuses[1], 800),
    4: Van(4, 5, vehicle_statuses[1], 500),
    5: Van(5, 3, vehicle_statuses[1], 400),
}

warehouses = {
    1: Warehouse(1, "Tashkent", 100, 18),
    2: Warehouse(2, "Fergana", 50, 0),
    3: Warehouse(3, "Samarkand", 80, 8),
}

shipments = {
    1: Shipment(1, 12, 200, warehouses[1], vehicles[1], 50000, shipment_status[2]),
    2: Shipment(2, 8, 300, warehouses[3], vehicles[2], 75000, shipment_status[1]),
    3: Shipment(3, 3, 150, warehouses[2], vehicles[4], 22500, shipment_status[3]),
    4: Shipment(4, 6, 100, warehouses[1], None, 0, shipment_status[1]),
}


# ---------- Warehouse functions ----------
# create a new warehouse and save it in the dictionary
def add_warehouse():
    warehouse_id = ask_int("Enter warehouse ID: ")
    while warehouse_id in warehouses:
        print(f"Warehouse with ID {warehouse_id} already exists")
        warehouse_id = ask_int("Enter warehouse ID: ")
    name = input("Enter warehouse name: ")
    capacity = ask_int("Enter capacity (tonne): ")
    current_load = 0
    warehouse = Warehouse(warehouse_id, name, capacity, current_load)
    warehouses[warehouse_id] = warehouse
    return warehouse

# return text with all warehouses
def show_warehouses():
    if not warehouses:
        return "No warehouses yet"
    return "\n\n".join(str(w) for w in warehouses.values())


# ---------- Vehicle functions ----------
# ask an ID until the vehicle exists, return the vehicle object
def find_vehicle(vehicle_id):
    vehicle_id = ask_int(vehicle_id)
    while vehicle_id not in vehicles:
        vehicle_id = ask_int(f"Vehicle #{vehicle_id} is not found\nEnter a valid ID: ")
    return vehicles[vehicle_id]

# show the types and return the chosen class (Truck or Van)
def ask_vehicle_type():
    t = "\n".join(f"{i}. {v.label}" for i, v in vehicle_types.items()) + "\n>>> "
    return ask_choice("Select type: \n" + t, vehicle_types)

# create a new vehicle and save it in the dictionary
def add_vehicle():
    vehicle_type = ask_vehicle_type()
    
    # repeat until the ID is new
    while True:
        vehicle_id = ask_int("Enter Vehicle ID: ")
        if vehicle_id not in vehicles:
            break
        print(f"Vehicle ID {vehicle_id} already exists")
        
    capacity = ask_int("Enter the capacity of the vehicle (tonne): ")

    max_distance = ask_int("Enter max distance: ")
  
    # a new vehicle is always Available
    vehicle = vehicle_type(vehicle_id, capacity, vehicle_statuses[1], max_distance)
    vehicles[vehicle_id] = vehicle
    return vehicle

# calculate the cost for a chosen vehicle and distance
def calculate_cost():
    vehicle = find_vehicle("Enter vehicle ID: ")
    distance = ask_int("Enter distance: ")
    while distance > vehicle.max_distance:
        print(f"Distance must not exceed {vehicle.max_distance} km")
        distance = ask_int("Enter distance: ")
    cost = vehicle.calculate_cost(distance)
    return cost

# return text with all vehicles
def show_vehicles():
    if not vehicles:
        return "No vehicles yet"
    return "\n\n".join(str(v) for v in vehicles.values())

# ask an ID until the warehouse exists, return the warehouse object
def find_warehouse(text):
    warehouse_id = ask_int(text)
    while warehouse_id not in warehouses:
        warehouse_id = ask_int(f"Warehouse #{warehouse_id} is not found\nEnter a valid ID: ")
    return warehouses[warehouse_id]


# ---------- Shipment functions ----------
# ask an ID until the shipment exists, return the shipment object
def find_shipment(text):
    shipment_id = ask_int(text)
    while shipment_id not in shipments:
        shipment_id = ask_int(f"Shipment #{shipment_id} is not found\nEnter a valid ID: ")
    return shipments[shipment_id]

# create a new shipment (not loaded into a vehicle yet)
def add_shipment():
    shipment_id = ask_int("Enter shipment ID: ")
    while shipment_id in shipments:
        print(f"Shipment with ID {shipment_id} already exists")
        shipment_id = ask_int("Enter shipment ID: ")

    warehouse = find_warehouse("Enter warehouse ID: ")
    weight = ask_float("Enter weight (tonne): ")
     # check free space in the warehouse
    if warehouse.capacity - warehouse.current_load < weight:
        return f"Warehouse {warehouse.name} does not have enough space ({warehouse.capacity - warehouse.current_load} tonne left)"

    distance = ask_int("Enter distance: ")

    shipment = Shipment(shipment_id, weight, distance, warehouse, None, 0, shipment_status[1])
    shipments[shipment_id] = shipment
    warehouse.current_load += weight
    return shipment

# put a shipment into a vehicle (all checks first)
def load_shipment():
    shipment = find_shipment("Enter shipment ID: ")
    if shipment.vehicle is not None:
        return f"Shipment #{shipment.shipment_id} is already loaded into {shipment.vehicle.label} #{shipment.vehicle.vehicle_id}"

    vehicle = find_vehicle("Enter vehicle ID: ")
    # the vehicle must be free, strong enough and able to drive that far
    if vehicle.status != vehicle_statuses[1]:
        return f"{vehicle.label} #{vehicle.vehicle_id} is not available (status: {vehicle.status})"
    if shipment.weight > vehicle.capacity:
        return f"Weight {shipment.weight} tonne exceeds the vehicle's capacity ({vehicle.capacity} tonne)"
    if shipment.distance > vehicle.max_distance:
        return f"Distance {shipment.distance} km exceeds the vehicle's max distance ({vehicle.max_distance} km)"

    # all checks passed: connect shipment and vehicle
    shipment.vehicle = vehicle
    shipment.cost = vehicle.calculate_cost(shipment.distance)
    vehicle.change_status(vehicle_statuses[2])
    return shipment

# change the status of a shipment and update the vehicle and the warehouse
def change_shipment_status():
    shipment = find_shipment("Enter shipment ID: ")
    print(f"Current status of shipment #{shipment.shipment_id}: {shipment.status}")
    if shipment.vehicle is None:
        return "Shipment is not loaded into a vehicle yet. Load it first"
    if shipment.status == shipment_status[3]:
        return "Delivered shipment cannot be changed"
    new_status = ask_choice("Select status of shipment:\n1. Created\n2. In transit\n3. Delivered\n>>> ", shipment_status)
    if new_status == shipment.status:
        return shipment.change_status(new_status)
    result = shipment.change_status(new_status)
    
    # the vehicle status follows the shipment status
    if new_status == shipment_status[1]:
        shipment.vehicle.change_status(vehicle_statuses[2])
    elif new_status == shipment_status[2]:
        shipment.vehicle.change_status(vehicle_statuses[3])
    elif new_status == shipment_status[3]:
        shipment.vehicle.change_status(vehicle_statuses[1])
        shipment.warehouse.current_load -= shipment.weight
    return result
# return text with all shipments
def show_shipments():
    if not shipments:
        return "No shipments yet"
    return "\n\n".join(str(s) for s in shipments.values())

# ---------- Main program ----------
menu = """\nLogistics Management
1. Add shipment
2. Load shipment
3. Change shipment status
4. All shipments
5. Calculate cost
6. Show all vehicles
7. Add vehicle
8. Warehouses
9. Add warehouse
10. Exit
>>> """

# the menu repeats until the user chooses 10
while True:
    choice = ask_int(menu)

    if choice == 1:
        print(add_shipment())
    elif choice == 2:
        print(load_shipment())
    elif choice == 3:
        print(change_shipment_status())
    elif choice == 4:
        print(show_shipments())
    elif choice == 5:
        print(calculate_cost())
    elif choice == 6:
        print(show_vehicles())
    elif choice == 7:
        print(add_vehicle())
    elif choice == 8:
        print(show_warehouses())
    elif choice == 9:
        print(add_warehouse())
    elif choice == 10:
        print("Exiting the program")
        break
    else:
        print("Invalid choice. Choose from 1 to 10")
