class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.brand} {self.model} ({self.year}) — двигатель запущен")

    def stop_engine(self):
        print(f"{self.brand} {self.model} ({self.year}) — двигатель остановлен")
