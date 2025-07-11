class SalaryNotInRange(Exception):
    def __init__(self, salary, message = "Salary not in range (1000, 2000)"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

try:
    salary = int(input("Enter Salary : "))
    if not(1000 <= salary <= 2000):
        raise SalaryNotInRange(salary)
except ValueError:
    print("Not a Number!")