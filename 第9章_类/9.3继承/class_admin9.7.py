class User:
    def __init__(self,fisrt_name,last_name):
        self.first_name=fisrt_name
        self.last_name=last_name
        self.login_attempts=0
    def describle_user(self):
        print(f'{self.first_name}{self.last_name}')
    def greet_user(self):
        print(f'你好，{self.first_name}{self.last_name}')
    def increment_login_attenmpts(self):
        self.login_attempts+=1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts=0
        print(self.login_attempts)
class Admin(User):
    def __init__(self,fisrt_name,last_name):
        super().__init__(fisrt_name,last_name)
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        print(self.privileges)
admin=Admin('chen','mr')
admin.show_privileges()
admin.describle_user()