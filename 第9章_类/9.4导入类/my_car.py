from class_car import Car
from class_car import ElectricCar
my_new_car=Car('audi','a4',2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=266
my_new_car.read_odometer()

my_mustdog=Car('ford','mustang','2024')
print(my_mustdog.get_descriptive_name())

my_leaf=ElectricCar('nissan','leaf','2024')
print(my_leaf.get_descriptive_name())