from garage import Garage


class Fleet:
    def __init__(self):
        self.garages = []

    def add_garage(self, garage: Garage):
        self.garages.append(garage)

    def remove_garage(self, garage: Garage):
        if garage in self.garages:
            self.garages.remove(garage)

    def find_vehicle(self, model_name: str):
        for g in self.garages:
            for v in g.vehicles:
                if v.model == model_name:
                    return v
        return None
