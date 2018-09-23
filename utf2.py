from urllib.request import urlopen
#Extended library for opening urls
import sys

count = 0

while True:
	walled_garden = urlopen("http://ctf.slothparadise.com/walled_garden.php?name=Brian").read().decode('utf-8')
	first_split = walled_garden.split("<pre>")
	second_split = first_split[1].split("</pre>")
	#print(second_split[0])

	#Open URL w/ concatenation
	URL = "http://ctf.slothparadise.com/walled_garden.php?name=Brian&captcha=" + second_split[0]
	#print(URL)

	walled_garden = urlopen(URL).read().decode('utf-8')

	count+=1

	if count == 1337:
		sys.exit(0)
		print("done")
