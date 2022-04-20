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

	#Use func from SDK
	devices = dnac.devices.get_device_list()

	for device in devices["response"]:
		print(f"ID: {device['id']} IP: {device['managementIpAddress']}")


if __name__ == '__main__':
	main()