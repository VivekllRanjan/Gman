#!/usr/bin/env python

import requests

def meraki_get(resource):
	"""
	Helper function to reduce repetitive HTTP GET statements. Takes in a specific REST 
	resource abd returns the JSON-formatted body text.
	"""

	#Declaring variables
	api_path = "https://n1.meraki.com/api/v0"
	headers ={
		"Content-Type": "application/json",
		"X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
	}

	#HTTP GET req
	get_resp = requests.get(f"{api_path}/{resource}",headers=headers)

	#Checking status code
	get_resp.raise_for_status()

	return get_resp.json()


def main():
	"""
	Exec starts here
	"""

	#Get list of organizations
	orgs = meraki_get("organizations")
	print("Orgs discovered:")

	devnet_id = 0
	for org in orgs:
		print(f"ID: {org['id']:<6} Name: {org['name']}")
		if "devnet" in org["name"].lower():
			devnet_id = org["id"]

	if devnet_id:
		networks = meraki_get(f"organizations/{devnet_id}/networks")

		#Printing networks with their network IDs
		print(f"\nNetworks seen for DevNet org ID {devnet_id}:")

		devnet_network = ""
		for network in networks:
			print(f"Network ID {network['id']} Name: {network['name']}")
			if "devnet" in network["name"].lower():
				devnet_network = network["id"]

		#If we find the DenNet network
		if devnet_network:
			#Get the devices from the DevNet network
			devices = meraki_get(f"networks/{devnet_network}/devices")

			#Print the networks with their IDs 
			print(f"\nDevices seen on DenNet network {devnet_network}:")

			for device in devices:
				print(f"Model: {device['model']:<8} IP: {device['lanIp']}")

if __name__ == '__main__':
	main()