class Restaurant:
    def __init__(self,restayrant_name,cuisine_type):
        self.restayrant_name=restayrant_name
        self.cuisin_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f'{self.restayrant_name}  {self.cuisin_type}')
    def open_restaurant(self):
        print(f'{self.restayrant_name} is opening' )
    def set_number_served(self,number01):
        self.number_served=number01
        print(f'就餐人数{number01}人')
    def increment_number_served(self,number02):
        self.number_served+=number02
        print(f'我认为这家餐馆每天可能接待的就餐人数是{self.number_served}人。')

restaurant=Restaurant('XINFU','CHUCANCAI')
restaurant.describe_restaurant()
restaurant.open_restaurant()
#restaurant.set_number_served(10)
restaurant.increment_number_served(20)