"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.hour = 0
        self.rate = 0

        self.bonus = 0
        self.numberOfContract = 0
        self.ratePerContract = 0
        
    def setSalaryContract(self, value):
        self.salary = value
    
    def setHourlyContract(self, hour, rate):
        self.hour = hour
        self.rate = rate

    def setComissionContract(self, number, rate):
        self.numberOfContract = number
        self.ratePerContract = rate

    def setBonusContract(self, value):
        self.bonus = value

    def get_pay(self):
        total = 0
        total += self.salary + self.hour*self.rate
        total += self.bonus + self.numberOfContract*self.ratePerContract
        return total

    def __str__(self):
        string = f"{self.name} works on a "
        if self.salary > 0: string += f"monthly salary of {self.salary}"
        else: string += f"contract of {self.hour} hours at {self.rate}/hour"

        if self.bonus > 0:
            string += f" and receives a bonus commission of {self.bonus}"
        elif self.numberOfContract > 0:
            string += f" and receives a commission for {self.numberOfContract} contract(s) at {self.ratePerContract}/contract"
        
        string += f". Their total pay is {self.get_pay()}."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.setSalaryContract(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.setHourlyContract(100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.setSalaryContract(3000)
renee.setComissionContract(4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.setHourlyContract(150, 25)
jan.setComissionContract(3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.setSalaryContract(2000)
robbie.setBonusContract(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.setHourlyContract(120, 30)
ariel.setBonusContract(600)
