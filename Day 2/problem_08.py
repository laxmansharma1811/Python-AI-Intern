class Employee:
    salary = 10000
    increment = 10

    @property
    def salary_after_increment(self):
        print(f'The increment salary is {self.salary + self.salary *(self.increment/100)}')

    @salary_after_increment.setter
    def salary_after_increment(self, salary):
        self.increment = ((salary/self.salary) - 1)*100



e = Employee()
e.salary_after_increment = 15000
print(e.increment)