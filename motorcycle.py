from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, body_type, has_box):
        super().__init__(brand, model, year)
        self.body_type = body_type
        self.has_box = has_box
