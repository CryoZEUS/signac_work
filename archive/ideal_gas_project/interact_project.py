#Interacting with signac project

"""
You interact with the signac project on the command line using the signac command. 
You can also interact with the project within Python via the signac.Project class. 
You can obtain an instance of that class within the project root directory and all sub-directories with:
"""

import signac 
project = signac.get_project()

#to iterate through jobs:

for job in project:
	print(job)

	