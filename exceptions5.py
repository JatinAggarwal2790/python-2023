import os, sys
try:
	print('a'/'b')
except Exception as err:
	ex_type ,ex_obj, ex_tb = sys.exc_info()
	print(ex_type)
	print(ex_obj)
	print(dir(ex_tb))
	#'tb_frame', 'tb_lasti', 'tb_lineno', 'tb_next'
	print(ex_tb.tb_frame)
	print(ex_tb.tb_lasti)
	print(ex_tb.tb_lineno)
	print(ex_tb.tb_next)

	filename = os.path.split(ex_tb.tb_frame.f_code.co_filename)[1]
	print(f"Exception occured in {filename} at line {ex_tb.tb_lineno}")
