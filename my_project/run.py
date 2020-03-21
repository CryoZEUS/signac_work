#run.py

import signac
from operations import hello
project = signac.get_project()


def greeted(job):
	return job.isfile('hello.txt')

	
for job in project:
	if not greeted(job):
		hello(job)

	