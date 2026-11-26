# Logistics Management System

A console program for a logistics company. It manages shipments, vehicles
and warehouses, and calculates the delivery cost.

Team project for the PCAD course. Language: Python.

## Team

| Name | Part of the project |
| (name 1) | Vehicle classes (Vehicle, Truck, Van) |
| (name 2) | Shipment class and cost calculation |
| (name 3) | Warehouse class and main menu |

## How to run

1. Install Python 3.
2. Download the file `main.py`.
3. Run in the terminal: `python main.py`

## Menu

```
Logistics Management
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
```

## Classes

- **Warehouse**: id, name, capacity, current load.
- **Vehicle** (parent class): id, capacity, status, max distance.
  - **Truck** (child): 250 per km.
  - **Van** (child): 150 per km, +20% if the van is refrigerated.
- **Shipment**: id, weight, distance, warehouse, vehicle, cost, status.

## Rules of the program

- Vehicle statuses: Available, Loaded, On road.
- Shipment statuses: Created, In transit, Delivered.
- A shipment can be loaded only into an available vehicle.
  The weight must not exceed the vehicle capacity, and the distance must
  not exceed the vehicle max distance.
- A warehouse must have enough free space for a new shipment.
- A delivered shipment cannot be changed.
- Cost = distance * rate of the vehicle.

## Concepts used

| Concept | Where in the code |
|---------|-------------------|
| Variables, input, print | `input()`, `print()` in all functions |
| Conditions and loops | `if/elif/else`, `while True` in the menu and in `ask_int` |
| Dictionaries | `vehicles`, `warehouses`, `shipments`, `vehicle_statuses` |
| Functions with parameters and return | `ask_int`, `find_vehicle`, `add_shipment` |
| Classes, constructors, `self`, `__str__` | `Warehouse`, `Vehicle`, `Shipment` |
| Inheritance, `super()`, overriding | `Truck`, `Van` extend `Vehicle` |

## Example

```
Logistics Management
...
>>> 5
Enter vehicle ID: 1
Enter distance: 200
50000
```

## Known limitations

- Numbers must be entered as digits. Entering letters where a decimal
  number is expected (weight) stops the program.
- Data is stored only while the program is running.

## Possible improvements

- Save data to a file.
- Add a new vehicle type (for example Scooter).
