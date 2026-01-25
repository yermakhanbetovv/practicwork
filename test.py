from car import Car
from motorcycle import Motorcycle
from garage import Garage
from fleet import Fleet

def test_vehicles():
    car = Car("BMW", "M3", 2021, 2, "Manual")
    moto = Motorcycle("Yamaha", "R1", 2020, "Sport", True)

    assert car.brand == "BMW"
    assert moto.body_type == "Sport"

    car.start_engine()
    moto.start_engine()

def test_garage():
    car = Car("Audi", "A4", 2019, 4, "Auto")
    garage = Garage()

    garage.add_vehicle(car)
    assert car in garage.vehicles

    garage.remove_vehicle(car)
    assert car not in garage.vehicles

def test_fleet():
    car = Car("Toyota", "Supra", 2022, 2, "Auto")
    garage = Garage()
    garage.add_vehicle(car)

    fleet = Fleet()
    fleet.add_garage(garage)

    found = fleet.find_vehicle("Supra")
    assert found is not None
    assert found.model == "Supra"

if __name__ == "__main__":
    test_vehicles()
    test_garage()
    test_fleet()
    print("Все тесты прошли!")
