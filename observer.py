"""New"""
class BusinessCustomer:

	def __init__(self, acc_id, money_owed):
		"""Constructor to store information"""
		self.acc_id = acc_id
		self.money_owed = money_owed


	def update(self):
		"""Updater method"""
		if self.money_owed > 0:
			print(f"{self.acc_id}: Call finance department")
		else:
			print(f"{self.acc_id}: Balance paid")


class ConsumerCustomer:

	def __init__(self, acc_id, money_owed):
		"""Constructor to store information"""
		self.acc_id = acc_id
		self.money_owed = money_owed


	def update(self):
		"""Updater method"""
		if self.money_owed > 0:
			print(f"{self.acc_id}: Send email reminder")
		else:
			print(f"{self.acc_id}: Balance paid")

class AccountingSystem:
	"""Maintains list of observers"""
	def __init__(self):
		"""Constructor creates a new, empty accounting system with an 
		empty set of customers (observers/subscribers)"""
		self.customers = set()


	def register(self, customer):
		"""New signup"""
		self.customers.add(customer)

	def unregister(self, customer):
		"""Remove customer"""
		self.customers.remove(customer)


	def notify(self):
		"""Notify"""
		for customer in self.customers:
			customer.update()



def main():
	"""Exec starts here"""

	"""Customer list"""
	cust1 = BusinessCustomer("Acc1", 100)
	cust2 = BusinessCustomer("Acc2", 20)
	cust3 = BusinessCustomer("Acc3", -10)
	cust4 = BusinessCustomer("Acc4", 0)

	"""Create the acc system (subject) and register new customers"""
	accounting_sys = AccountingSystem()
	accounting_sys.register(cust1)
	accounting_sys.register(cust2)
	accounting_sys.register(cust3)
	accounting_sys.register(cust4)

	"""Run the notification to all subscribers"""
	accounting_sys.notify()

	"""Unregister cleared account customers"""
	accounting_sys.unregister(cust4)
	print("** Acc4 has cancelled their accout after clearing")

	accounting_sys.notify()


if __name__ == '__main__':
	main()
