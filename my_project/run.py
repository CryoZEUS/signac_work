#run.py

import signac
from operations import hello
project = signac.get_project()

for job in project:
	hello(job)

	