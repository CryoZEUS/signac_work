#init.py

import signac

project = signac.init_project('MyProject')

for i in range(10):
	project.open_job({'a': i}).init()

	