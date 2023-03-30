def get_line_count(filename):
	try:
		with open(filename, 'r') as f:
			linecount = len(f.read())
	except Exception:
		print("Supply correct path")
	else:
		print(filename,linecount)
	finally:
		print("bye bye")


get_line_count("exceptions1.py")
get_line_count("2do.txt")
get_line_count("3do.txt")