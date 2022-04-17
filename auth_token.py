#!/usr/bin/env python

import requests

def get_token():
	"""Gets access token"""

	"""Declaring variables"""
	api_path = "https://sandboxdnac.cisco.com/dna"
	auth = ("devnetuser","Cisco123!")
	headers = {"Content-Type": "application/json"}

	#Issue the http post req
	auth_resp = requests.post(
		f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers
		)

	#If successful, print the token. Else, raise HTTPError details
	auth_resp.raise_for_status()
	token = auth_resp.json()["Token"]
	return token


def main():
	#Exec begins here

	token = get_token()
	print(token)


if __name__ == "__main__":
	main()