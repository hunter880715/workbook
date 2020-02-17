# coding: GBK 
class Car():
    """һ��ģ�������ļ򵥳��ԡ�"""

    def __init__(self, manufacturer, model, year):
        """��ʼ���������������ԡ�"""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """�����������������Ϣ��"""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """��ӡһ��ָ��������̵���Ϣ��"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        ����̱��������Ϊָ����ֵ��
        ��ֹ����̱�������ص���
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """����̱��������ָ��������"""
        self.odometer_reading += miles

class Battery():
    """һ��ģ��綯������ƿ�ļ򵥳��ԡ�"""

    def __init__(self, battery_size=60):
        """��ʼ����ƿ�����ԡ�"""
        self.battery_size = battery_size

    def describe_battery(self):
        """��ӡһ��������ƿ��������Ϣ��"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

        
    def get_range(self):
        """��ӡһ����Ϣ��ָ����ƿ��������̡�"""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """�ڿ��ܵ�����½���ƿ������"""
        if self.battery_size == 60:  # Ĭ������
            self.battery_size = 85   # ���ú�����
            print("Upgraded the battery to 85 kWh.")
        else:
            print("\nThe battery is already upgraded.")
    
        
class ElectricCar(Car):
    """�綯�����Ķ���֮����"""

    def __init__(self, manufacturer, model, year):
        """
        ��ʼ����������ԣ��ٳ�ʼ���綯�������е����ԡ�
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
# Ĭ�ϵ�ƿ����ʱ���ã�
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
# ���ú��ƿ����ʱ���ã�
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
