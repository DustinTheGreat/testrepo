#!usr/bin/python


import os


def run(**args):
	print "[*] in eviroment module"
	return str(os.environ)