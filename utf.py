from urllib.request import urlopen
#Extended library for opening urls
import sys


while True:
	about_page = urlopen("http://ctf.slothparadise.com/about.php").read().decode('utf-8')
	if "KEY" in about_page:
		print(about_page)
		sys.exit(0)