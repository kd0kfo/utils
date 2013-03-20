from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
import os.path as OP
from getopt import getopt,GetoptError

try:
    (opts,args) = getopt(argv[1:],"m:",["match="])
except GetoptError as ge:
    from sys import stderr
    stderr.write(ge)
    stderr.write("\n")
    exit(1)

pattern = None

for (opt, optarg) in opts:
    while opt[0] == '-':
        opt = opt[1:]
    if opt in ["m","match"]:
        pattern = optarg

url = args[0]

url_base = "/".join(url.split("/")[0:-1])

html = urlopen(url).read()
soup = BeautifulSoup(html,"lxml")

links = [link.get('href') for link in soup.find_all('a')]

for link in links:
    if "http://" not in link:
        link = "{0}/{1}".format(url_base,link)
    if not pattern or pattern in link:
        filename = link.split("/")[-1]
        print("Downloading {0} ({1})".format(filename,link))
        content = urlopen(link).read()
        with open(filename,"w") as outfile:
            outfile.write(content)
        
