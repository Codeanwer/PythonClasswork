class Employee:
    def __init__(self,name):
        self.name = name
    def get_salary(self):
        pass
class Manager(Employee):
    def __init__(self,name,salary=15000):
        super().__init__(name)
        self.salary = salary
    def get_salary(self):
        return self.salary
    def __str__(self):
        return f"{self.name}的薪资是{self.get_salary()}"
class Programmer(Employee):
    def __init__(self, name, base_salary=12000, over_time=0):
        super().__init__(name)
        self.base_salary = base_salary
        self.__over_time = over_time
    def get_salary(self):
        if self.__over_time < 0:
            raise ValueError("工作时长的输入有误")
        elif self.__over_time > 20:
            self.__over_time = 20
        return self.base_salary + 100 * self.__over_time
    def __str__(self):
        return f"{self.name}的薪资是{self.get_salary()}"
class SoftTest(Employee):
    def __init__(self,name,base_salary=8000,bug_num=0):
        super().__init__(name)
        self.base_salary = base_salary
        self.bug_num = bug_num
    def get_salary(self):
        return self.base_salary + 5 * self.bug_num
    def __str__(self):
        return f"{self.name}的薪资是{self.get_salary()}"
def main():
    employee_list = [
        Manager("宋江"),Manager("吴用"),Manager("公孙胜",10000),
        Programmer("花荣"),Programmer("武松",10000,10),Programmer("林冲",13000,30),
        SoftTest("朱武"),SoftTest("蒋敬"),SoftTest("柴进",9000,100)
    ]
    for emp in employee_list:
        if isinstance(emp,Programmer):
            print("程序员：",emp)
        elif isinstance(emp,Manager):
            print("产品经理：",emp)
        else:
            print("测试工程师：",emp)
if __name__ == "__main__":
    main()
