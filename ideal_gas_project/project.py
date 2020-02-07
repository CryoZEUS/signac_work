#project.py
import signac
from flow import FlowProject
import os
import json
import numpy as np

@FlowProject.label
def volume_computed(job):
	return job.isfile("volume.txt")

@FlowProject.operation
@FlowProject.pre.after(volume_computed)
@FlowProject.post.isfile("data.json")
def store_volume_in_json_file(job):
	with open(job.fn("volume.txt")) as textfile:
		with open(job.fn("data.json"), "w") as jsonfile:
			data = {"volume" : float(textfile.read())}
			jsonfile.write(json.dumps(data) + "\n")

	with job.data:
		job.data.my_array = np.zeros(64,32)

	

#Add another operation to this script  that stores the volume in the job document:
@FlowProject.operation
@FlowProject.post(lambda job: 'volume' in job.document)
def store_volume_in_document(job):
	with open(job.fn("volume.txt")) as textfile:
		job.document.volume = float(textfile.read())

#Besides needing fewer lines of code, storing data in the job document has one more distinct advantage: 
#It is directly searchable. That means that we can find and select jobs based on its content.

def compute_volume(job):
	volume = job.sp.N * job.sp.kT / job.sp.p
	with open(job.fn('volume.txt'), 'w') as file:
		file.write(str(volume) + '\n')


if __name__ == '__main__':
	FlowProject().main()


