#!usr/bin/python


import os


def run(**args):
	print "[*] in dir list module."
	files  = os.listdir(".")

	return str(files)


	