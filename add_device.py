#!/usr/bin/env python

import time
import requests
from auth_token import get_token

def main():
	"""
	Execution starts here
	"""

	#Get token
	token = get_token()

	#Variables
	api_path = "https://sandboxdnac.cisco.com/dna"
	headers = {"Content-Type": "application/json", "X-Auth-Token": token}

	#Create a dict to represent the device to be added
	new_dev_dict = {
	"ipAddress": ["92.0.1.2"],
	"cliTransport": "ssh",
	"password": "secret123",
	"enablePassword": "secret456",
	"snmpAuthPassphrase": "v3",
	"snmpAuthProtocol": "v3",
	"snmpMode": "enable",
	"snmpPrivPassphrase": "secret",
	"snmpPrivProtocol": "v3",
	"snmpROCommunity": "readonly",
	"snmpRWCommunity": "readwrite",
	"snmpRetry": "1",
	"snmpTimeout": "60",
	"snmpUserName": "devnetuser",
	}

	#HTTP POST to add device
	add_resp = requests.post(
		f"{api_path}/intent/api/v1/network-device", json=new_dev_dict, headers=headers,
		)

	if add_resp.ok:
		# Wait 20 sec after server responds
		print(f"Request accepted: status code {add_resp.status_code}")
		time.sleep(20)

		#Query DNA center for the statusof the specific task ID
		task = add_resp.json()["response"]["taskId"]
		task_resp = requests.get(
			f"{api_path}/intent/api/v1/task/{task}",headers=headers
			)
		if task_resp.ok:
			task_data = task_resp.json()["response"]
			if not task_data["isError"]:
				print("New device added successfully")
			else:
				print(f"Async task error seen: {task_data['progress']}")
		else:
			print(f"Asunc GET failed: status code {task_resp.status_code}")
	else:
		#Initial HTTP POST failed; print details
		print(f"Device addition failed with code {add_resp.status_code}")
		print(f"Failure body: {add_resp.text}")

if __name__ == '__main__':
	main()