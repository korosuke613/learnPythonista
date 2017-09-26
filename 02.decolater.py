import time

def instrument(func):
	import functools
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		import time
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__, ":", end - start)
	return wrapper
	
@instrument
def foo():
	time.sleep(1)
	
foo()
print(foo.__name__)
