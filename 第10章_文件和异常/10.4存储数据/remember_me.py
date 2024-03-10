from pathlib import Path
import json


def  get_sorted_username(path):
    """如果存在用户，就获取它"""
    if path.exists():
        contents=path.read_text()
        username=json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """提示输入用户名"""
    username = input("What is you name?")
    userage=input("How old are you?")
    wherename=input("Where are you from?")
    user=[username,userage,wherename]
    contents = json.dumps(user)
    path.write_text(contents)
    return username
def greet_user():
    """问候用户，并指出姓名"""
    path = Path('username.json')
    username=get_sorted_username(path)
    if username:
        print(f'Welcome back,{username}!')
    else:
        username=get_new_username(path)
        print(f"We'll remember you when you come back,{username}!")

greet_user()