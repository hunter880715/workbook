# coding: GBK 
class Car():
    """一次模拟汽车的简单尝试。"""

    def __init__(self, manufacturer, model, year):
        """初始化描述汽车的属性。"""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值。
        禁止将里程表读数往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量。"""
        self.odometer_reading += miles

class Battery():
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=60):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

        
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """在可能的情况下将电瓶升级。"""
        if self.battery_size == 60:  # 默认容量
            self.battery_size = 85   # 设置后容量
            print("Upgraded the battery to 85 kWh.")
        else:
            print("\nThe battery is already upgraded.")
    
        
class ElectricCar(Car):
    """电动汽车的独特之处。"""

    def __init__(self, manufacturer, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性。
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
# 默认电瓶容量时调用：
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
# 设置后电瓶容量时调用：
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
