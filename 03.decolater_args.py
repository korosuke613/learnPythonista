def change_result(result):
	def receive_func(func):
		import functools
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
			return result
		return wrapper
	return receive_func
	
@change_result(False)
def foo():
	return True
	
print(foo())

