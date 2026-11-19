class Warehouse:
    # create a warehouse with empty lists
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.shipments = []

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def add_shipment(self, shipment):
        self.shipments.append(shipment)



    def find_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                return vehicle
        return None    


    # find a shipment by id, return None if not found
    def find_shipment(self, shipment_id):
        for shipment in self.shipments:
            if shipment.id == shipment_id:
                return shipment
        return None


    # count shipments by status and return a dictionary 
    def count_by_status(self):
        result = {}
        for shipment in self.shipments:
            status = shipment.status
            if status in result:
                result[status] = result[status] + 1 
            else:
                result[status] = 1
        return result         

    def __str__(self):
        return f"Warehouse {self.name}: {len(self.vehicles)} vehicles, {len(self.shipments)} shipments"


    # print all vehicles
    def show_vehicles(self):
        print("Vehicles in warehouse:")
        for vehicle in self.vehicles:
            print(vehicle)

    # print all shipments
    def show_shipments(self):
        print("Shipments in warehouse:")
        for shipment in self.shipments:
            print(shipment)


class FakeVehicle:
    def __init__(self, id):
        self.id = id  


    def __str__(self):
        return f"Vehicle {self.id}"    


class FakeShipment:
    def __init__(self, id, status):
        self.id = id
        self.status = status


    def __str__(self):
        return f"Shipment {self.id} ({self.status})"    
                           

    # text for print(warehouse)
w = Warehouse("Main")
print(w)  

w.add_vehicle(FakeVehicle(1))
w.add_vehicle(FakeVehicle(2))
print(w)

print(w.find_vehicle(2).id)
print(w.find_vehicle(99))


w.add_shipment(FakeShipment(1, "created"))
w.add_shipment(FakeShipment(2, "created"))
w.add_shipment(FakeShipment(3, "delivered"))
print(w.find_shipment(3).status)
print(w.find_shipment(99))
print(w.count_by_status())

w.show_vehicles()
w.show_shipments()