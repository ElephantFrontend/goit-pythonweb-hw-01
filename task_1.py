from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} {model}", "(US Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} {model}", "(US Spec)")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} {model}", "(EU Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} {model}", "(EU Spec)")

def main():
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle2 = eu_factory.create_motorcycle("BMW", "R1200")

    vehicle1.start_engine()
    vehicle2.start_engine()

if __name__ == "__main__":
    main()
