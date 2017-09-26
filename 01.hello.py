class Hello:
	@classmethod
	def hello(cls):
		cls.str = 'Hello Python!'
		print(cls.str)

def main():
	Hello.hello()

if __name__ == '__main__':
	main()

