#operations.py
from time import sleep


def hello(job):
	print('hello', job)
	sleep(1)
	#with job:
		#with open('hello.txt', 'w') as file:
			#file.write('world!\n')

if __name__ == '__main__':
	import flow
	flow.run()
	