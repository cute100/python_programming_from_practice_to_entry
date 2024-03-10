class User:
    def __init__(self,fisrt_name,last_name,username,email,location):
        self.first_name=fisrt_name
        self.last_name=last_name
        self.username=username
        self.email=email
        self.location=location
    def describle_user(self):
        print(f'{self.first_name}{self.last_name}')
        print(f'Username:{self.username}')
        print(f'Email:{self.email}')
        print(f'Location:{self.location}')
    def greet_user(self):
        print(f'你好，{self.first_name}{self.last_name}')

jiarun=User('chen','jiarun','xiaochen','email@','gangwuzhen')
jiarun.describle_user()
jiarun.greet_user()


