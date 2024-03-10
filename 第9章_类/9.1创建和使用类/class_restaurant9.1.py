class Restaurant:
    def __init__(self,restayrant_name,cuisine_type):
        self.restayrant_name=restayrant_name
        self.cuisin_type=cuisine_type
    def describe_restaurant(self):
        print(f'{self.restayrant_name}  {self.cuisin_type}')
    def open_restaurant(self):
        print(f'{self.restayrant_name} is opening' )

restaurant=Restaurant('XINFU','CHUCANCAI')
restaurant.describe_restaurant()
restaurant.open_restaurant()