class Car:
    def __init__(self, brand: str, model: str, horsepower: int):
        self.brand = brand
        self.model = model
        self.horsepower = horsepower
        self.engine_running = False

    
    def start_engine(self) -> str:
        if self.engine_running:
            return f"{self.brand} {self.model}: двигатель уже работает"
        self.engine_running = True
        return f"{self.brand} {self.model}: двигатель заведён"

    
    @staticmethod
    def calculate_tax(horsepower: int, rate_per_hp: float = 12.0) -> float:
        if horsepower <= 0:
            raise ValueError("Мощность должна быть положительной")
        return horsepower * rate_per_hp



print(Car.calculate_tax(150))      

car = Car("Toyota", "Camry", 150)
print(car.start_engine())          
print(car.start_engine())          