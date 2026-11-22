class Warehouse:
    def __init__(self, warehouse_id, name, capacity, current_load):
        self.warehouse_id = warehouse_id
        self.name = name
        self.capacity = capacity
        self.current_load = current_load

    def load_info(self, capacity, current_load, name):
        return f"{name} can hold more {capacity-current_load} t shipments"

    def __str__(self):
        return f"Warehouse #{self.warehouse_id}\nName: {self.name}\nCapacity: {self.capacity}\nCurrent load: {self.current_load}"