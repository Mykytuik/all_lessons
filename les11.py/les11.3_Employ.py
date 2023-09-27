class Employee:
    _count=0
    employ_dic=list()
    def __init__(self,_name, _salary=100):
        self._name=_name
        self._salary=_salary
        Employee._count+=1
        Employee.employ_dic+=[[_name,_salary]]


    # @property
    # def name(self):
    #     return self._name
    # @name.setter
    # def name(self,n):
    #     self._name=n


    # @property
    # def salary(self):
    #     return self._salary
    # @salary.setter
    # def salary(self,s):
    #     self._salary=s


    def __total__(self):
        print(f"total number of employees:{Employee._count}")
    
    def __information__(self):
        for i in range(Employee._count):
            print(f" {Employee.employ_dic[i]} gets {Employee.employ_dic[i]}$")
empl1=Employee("Mike",300)
empl2=Employee("Misha",1000)
Employee.__information__(Employee)
Employee.__total__(Employee)