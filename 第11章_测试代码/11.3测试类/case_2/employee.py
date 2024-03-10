
class Employee():
    def __init__(self,first_name,last_name,yearly_pay=0):
        self.first_name=first_name
        self.last_name=last_name
        self.yearly_pay=yearly_pay
        self.add_pay=5000
        print(f"你好，{self.first_name}{self.last_name}!!!\n")
    def give_raise(self):
        print(f"你现在的年薪是{self.yearly_pay}美元，将为你增加至5000美元。")
        self.yearly_pay+=self.add_pay
        print(f"你现在的年薪已经更新为{self.yearly_pay}美元")
        while True:
            self.yearly_pay = input(f"你现在的年薪是{self.yearly_pay}美元,如果你不满意，请自行输入其他的年薪增加量：")
            if self.yearly_pay=='q':
                print(f"你未变革年薪！！！")
                break
            else:
                print(f"你最终确定的年薪是{self.yearly_pay}美元\n")

