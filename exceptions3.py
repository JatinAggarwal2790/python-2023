while True:
	try:
		amount = int(input("Enter the amount you wish to withdraw: "))
	except ValueError:
		print("Enter a valid amount")
	else:
		print("Collect your cash")
		break
