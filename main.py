from car import Car
from motorcycle import Motorcycle
from garage import Garage
from fleet import Fleet

if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020, 4, "Automatic")
    car2 = Car("BMW", "M5", 2018, 4, "Manual")
    moto1 = Motorcycle("Yamaha", "R1", 2021, "Sport", True)

    garage1 = Garage()
    garage2 = Garage()
    garage1.add_vehicle(car1)
    garage1.add_vehicle(moto1)
    garage2.add_vehicle(car2)

    fleet = Fleet()
    fleet.add_garage(garage1)
    fleet.add_garage(garage2)

    print("=== Гараж 1 ===")
    garage1.list_vehicles()

    print("\n=== Гараж 2 ===")
    garage2.list_vehicles()
    garage1.remove_vehicle(moto1)
    print("\n=== Гараж 1 после удаления мотоцикла ===")
    garage1.list_vehicles()
    found = fleet.find_vehicle("M5")
    if found:
        print(f"\nНайдено: {found.brand} {found.model} ({found.year})")
    else:
        print("\nНе найдено")
