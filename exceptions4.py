try:
	print('a'/'b')
except Exception as err:
	print("Check your data")
	print(type(err))
	print(err)