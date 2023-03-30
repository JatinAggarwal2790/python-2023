def divide(a,b):
	try:
		result = a/b
	except ZeroDivisionError:
		print("Check your denominator")
	except TypeError:
		print("Check your types")
	except Exception:
		print("Something went wrong")
	else:
		print(result)


divide(5,2)
divide(5,0)
divide('a','b')