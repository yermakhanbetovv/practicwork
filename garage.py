from vehicle import Vehicle


class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def list_vehicles(self):
        for v in self.vehicles:
            print(f"- {v.brand} {v.model} ({v.year})")
