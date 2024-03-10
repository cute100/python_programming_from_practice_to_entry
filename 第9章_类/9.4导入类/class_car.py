class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This Car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

class Battery:
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self,battery_size=40):
        """初始化电池的属性"""
        self.battery_size=battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size==40:
            range=150
        elif self.battery_size==65:
            range=225
        print(f"This car can go about {range} miles on a full charge")
    def upgrade_battery(self):
        """在可能的情况下将电池审计"""
        if self.battery_size==40:
            self.battery_size=65
            print('Upgranded the battery to 65 kWh')
        else:
            print('The battery is already upgraded.')
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性
        再初始化电动汽车特有的属性"""
        super().__init__(make,model,year)
        self.battery=Battery()
