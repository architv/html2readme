from bs4 import BeautifulSoup
path = raw_input('Give your file path along with name and extension: ')
html = open(path).read()
soup = BeautifulSoup(html)
heading = soup.h1.string + "\n"
heading += "================================\n\n"
para = soup.p.string + "\n\n"
li = ""
for lis in soup.find_all('li'):
	li += "* " + lis.string + "\n"
	#print li
total = heading + para + li
print total
with open("README.md", 'wb') as f:
	f.write(total)