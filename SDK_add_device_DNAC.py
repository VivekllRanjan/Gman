#!/usr/bin/env python

from dnacentersdk import api

def main():
	"""
	Exec starts here
	"""

	#Creating DNAC object : Which automatically handles token req
	dnac = api.DNACenterAPI(
		base_url="https://sandboxdnac.cisco.com",
		username="devnetuser",
		password="Cisco123!",
		)

	#New device dict
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
	"snmpRetry": 1,
	"snmpTimeout": 60,
	"snmpUserName": "devnetuser",
	}

	#Use func from SDK
	add_dev = dnac.devices.add_device(**new_dev_dict)

	#Wait for response 
	time.sleep(10)
	task = add_dev["response"]["taskId"]
	task_data = dnac.task.get_task_by_id(task)

	if not task_data["response"]["isError"]:
		print("New device added")
	else:
		print(f"Async task error seen: {task_data['progress']}")


		
if __name__ == '__main__':
	main()