class EmployeeAccount(object):
	
	def __init__(self, employeecode, name, gender, salary):
		self.__EmployeeCode = employeecode
		self.Gender = gender
		self._Name = name
		self.Salary = salary

	def tax(self,amount):
		self.Salary = salary
		amount = 2000
		if salary > 10000:
			deduction = salary-amount
			return deduction

		else:
			return salary

	def vacation(self,gen):
		if gen > female:
			return "30-day vacation"

		else:
			return "15-day vacation"



		
