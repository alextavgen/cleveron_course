
class Employee:
    def __init__(self, name, surname, salary, payoutday=None):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.payoutday = payoutday

    def print(self):
        print(self.name + ' ' + self.surname)
        print('Salary is %s' % self.salary)
        print('Payoutday %s' % self.payoutday)

    def calculate_salary(self):
        pass



class ContractedEmployee(Employee):
    def __init__(self, name, surname, salary, payoutday=None,
                 contract_startdate = None, contract_length=None):

        super().__init__(name, surname, salary, payoutday)
        self.contract_startdate = contract_startdate
        self.contract_length = contract_length
        self.tax_coefficient = 0.5

    def print(self):
        super().print()
        print('Contract start date %s' % self.contract_startdate)
        print('Contract length %s' % self.contract_length)

    def calculate_salary(self):
        return self.salary - self.salary * self.tax_coefficient


class YoungEmployee(Employee):
    def __init__(self, name, surname, salary, payout_day=None,
                 age=None, job_length=None):
        super().__init__(name, surname, salary,payout_day)
        self.age = age
        self.job_length = job_length
        self.tax_coefficient = 0.2

    def print(self):
        super().print()
        print('Age is %s' %self.age)
        print('Job length %s' % self.job_length)

    def calculate_salary(self):
        return 100 + (self.salary - self.salary * self.tax_coefficient)

employee = Employee('John', 'Smith', 4000)

employee_list = list()
contracted_employee = ContractedEmployee('Gerd', 'Schikk', 5000,
                                         contract_startdate='12:10:2019',
                                         contract_length=12)
employee_list.append(contracted_employee)
employee_list.append(ContractedEmployee('Vivek', 'Scharma', 4500,
                                         contract_startdate='12:10:2019',
                                         contract_length=12))
employee_list.append(ContractedEmployee('Ricco', 'Ferma', 4300,
                                         contract_startdate='12:10:2019',
                                         contract_length=12))

employee_list.append(YoungEmployee('Richard', 'West', 1000,
                                   age=16, job_length=4))

employee_list.append(YoungEmployee('James', 'Big', 1200,
                                   age=18, job_length=4))

for employee in employee_list:
    print('Employee %s salary is %s' % (employee.name,
                                        employee.calculate_salary()))
