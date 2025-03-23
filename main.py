class Vehicle:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def display_info(self):
        print(f"{self.get_brand()} {self.get_model()} ({self.get_year()})")


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.__fuel_type = fuel_type

    def get_fuel_type(self):
        return self.__fuel_type

    def display_info(self):
        super().display_info()
        print(f" - Fuel: {self.get_fuel_type()}")

    def start_engine(self):
        print("Vroom! The car engine is started.")


class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.__engine_capacity = engine_capacity

    def get_engine_capacity(self):
        return self.__engine_capacity

    def display_info(self):
        super().display_info()
        print(f" - Engine: {self.get_engine_capacity()}cc")

    def start_engine(self):
        print("Rev! The bike engine is started.")


cars = [
    Car("Toyota", "Corolla", 2022, "Petrol"),
    Car("Honda", "Civic", 2020, "Diesel"),
    Car("Ford", "Mustang", 2019, "Petrol"),
    Car("Nissan", "Altima", 2018, "Hybrid"),
    Car("Volkswagen", "Golf", 2017, "Diesel"),
    Car("BMW", "3 Series", 2016, "Petrol"),
    Car("Mercedes-Benz", "C-Class", 2015, "Diesel"),
    Car("Audi", "A4", 2014, "Petrol"),
]

bikes = [
    Bike("Yamaha", "R15", 2021, 155),
    Bike("Honda", "CBR500R", 2020, 500),
    Bike("Kawasaki", "Ninja 400", 2019, 400),
    Bike("Suzuki", "GSX-R600", 2018, 600),
    Bike("Ducati", "Panigale V4", 2017, 1103),
    Bike("Harley-Davidson", "Softail", 2016, 107),
    Bike("Triumph", "Street Triple", 2015, 675),
    Bike("KTM", "RC 390", 2014, 390),
]

for car in cars:
    car.display_info()
    car.start_engine()
    print()

for bike in bikes:
    bike.display_info()
    bike.start_engine()
    print()