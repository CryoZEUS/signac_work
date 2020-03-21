#project.py

#To implement a more automated workflow, we can subclass a FlowProject

import signac
from flow import FlowProject

class Project(FlowProject):
	pass

	#Defining a workflow (begin):

def greeted(job):
	return job.isfile('hello.txt')

@Project.operation
@Project.post(greeted)
def hello(job):
	with job:
		with open('hello.txt', 'w') as file:
			file.write('world!\n')

	#Defining a workflow (end)



if __name__ == '__main__':
	Project().main()
	