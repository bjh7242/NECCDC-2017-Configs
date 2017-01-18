#!/usr/bin/env python
'''
Author: Jared Stroud
Purpose: Quick and dirty script to spawn machines for NECCDC-2016
Disclaimer: This is terrible.
'''

import os
import argparse
import pdb

def get_ips():
	'''
	Name: get_ips()
	Description: Obtain IP addresses from text file.
				 Each address is on a new line.	
	Return: List of (strings) IPv4 addresses.
	'''
	with open("DO_ips.txt") as fin:
		addresses = fin.readlines()

	addresses = [address.strip() for address in addresses]
	return addresses

def get_domains():
	'''
	Name: get_domains()
	Description: Obtain domain names from text file.
				 Each domain is on a new line.	
	Return: List of (strings) domain names.
	'''
	with open("DO_domains.txt") as fin:
		domains = fin.readlines()

	domains = [domain.strip() for domain in domains]
	return domains 

def DO_subdomain_creator(subdomain, list_of_ips):
	#for counter, address in enumerate(list_of_ips):
		#print("blueteam%s-%s.fantasysports.trade --> %s" % (str(counter), subdomain, address))
	#	os.system("./fantasytrade-update blueteam%s-%s %s\n" % (str(counter), str(subdomain), str(address)))
	x = 1
	for address in list_of_ips:
		print("blueteam%s-%s --> %s\n" % (str(x), str(subdomain), str(address)))
		x += 1
		if x > 10:
			break

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('--subdomain', required=True, help="Specify subdomain to update for DO")
	args = parser.parse_args()
	ipv4_addresses = get_ips()
	DO_subdomain_creator(args.subdomain, ipv4_addresses)
