import sqlite3

table_name = 'bank'
connect = sqlite3.connect("data_base.db")
cursor = connect.cursor()

def create():
	account_number = input("Enter Account number: ")
	customer_name = input("Enter Customer name: ")
	balance = float(input("Enter Balance: "))
	cursor.execute('INSERT INTO %s VALUES("%s", "%s", %f)'%(table_name, account_number, customer_name, balance))
	save()

def show():
	records = cursor.execute('SELECT * FROM %s'%table_name)
	for record in records:
		display(record)

def update():
	account_number = input("Enter account number to update balance: ")
	balance = float(input("Enter balance: "))
	cursor.execute('UPDATE %s SET balance = %f where account_number = "%s"'%(table_name, balance, account_number))
	save()

def delete():
	account_number = input("Enter account number to close account: ")
	cursor.execute('DELETE FROM %s WHERE account_number = "%s"'%(table_name, account_number))
	save()

def search():
	account_number = input("Enter account number to search: ")
	# record = cursor.execute('SELECT * FROM %s where account_number = "%s"'%(table_name, account_number))
	records = cursor.execute('SELECT * FROM %s'%table_name)
	for record in records:
		if record[0] == account_number:
			display(record)

def display(record):
	print("Account number:", record[0])
	print("Customer name:", record[1])
	print("Balance:", record[2])

def save():
	connect.commit()

while True:
	print("My Bank")
	print("1. Open an Account", "2. Show All Accounts", "3. Update balance", "4. Close Account", "5. Search account", "6. Exit", sep ="\n")
	functions = [create, show, update, delete, search, exit]
	try:
		choice = int(input("Enter your choice: "))
		functions[choice - 1]()
	except ValueError:
		print("\nEnter a valid input!\n")
	except IndexError:
		print("\nEnter a valid choice!\n")