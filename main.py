class Warehouse:
    def __init__(self, warehouse_id, name, capacity, current_load):
        self.warehouse_id = warehouse_id
        self.name = name
        self.capacity = capacity
        self.current_load = current_load

    def load_info(self, capacity, current_load, name):
        return f"{name} can hold more {capacity-current_load} t shipments"

    def __str__(self):
        return f"Warehouse #{self.warehouse_id}\nName: {self.name}\nCapacity: {self.capacity} shipments\nCurrent load: {self.current_load}"

warehouses = {
    1: Warehouse(1, "Tashkent", 500, 120),
    2: Warehouse(2, "Fergana", 300, 300),
    3: Warehouse(3, "Samarkand", 450, 0),
}

def add_warehouse():
    warehouse_id = ask_int("Enter warehouse ID: ")
    while not warehouse_id in warehouses:
        print(f"Warehouse with ID {warehouse_id} is available.")
        warehouse_id = ask_int("Enter warehouse ID: ")
    name = input("Enter warehouse name: ")
    capacity = ask_int("Enter capacity: ")
    current_load = 0
    warehouse = Warehouse(warehouse_id, name, capacity, current_load)
    warehouses[warehouse_id] = warehouse
    return warehouse