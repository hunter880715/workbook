# coding: GBK 
# 9-10 ���� Restaurant �ࣺ�����µ� Restaurant �ഺ����һ��ģ���С�
"""һ���������ڱ�ʾ�͹ݸ������Ե���"""
class Restaurant():
    """һ�Ҳ͹ݵĳ���"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """��ʼ���͹�����"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """��ӡǰ������������Ϣ"""
        msg = "The restaurant name is: "
        msg += self.name.title() + ";"
        msg += "\n" + "cuisine type is: "
        msg += self.type.title() + ".\n"
        print(msg)
            
    def open_restaurant(self):
        """ָ���͹�����Ӫҵ"""
        print(self.name.title() + " is on business.\n")
    
    def set_number_served(self, number_served):
        """�޸ľͲ�����"""
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        """�Ͳ���������"""
        self.number_served += additional_servedclass
        
class IceCreamStand(Restaurant):
    """����ܲ͹�����֮��"""
    def __init__(self, restaurant_name, cuisine_type):
        """��ʼ����������"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # ��� flavors ���ԣ�����һ���洢������б�

    def show_flavors(self):
        """��ʾ����ܵ�Ʒ��"""
        print("�����ṩ���¼��ֿ�ζ�����:")
        for flavors in self.flavors:
            print("- " + flavors.title())
