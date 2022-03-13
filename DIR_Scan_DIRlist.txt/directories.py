import tkinter as tk
from tkinter.filedialog import askopenfilename
from turtle import color
from urllib import request
import requests
import sys
from termcolor import colored, cprint


print(colored(
	'''
	8888b.  88 88""Yb     .dP"Y8  dP""b8    db    88b 88 
	 8I  Yb 88 88__dP     `Ybo." dP   `"   dPYb   88Yb88 
	 8I  dY 88 88"Yb      o.`Y8b Yb       dP__Yb  88 Y88 
	8888Y"  88 88  Yb     8bodP'  YboodP dP""""Yb 88  Y8 

	┌┐ ┬ ┬  ┬┌┬┐┌┬┐┬ ┬┬┌┬┐┌─┐ ┬  ┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐┬
	├┴┐└┬┘  │ │  │ ├─┤│ ││├┤  │  ├─┤├┬┘├─┤│││└─┐├┬┘│
	└─┘ ┴   ┴ ┴  ┴ ┴ ┴┴─┴┘└─┘└┘  ┴ ┴┴└─┴ ┴┴ ┴└─┘┴└─┴
	'''
, 'blue'))
print(colored("Select Directory list .txt", 'yellow'))
root = tk.Tk()
root.withdraw()
filename = askopenfilename()
target_url = input(colored('[*] Enter Target URL: https://', 'yellow'))

def request(url):
	try:
		return requests.get("https://" + url)
	except requests.exceptions.ConnectionError:
		pass


file = open(filename, 'r')
for line in file:
	directory = line.strip()
	full_url = target_url + '/' + directory
	response = request(full_url)
	if response:
		print(colored('[*] Discovered Directory: ' + 'https://' + full_url, 'green'))
