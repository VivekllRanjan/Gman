#!/usr/bin/env python

import requests
from auth_token import get_token 
import json

def main():
	#Exec begins here

	"""GET token"""
	token=get_token()

	"""Declaring variables"""
	api_path = "https://sandboxdnac.cisco.com/dna"
	auth = ("devnetuser","Cisco123!")
	headers = {"Content-Type": "application/json", "X-Auth-Token":token}

	#GET request 
	get_resp = requests.get(
		f"{api_path}/intent/api/v1/network-device", headers=headers
		)
	#Printing the devices
	print(json.dumps(get_resp.json(), indent=2))

	#Iterating over list of dict and print device ID and management IP
	if get_resp.ok:
		for device in get_resp.json()["response"]:
			print(f"ID: {device['id']} IP: {device['managementIpAddress']}")

	else:
		print(f"Device collection failes with code {get_resp.status_code}")
		print(f"Failure body: {get_resp.text}")

if __name__ == "__main__":
	main()