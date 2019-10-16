import sys
import subprocess
import re

if not re.search(".*&.*", sys.argv[1]): #regex found no matches
	subprocess.run("echo " + sys.argv[1], shell=True)
else:
	print(sys.argv[1] + " is not valid input")