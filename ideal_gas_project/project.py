#project.py
import signac
from flow import FlowProject
import os
import json

@FlowProject.label
def volume_computed(job):
	return job.isfile("volume.txt")

@FlowProject.operation
@FlowProject.post(volume_computed)
@FlowProject.post.isfile("data.json")
def store_volume_in_json_file(job):
	with open(job.fn("volume.txt")) as textfile:
		with open(job.fn("data.json"), "w") as jsonfile:
			data = {"volume" : float(textfile.read())}
			jsonfile.write(json.dumps(data) + "\n")

def compute_volume(job):
	volume = job.sp.N * job.sp.kT / job.sp.p
	with open(job.fn('volume.txt'), 'w') as file:
		file.write(str(volume) + '\n')


if __name__ == '__main__':
	FlowProject().main()